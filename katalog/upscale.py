#!/usr/bin/env python3
"""Seçilen ürün görsellerinin çözünürlüğünü yükseltir (Real-ESRGAN ile süper çözünürlük).

Kullanım (depo kökünden):
  python3 katalog/upscale.py --liste [--esik 400]        küçük görselleri listeler (uzun kenar < eşik)
  python3 katalog/upscale.py BKP9150 BK-CP618 ...         verilen ürün kodlarının görsellerini yükseltir
  python3 katalog/upscale.py --bolum 50                   bir bölümün tüm ürünlerini yükseltir
  python3 katalog/upscale.py --kucuk 300                  uzun kenarı 300 px altındaki tüm görselleri yükseltir
  python3 katalog/upscale.py --geri-al BKP9150            orijinal görseli geri yükler
  python3 katalog/upscale.py --motor lanczos KOD          Real-ESRGAN yoksa klasik büyütme (keskinleştirmeli)

Sonra:  python3 katalog/build_urunler.py  ve  python3 katalog/build_katalog.py gida   (ya da --derle)

Girdi/çıktı: katalog/urunler.json → gorsel yolu; görsel yerinde güncellenir, orijinali
katalog/gorseller/orijinal/ altına bir kez kopyalanır; işlem kaydı katalog/gorseller/orijinal/upscale-log.json.

Motor: ~/.euplus-tools/realesrgan/realesrgan-ncnn-vulkan (REALESRGAN ortam değişkeniyle değiştirilebilir).
Kurulum: https://github.com/xinntao/Real-ESRGAN/releases → realesrgan-ncnn-vulkan-20220424-macos.zip,
~/.euplus-tools/realesrgan/ altına aç, `xattr -dr com.apple.quarantine .` ve `chmod +x realesrgan-ncnn-vulkan`.

Şeffaflık: Real-ESRGAN alfa kanalını güvenilir işlemediği için RGB (beyaz zemine bindirilmiş) ve alfa
ayrı ayrı büyütülür, sonra beyaz zemin etkisi geri alınır (un-premultiply). Böylece PNG şeffaf kalır.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile
from datetime import date
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(HERE, "urunler.json")
ORIG = os.path.join(HERE, "gorseller", "orijinal")
LOG = os.path.join(ORIG, "upscale-log.json")
BIN = os.environ.get("REALESRGAN", os.path.expanduser("~/.euplus-tools/realesrgan/realesrgan-ncnn-vulkan"))
MODEL_DIR = os.path.join(os.path.dirname(BIN), "models")

def load():
    return json.load(open(DATA, encoding="utf-8"))

def products(args, D):
    by = {p["kod"].upper(): p for p in D["urunler"]}
    sel = []
    for k in args.kod:
        if k.upper() not in by: sys.exit(f"kod bulunamadı: {k}")
        sel.append(by[k.upper()])
    if args.bolum:
        sel += [p for p in D["urunler"] if p["bolum"] in args.bolum]
    if args.kucuk:
        for p in D["urunler"]:
            f = os.path.join(HERE, p["gorsel"]); name = os.path.basename(p["gorsel"])
            src = os.path.join(ORIG, name) if os.path.exists(os.path.join(ORIG, name)) else f   # daha önce büyütülmüşse orijinale bak
            if os.path.exists(src) and max(Image.open(src).size) < args.kucuk: sel.append(p)
    # aynı görseli paylaşan ürünler (kategori fotoğrafı) bir kez işlenir
    seen, out = set(), []
    for p in sel:
        if p["gorsel"] not in seen: seen.add(p["gorsel"]); out.append(p)
    return out

def listele(D, esik):
    rows = []
    for p in D["urunler"]:
        f = os.path.join(HERE, p["gorsel"])
        if not os.path.exists(f): continue
        w, h = Image.open(f).size
        if max(w, h) < esik: rows.append((max(w, h), p["kod"], p["ad"], f"{w}×{h}"))
    for n, kod, ad, wh in sorted(rows):
        print(f"{kod:16s} {wh:>10s}  {ad}")
    print(f"\n{len(rows)} görselin uzun kenarı {esik} px altında.")

# ---------------- motorlar ----------------
def run_realesrgan(im_rgb, scale, model):
    """RGB görseli Real-ESRGAN ile büyütür; PNG dosya üzerinden çalışır."""
    if not os.path.exists(BIN):
        sys.exit(f"Real-ESRGAN bulunamadı: {BIN}\nKurulum için betik başındaki açıklamaya bakın ya da --motor lanczos kullanın.")
    with tempfile.TemporaryDirectory() as td:
        i, o = os.path.join(td, "i.png"), os.path.join(td, "o.png")
        im_rgb.save(i)
        r = subprocess.run([BIN, "-i", i, "-o", o, "-n", model, "-s", str(scale), "-m", MODEL_DIR, "-f", "png"],
                           capture_output=True, text=True)
        if r.returncode != 0 or not os.path.exists(o):
            sys.exit("Real-ESRGAN hata verdi:\n" + (r.stderr or r.stdout))
        return Image.open(o).convert("RGB").copy()

def run_lanczos(im_rgb, scale, model=None):
    big = im_rgb.resize((im_rgb.width * scale, im_rgb.height * scale), Image.LANCZOS)
    return big.filter(ImageFilter.UnsharpMask(radius=2, percent=80, threshold=2))

ENGINES = {"realesrgan": run_realesrgan, "lanczos": run_lanczos}

# ---------------- şeffaflık korumalı büyütme ----------------
def upscale_rgba(im, engine, scale, model):
    im = im.convert("RGBA")
    a = np.asarray(im.split()[3]).astype(np.float32) / 255.0
    rgb = np.asarray(im.convert("RGB")).astype(np.float32)
    # beyaz zemine bindir (katalogda da beyaz zemin var; saçak rengi beyaz olur)
    comp = rgb * a[..., None] + 255.0 * (1 - a[..., None])
    big_rgb = np.asarray(engine(Image.fromarray(comp.round().astype(np.uint8)), scale, model)).astype(np.float32)
    # alfa'yı aynı motorla büyüt (gri → RGB olarak), kanal ortalamasını al
    a_img = Image.fromarray((a * 255).round().astype(np.uint8)).convert("RGB")
    big_a = np.asarray(engine(a_img, scale, model)).astype(np.float32).mean(axis=2) / 255.0
    big_a = np.clip(big_a, 0, 1)
    # un-premultiply: F = (C - (1-a)·255) / a   (a küçükken bölme patlamasın)
    safe = np.maximum(big_a, 0.05)[..., None]
    fg = (big_rgb - 255.0 * (1 - big_a[..., None])) / safe
    fg = np.where(big_a[..., None] < 0.02, big_rgb, fg)
    out = Image.fromarray(np.clip(fg, 0, 255).round().astype(np.uint8))
    out.putalpha(Image.fromarray((big_a * 255).round().astype(np.uint8)))
    return out

def process(p, args, log):
    rel = p["gorsel"]; f = os.path.join(HERE, rel)
    src = Image.open(f); w0, h0 = src.size
    name = os.path.basename(rel)
    os.makedirs(ORIG, exist_ok=True)
    bak = os.path.join(ORIG, name)
    if not os.path.exists(bak): shutil.copy2(f, bak)     # orijinal bir kez saklanır
    base = Image.open(bak)                                 # her zaman orijinalden büyüt (üst üste işleme yok)
    engine = ENGINES[args.motor]
    transparent = base.mode in ("RGBA", "LA") or (base.mode == "P" and "transparency" in base.info)
    big = upscale_rgba(base, engine, args.olcek, args.model) if transparent else engine(base.convert("RGB"), args.olcek, args.model)
    if max(big.size) > args.hedef: big.thumbnail((args.hedef, args.hedef), Image.LANCZOS)
    big.save(f, optimize=True)
    log[name] = dict(kod=p["kod"], tarih=str(date.today()), motor=args.motor, model=args.model if args.motor == "realesrgan" else "",
                     olcek=args.olcek, once=[w0, h0], sonra=list(big.size))
    print(f"{p['kod']:16s} {w0}×{h0} → {big.size[0]}×{big.size[1]}  ({rel})")

def restore(kodlar, D, log):
    by = {p["kod"].upper(): p for p in D["urunler"]}
    for k in kodlar:
        p = by.get(k.upper()) or sys.exit(f"kod bulunamadı: {k}")
        name = os.path.basename(p["gorsel"]); bak = os.path.join(ORIG, name)
        if not os.path.exists(bak): print(f"{k}: orijinal yedeği yok, atlandı"); continue
        shutil.copy2(bak, os.path.join(HERE, p["gorsel"])); log.pop(name, None)
        print(f"{k}: orijinal geri yüklendi")

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("kod", nargs="*", help="ürün kodu (BKP9150, BK-CP618 ...)")
    ap.add_argument("--bolum", type=int, nargs="*", default=[], help="bölüm numarası (katalog/urunler.json)")
    ap.add_argument("--kucuk", type=int, default=0, help="uzun kenarı bu değerin altındaki tüm görselleri seç (px)")
    ap.add_argument("--liste", action="store_true", help="küçük görselleri listele")
    ap.add_argument("--esik", type=int, default=400, help="--liste için uzun kenar eşiği (px)")
    ap.add_argument("--motor", choices=ENGINES, default="realesrgan")
    ap.add_argument("--model", default="realesrgan-x4plus", help="Real-ESRGAN modeli (realesrgan-x4plus | realesrgan-x4plus-anime)")
    ap.add_argument("--olcek", type=int, default=4, help="büyütme katsayısı (x4 modeli için 4)")
    ap.add_argument("--hedef", type=int, default=1600, help="çıktıda uzun kenar üst sınırı (px)")
    ap.add_argument("--geri-al", action="store_true", help="verilen kodların orijinal görselini geri yükle")
    ap.add_argument("--derle", action="store_true", help="bitince build_urunler.py ve build_katalog.py gida çalıştır")
    args = ap.parse_args()
    D = load()
    if args.liste: return listele(D, args.esik)
    log = json.load(open(LOG, encoding="utf-8")) if os.path.exists(LOG) else {}
    if args.geri_al: restore(args.kod, D, log)
    else:
        sel = products(args, D)
        if not sel: sys.exit("ürün verilmedi. Örnek: python3 katalog/upscale.py BKP9150 BK-CP618   (--liste ile adaylara bakın)")
        for p in sel: process(p, args, log)
    os.makedirs(ORIG, exist_ok=True)
    json.dump(log, open(LOG, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if args.derle:
        subprocess.run([sys.executable, os.path.join(HERE, "build_urunler.py")], cwd=ROOT, check=True)
        subprocess.run([sys.executable, os.path.join(HERE, "build_katalog.py"), "gida"], cwd=ROOT, check=True)
    else:
        print("\nÜrün dosyalarını ve kataloğu yenilemek için:\n  python3 katalog/build_urunler.py && python3 katalog/build_katalog.py gida")

if __name__ == "__main__":
    main()
