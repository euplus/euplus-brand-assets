#!/usr/bin/env python3
"""EUPLUS paket servis ambalajları kataloğu (PDF) üretici.

Kullanım:  python3 katalog/build_katalog_servis.py
Girdi:     katalog/urunler.json (katalog="servis" bölümleri) + katalog/gorseller/pc-*.{jpg,png}
           + logos/euplus/euplus.svg (vektör logo)
Çıktı:     katalog/EUPLUS-Paket-Servis-Katalogu-2026.pdf
Bağımlılık: reportlab, Pillow, pymupdf

Kaynak: Promocup 2026 kataloğu (kaynaklar/promocup). Her bölüm tek sayfa: başlık bloğu,
tanıtım fotoğrafı (ya da ürün kartları) ve teknik tablo. Şeffaf sunum kapları kataloğu
için build_katalog.py kullanılır; ikisi aynı görsel dili paylaşır.
"""
import json, math, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "EUPLUS-Paket-Servis-Katalogu-2026.pdf")
LOGO = os.path.join(ROOT, "logos", "euplus", "euplus-2048.png")
LOGO_SVG = os.path.join(ROOT, "logos", "euplus", "euplus.svg")
_logo_slots = []
DATA = json.load(open(os.path.join(HERE, "urunler.json"), encoding="utf-8"))
YEAR = "2026"
TITLE = "Paket Servis Ambalajları"

# ---- marka renkleri (README renk tablosu) ----
ORANGE = HexColor("#EF7C00"); GRAY = HexColor("#878786"); INK = HexColor("#1A1A18")
MUTED = HexColor("#6B6B66"); LINE = HexColor("#E7E4DE"); PAPER = HexColor("#FBFAF8"); TINT = HexColor("#FDEBD9")

FONT_DIRS = ["/System/Library/Fonts/Supplemental", "/Library/Fonts", os.path.expanduser("~/Library/Fonts"),
             "/usr/share/fonts/truetype/dejavu", "/usr/share/fonts/truetype/msttcorefonts"]
def _find(*names):
    for d in FONT_DIRS:
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p): return p
    raise SystemExit(f"Font bulunamadı: {names}")
pdfmetrics.registerFont(TTFont("R", _find("Arial.ttf", "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("B", _find("Arial Bold.ttf", "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("N", _find("Arial Narrow.ttf", "Arial.ttf", "DejaVuSansCondensed.ttf")))

W, H = A4
M = 40; TOP = H - 58; BOT = 46
COMPANY = "EUPLUS Lojistik Ambalaj San. Tic. A.Ş."
ADDRESS = "Mersinli Mah. 2829 Sokak No:3, 1. Sanayi Sitesi, 35170 İzmir / TÜRKİYE"
PHONE = "Tel: +90 232 421 41 41   ·   Faks: +90 232 421 41 66"
WEB = "www.euplus.com.tr"

SECTIONS = {int(k): v for k, v in DATA["bolumler"].items() if v.get("katalog") == "servis"}
ORDER = sorted(SECTIONS)
PRODUCTS = [p for p in DATA["urunler"] if p["bolum"] in SECTIONS]
def items_of(sec): return [p for p in PRODUCTS if p["bolum"] == sec]

# ---------------- yardımcılar ----------------
_img_cache = {}
def img(path):
    if path not in _img_cache:
        im = Image.open(path)
        _img_cache[path] = ImageReader(im if im.mode == "RGBA" else im.convert("RGB"))
    return _img_cache[path]
def gpath(rel): return os.path.join(HERE, rel)

def logo(c, x, y, w, h):
    _logo_slots.append((page_no[0] - 1, (x, H - (y + h), x + w, H - y)))

def draw_fit(c, path, x, y, w, h, pad=0):
    r = img(path); iw, ih = r.getSize()
    s = min((w - 2 * pad) / iw, (h - 2 * pad) / ih); dw, dh = iw * s, ih * s
    c.drawImage(r, x + (w - dw) / 2, y + (h - dh) / 2, dw, dh, mask="auto")

def rounded_image(c, path, x, y, w, h, r=10):
    """Fotoğrafı yuvarlak köşeli kutuya 'cover' mantığıyla (taşan kısmı kırparak) yerleştirir."""
    c.saveState()
    p = c.beginPath(); p.roundRect(x, y, w, h, r); c.clipPath(p, stroke=0, fill=0)
    ir = img(path); iw, ih = ir.getSize()
    s = max(w / iw, h / ih); dw, dh = iw * s, ih * s
    c.drawImage(ir, x + (w - dw) / 2, y + (h - dh) / 2, dw, dh, mask="auto")
    c.restoreState()
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.roundRect(x, y, w, h, r, fill=0, stroke=1)

def text(c, x, y, s, font="R", size=9, color=INK, align="l"):
    c.setFont(font, size); c.setFillColor(color)
    if align == "l": c.drawString(x, y, s)
    elif align == "r": c.drawRightString(x, y, s)
    else: c.drawCentredString(x, y, s)

def fit_text(c, x, y, s, font, size, width, color=INK, align="l", min_size=6.0):
    """Metni genişliğe sığdırmak için punto küçültür (gerekirse)."""
    while size > min_size and pdfmetrics.stringWidth(s, font, size) > width: size -= 0.25
    text(c, x, y, s, font, size, color, align)

def wrap(c, s, font, size, width):
    words = s.split(); lines = []; cur = ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width: cur = t
        else: lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines

def dims(s): return s.replace("x", " × ") + " mm" if s else "—"
def dimsx(s): return s.replace("x", "×") if s else "—"
def val(s, unit=""): return (s + unit) if s else "—"

def chips(c, x, y, items):
    for t in items:
        tw = pdfmetrics.stringWidth(t, "B", 7) + 24
        c.setStrokeColor(ORANGE); c.setLineWidth(0.8); c.setFillColor(white)
        c.roundRect(x, y - 4.5, tw, 14, 7, fill=1, stroke=1)
        c.setFillColor(ORANGE); c.circle(x + 8.5, y + 2.5, 2.2, fill=1, stroke=0)
        text(c, x + 15, y, t, "B", 7, INK)
        x += tw + 6

def table(c, x, y, cols, rows, row_h=13):
    total = sum(w for _, w, _ in cols)
    c.setFillColor(GRAY); c.rect(x, y - 4, total, 15, fill=1, stroke=0)
    xx = x + 4
    for name, w, al in cols:
        text(c, xx + (w - 8 if al == "r" else 0), y, name, "B", 7, white, al); xx += w
    y -= 15
    for i, row in enumerate(rows):
        if i % 2: c.setFillColor(PAPER); c.rect(x, y - 4, total, row_h, fill=1, stroke=0)
        xx = x + 4
        for (name, w, al), v in zip(cols, row):
            if name == "Kod": fit_text(c, xx, y, v, "B", 7.5, w - 6, ORANGE, al)
            else: fit_text(c, xx + (w - 8 if al == "r" else 0), y, v, "N", 7.5, w - 8, INK, al)
            xx += w
        y -= row_h
    c.setStrokeColor(LINE); c.setLineWidth(0.5); c.line(x, y + row_h - 4, x + total, y + row_h - 4)
    return y

# ---------------- sayfa iskeleti ----------------
page_no = [0]
def header_footer(c, section_title=None):
    page_no[0] += 1
    c.setFillColor(white); c.rect(0, 0, W, H, fill=1, stroke=0)
    logo(c, M, H - 44, 70, 30)
    if section_title: text(c, W - M, H - 32, section_title.upper(), "B", 8.5, GRAY, "r")
    c.setStrokeColor(ORANGE); c.setLineWidth(1.2); c.line(M, H - 50, W - M, H - 50)
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(M, 34, W - M, 34)
    text(c, M, 22, f"{COMPANY}   ·   {WEB}   ·   {TITLE} {YEAR}", "R", 7, MUTED)
    text(c, W - M, 22, str(page_no[0]), "B", 8, GRAY, "r")

# ---------------- kapak ----------------
def cover(c):
    page_no[0] += 1
    c.setFillColor(white); c.rect(0, 0, W, H, fill=1, stroke=0)
    logo(c, M, H - 150, 230, 100)
    text(c, M, H - 215, TITLE, "B", 32, INK)
    text(c, M, H - 243, f"Ürün Kataloğu {YEAR}  ·  Karton bardak, kase, kutu, kapak ve kağıt çanta", "R", 12, MUTED)
    rounded_image(c, gpath("gorseller/pc-kapak-hero.jpg"), M, 120, W - 2 * M, 440, r=12)
    c.setFillColor(ORANGE); c.rect(0, 0, W, 92, fill=1, stroke=0)
    text(c, M, 60, COMPANY, "B", 11, white)
    text(c, M, 44, ADDRESS, "R", 8.5, white)
    text(c, M, 30, PHONE + "   ·   " + WEB, "R", 8.5, white)
    c.showPage()

# ---------------- giriş + içindekiler ----------------
def intro(c, toc, index_page):
    header_footer(c, "Katalog hakkında")
    y = TOP - 10
    text(c, M, y, "Paket servisin tüm ambalajı tek elden", "B", 20, INK); y -= 26
    body = ("EUPLUS Lojistik Ambalaj, kafe, restoran, pastane ve paket servis işletmeleri için karton ve plastik "
            "servis ambalajlarını tek çatı altında sunar. Bu katalogda tek ve çift katlı sıcak içecek bardakları, "
            "soğuk içecek bardakları, dondurma ve salata kaseleri, patates ve hamburger kutuları, mikro oluklu gıda "
            "kutuları, PET bardaklar, uyumlu kapaklar, taşıma viyolleri ve kağıt çantaları bulacaksınız. "
            "Tüm ürünler gıdayla temasa uygun hammaddeden üretilir; karton ürünlerde kraft veya beyaz yüzey, "
            "ofset / flekso / dijital baskı ile markanıza özel tasarım seçeneği vardır.")
    for ln in wrap(c, body, "R", 10, W - 2 * M):
        text(c, M, y, ln, "R", 10, INK); y -= 14.5
    y -= 10
    feats = [("Gıdaya uygun", "Tüm ürünler gıdayla temasa uygun hammaddeden üretilir"),
             ("Özel baskı", "Ofset, flekso veya dijital baskı ile markanıza özel tasarım"),
             ("Kraft / Beyaz", "Karton ürünlerde kraft veya beyaz yüzey seçeneği"),
             ("Fişek + koli", "Adetler fişek (iç paket) ve koli düzenine göre verilmiştir")]
    bw = (W - 2 * M - 3 * 10) / 4; bh = 74
    for i, (t, d) in enumerate(feats):
        x = M + i * (bw + 10)
        c.setFillColor(PAPER); c.setStrokeColor(LINE); c.roundRect(x, y - bh, bw, bh, 6, fill=1, stroke=1)
        text(c, x + 10, y - 24, t, "B", 13, ORANGE)
        yy = y - 40
        for ln in wrap(c, d, "R", 7.5, bw - 20):
            text(c, x + 10, yy, ln, "R", 7.5, MUTED); yy -= 10
    y -= bh + 30
    text(c, M, y, "İçindekiler", "B", 16, INK); y -= 8
    c.setStrokeColor(ORANGE); c.setLineWidth(1); c.line(M, y, M + 60, y); y -= 20
    for num, (title, en, pg, cnt) in enumerate(toc, start=1):
        text(c, M, y, f"{num:02d}", "B", 10.5, ORANGE)
        text(c, M + 26, y, title, "B", 10, INK)
        text(c, M + 26 + pdfmetrics.stringWidth(title, "B", 10) + 8, y, f"{en}  ·  {cnt} ürün", "R", 7.5, MUTED)
        text(c, W - M, y, str(pg), "B", 10, INK, "r")
        c.setStrokeColor(LINE); c.setLineWidth(0.4); c.line(M, y - 6, W - M, y - 6)
        y -= 19
    text(c, M + 26, y, "Ürün listesi (tablo)", "B", 10, INK)
    text(c, W - M, y, str(index_page), "B", 10, INK, "r")
    y -= 26
    text(c, M, y, "Tablolardaki alanlar", "B", 9.5, INK); y -= 13
    legend = [("Ağız / Dip Ø", "Bardak ve kaselerde ağız ve dip çapı, milimetre"), ("Yük.", "Ürün yüksekliği, milimetre"),
              ("Ağırlık", "Bir adet ürünün ağırlığı, gram"), ("Fişek", "İç paketteki (fişek) ürün adedi"),
              ("Koli içi", "Bir kolideki toplam ürün adedi"), ("Koli ölçüsü", "Dış koli ölçüsü U × G × Y, milimetre"),
              ("Net kg", "Dolu kolinin net ağırlığı, kilogram")]
    col_w = (W - 2 * M) / 2
    for i, (k, v) in enumerate(legend):
        x = M + (i % 2) * col_w; yy = y - (i // 2) * 11.5
        text(c, x, yy, k, "B", 7.5, GRAY); text(c, x + 58, yy, v, "R", 7.5, INK)
    c.showPage()

# ---------------- bölüm sayfası ----------------
COLS_BARDAK = [("Kod", 54, "l"), ("Ürün", 142, "l"), ("Ağız Ø", 34, "r"), ("Dip Ø", 34, "r"), ("Yük.", 32, "r"),
               ("Ağırlık", 40, "r"), ("Fişek", 34, "r"), ("Koli içi", 46, "r"), ("Koli ölçüsü (mm)", 66, "l"), ("Net kg", 33, "r")]
COLS_KAPAK = [("Kod", 66, "l"), ("Ürün", 170, "l"), ("Materyal", 46, "l"), ("Ağırlık", 40, "r"), ("Fişek", 36, "r"),
              ("Koli içi", 46, "r"), ("Koli ölçüsü (mm)", 76, "l"), ("Net kg", 35, "r")]

def rows_bardak(items):
    rows = []
    for p in items:
        ks = p.get("koli_secenekleri") or [{"koli_ici": p["koli_ici"], "koli": p["koli"], "net_kg": p.get("net_kg", "")}]
        for i, o in enumerate(ks):
            if i == 0:
                rows.append([p["kod"], p["ad"], val(p["agiz_capi"]), val(p["dip_capi"]), val(p["yukseklik"]), val(p["agirlik_g"], " g"),
                             val(p["fisek_ici"]), val(o["koli_ici"]), dimsx(o["koli"]), val(o["net_kg"])])
            else:
                rows.append(["", "    alternatif koli", "", "", "", "", "", val(o["koli_ici"]), dimsx(o["koli"]), val(o["net_kg"])])
    return rows

def rows_kapak(items):
    rows = []
    for p in items:
        ks = p.get("koli_secenekleri") or [{"koli_ici": p["koli_ici"], "koli": p["koli"], "net_kg": p.get("net_kg", "")}]
        o = ks[0]
        rows.append([p["kod"], p["ad"], p["materyal"] or "—", val(p["agirlik_g"], " g"), val(p["fisek_ici"]),
                     val(o["koli_ici"]), dimsx(o["koli"]), val(o["net_kg"])])
    return rows

def title_block(c, num, sec):
    y = TOP - 14
    text(c, M, y - 10, f"{num:02d}", "B", 30, ORANGE)
    text(c, M + 48, y, sec["ad"], "B", 18, INK)
    text(c, M + 48, y - 14, f"{sec['en']}  ·  {sec.get('slogan', '')}", "R", 9, MUTED)
    y -= 34
    for ln in wrap(c, sec.get("ozet", ""), "R", 8.5, W - 2 * M)[:2]:
        text(c, M, y, ln, "R", 8.5, INK); y -= 11.5
    y -= 6
    chips(c, M, y, ["Gıdaya uygun", "Özel baskı yapılır", "Çevre dostu"])
    return y - 20  # içerik üst sınırı

def card(c, p, x, y, w, h, show_mat=True):
    c.setFillColor(white); c.setStrokeColor(LINE); c.setLineWidth(0.7); c.roundRect(x, y, w, h, 8, fill=1, stroke=1)
    ph = h - 84
    c.setFillColor(PAPER); c.roundRect(x + 6, y + h - ph - 6, w - 12, ph, 6, fill=1, stroke=0)
    draw_fit(c, gpath(p["gorsel"]), x + 6, y + h - ph - 6, w - 12, ph, pad=14)
    ty = y + h - ph - 22
    text(c, x + 10, ty, p["kod"], "B", 10.5, ORANGE)
    if p.get("tedarikci_kodu"): pass
    lines = wrap(c, p["ad"], "B", 8.5, w - 20)[:2]
    for ln in lines: ty -= 12; text(c, x + 10, ty, ln, "B", 8.5, INK)
    if len(lines) == 1: ty -= 12
    ty -= 12
    if p["olcu"]: text(c, x + 10, ty, "Ölçü", "B", 7, GRAY); text(c, x + 48, ty, dims(p["olcu"]), "R", 7.5, INK); ty -= 10
    if show_mat and p["materyal"]: text(c, x + 10, ty, "Materyal", "B", 7, GRAY); fit_text(c, x + 48, ty, p["materyal"], "R", 7.5, w - 58, INK); ty -= 10

def section_page(c, num, sec_id):
    sec = SECTIONS[sec_id]; items = items_of(sec_id)
    header_footer(c, f"{num:02d}  {sec['ad']}")
    ytop = title_block(c, num, sec)
    kind = sec.get("tablo", "kapak")
    if kind in ("bardak", "kapak"):
        cols = COLS_BARDAK if kind == "bardak" else COLS_KAPAK
        rows = rows_bardak(items) if kind == "bardak" else rows_kapak(items)
        table_h = 15 + len(rows) * 13 + 8
        hero_h = max(150, min(300, ytop - BOT - table_h - 44))
        iw, ih = img(gpath(sec["gorsel"])).getSize()
        if sec.get("gorsel2"):
            gw = (W - 2 * M - 10) / 2
            hero_h = min(hero_h, gw * ih / iw)  # iki görsel yan yana: kırpmadan göster
            rounded_image(c, gpath(sec["gorsel"]), M, ytop - hero_h, gw, hero_h)
            rounded_image(c, gpath(sec["gorsel2"]), M + gw + 10, ytop - hero_h, gw, hero_h)
            text(c, M + gw / 2, ytop - hero_h - 12, "PET kapak · kristal şeffaf görünüm", "B", 7.5, GRAY, "c")
            text(c, M + gw + 10 + gw / 2, ytop - hero_h - 12, "PP kapak · hafif buzlu, ısıya dayanıklı", "B", 7.5, GRAY, "c")
            y = ytop - hero_h - 34
        else:
            nat_h = (W - 2 * M) * ih / iw
            if 200 <= nat_h < hero_h: hero_h = nat_h  # yer varsa fotoğrafı kırpmadan göster
            rounded_image(c, gpath(sec["gorsel"]), M, ytop - hero_h, W - 2 * M, hero_h)
            y = ytop - hero_h - 24
        y = table(c, M, y, cols, rows)
        notes = [p for p in items if p.get("not") and kind == "kapak"]
        if notes:
            y -= 8
            text(c, M, y, "Uyumluluk", "B", 7.5, GRAY); y -= 10
            for p in notes:
                if y < BOT + 6: break
                text(c, M, y, f"{p['kod']}: {p['not']}", "N", 7, MUTED); y -= 9
    elif kind == "kart":
        n = len(items); cols_ = 2 if n <= 2 else 3; rows_ = math.ceil(n / cols_); gap = 12
        cw = (W - 2 * M - (cols_ - 1) * gap) / cols_
        avail = ytop - BOT - 56
        ch = min((avail - (rows_ - 1) * gap) / rows_, 400 if rows_ == 1 else 300)
        for i, p in enumerate(items):
            col, row = i % cols_, i // cols_
            x = M + col * (cw + gap); y = ytop - (row + 1) * ch - row * gap
            card(c, p, x, y, cw, ch)
        y = ytop - rows_ * ch - (rows_ - 1) * gap - 16
        note = items[0].get("not") or "Baskılı veya baskısız; kraft ya da beyaz karton"
        c.setFillColor(TINT); c.roundRect(M, y - 30, W - 2 * M, 38, 6, fill=1, stroke=0)
        text(c, M + 12, y - 8, "Diğer ölçüler", "B", 8.5, INK)
        text(c, M + 12, y - 21, note + ". Farklı ölçü ve adetler için bizimle iletişime geçin.", "R", 7.5, MUTED)
        y -= 46
        if y - 70 > BOT:
            opts = [("Yüzey", "Kraft veya beyaz karton; gıdayla temasa uygun"),
                    ("Baskı", "Ofset, flekso veya dijital; markanıza özel tasarım"),
                    ("Sevkiyat", "Düz (açık) sevk edilir, kullanım anında katlanır")]
            bw = (W - 2 * M - 2 * 10) / 3
            for i, (t, d) in enumerate(opts):
                x = M + i * (bw + 10)
                c.setFillColor(PAPER); c.setStrokeColor(LINE); c.roundRect(x, y - 62, bw, 62, 6, fill=1, stroke=1)
                text(c, x + 10, y - 20, t, "B", 11, ORANGE)
                yy = y - 34
                for ln in wrap(c, d, "R", 7.5, bw - 20): text(c, x + 10, yy, ln, "R", 7.5, MUTED); yy -= 10
    elif kind == "canta":
        gap = 10; cw = (W - 2 * M - 3 * gap) / 4; ch = 215
        for i, p in enumerate(items):
            x = M + i * (cw + gap); y = ytop - ch
            c.setFillColor(white); c.setStrokeColor(LINE); c.setLineWidth(0.7); c.roundRect(x, y, cw, ch, 8, fill=1, stroke=1)
            c.setFillColor(PAPER); c.roundRect(x + 6, y + 40, cw - 12, ch - 46, 6, fill=1, stroke=0)
            draw_fit(c, gpath(p["gorsel"]), x + 6, y + 40, cw - 12, ch - 46, pad=10)
            text(c, x + cw / 2, y + 26, p["kod"], "B", 8, ORANGE, "c")
            lines = wrap(c, p["ad"].replace(" – ", " · "), "B", 7.5, cw - 12)[:1]
            text(c, x + cw / 2, y + 14, lines[0], "B", 7.5, INK, "c")
        y = ytop - ch - 26
        half = (W - 2 * M - 14) / 2
        text(c, M, y, "Ölçü aralığı", "B", 10, INK)
        text(c, M + half + 14, y, "Seçenekler", "B", 10, INK); y -= 8
        c.setStrokeColor(ORANGE); c.setLineWidth(1); c.line(M, y, M + 50, y); c.line(M + half + 14, y, M + half + 64, y); y -= 16
        rng = [("Körük (derinlik)", "9 – 26 cm"), ("Genişlik", "22 – 55 cm"), ("Yükseklik", "20 – 62 cm"), ("Minimum sipariş", "25.000 adet")]
        yy = y
        for i, (k, v) in enumerate(rng):
            if i % 2 == 0: c.setFillColor(PAPER); c.rect(M, yy - 5, half, 16, fill=1, stroke=0)
            text(c, M + 6, yy, k, "B", 8, GRAY); text(c, M + half - 6, yy, v, "B", 8.5, INK, "r"); yy -= 16
        opts = [("Sap", "Burgu saplı · Düz saplı · SOS (yassı dipli) çanta"), ("Kağıt", "Kraft kağıt · Beyaz kağıt"),
                ("Baskı", "Ofset veya flekso; markanıza özel tasarım"), ("Teslimat", "Ölçü ve adet onayından sonra üretim")]
        yy = y
        for k, v in opts:
            text(c, M + half + 20, yy, k, "B", 8, GRAY); text(c, M + half + 62, yy, v, "R", 8, INK); yy -= 16
        y = yy - 10
        c.setFillColor(TINT); c.roundRect(M, y - 30, W - 2 * M, 38, 6, fill=1, stroke=0)
        text(c, M + 12, y - 8, "Siparişe özel üretim", "B", 8.5, INK)
        text(c, M + 12, y - 21, "Kağıt çantalar stoktan değil, ölçü / kağıt / sap ve baskı seçimine göre üretilir. Teklif için bizimle iletişime geçin.", "R", 7.5, MUTED)
    c.showPage()

# ---------------- ürün listesi ----------------
def index_table(c):
    cols = [("Kod", 64, "l"), ("Ürün", 158, "l"), ("Ölçü / çap (mm)", 86, "l"), ("Materyal", 66, "l"),
            ("Koli içi", 42, "r"), ("Koli ölçüsü (mm)", 68, "l"), ("Net kg", 31, "r")]
    def head(y):
        c.setFillColor(GRAY); c.rect(M, y - 4, W - 2 * M, 15, fill=1, stroke=0)
        x = M + 4
        for name, wd, al in cols:
            text(c, x + (wd - 8 if al == "r" else 0), y, name, "B", 7, white, al); x += wd
        return y - 15
    def olcu(p):
        if p.get("agiz_capi") and p.get("dip_capi"): return f"Ø{p['agiz_capi']} / Ø{p['dip_capi']} × {p['yukseklik']}"
        if p.get("agiz_capi"): return f"Ø{p['agiz_capi']}"
        return dimsx(p["olcu"])
    header_footer(c, "Ürün listesi"); y = TOP - 8
    text(c, M, y, "Ürün listesi", "B", 16, INK); y -= 24; y = head(y)
    rh = 12.2
    for num, sec in enumerate(ORDER, start=1):
        items = items_of(sec)
        if y - rh * 2 < BOT:
            c.showPage(); header_footer(c, "Ürün listesi"); y = TOP - 8; y = head(y)
        c.setFillColor(TINT); c.rect(M, y - 4, W - 2 * M, rh, fill=1, stroke=0)
        text(c, M + 4, y, f"{num:02d}  {SECTIONS[sec]['ad']}", "B", 8, ORANGE); y -= rh
        for n, p in enumerate(items):
            if y - rh < BOT:
                c.showPage(); header_footer(c, "Ürün listesi"); y = TOP - 8; y = head(y)
            if n % 2: c.setFillColor(PAPER); c.rect(M, y - 4, W - 2 * M, rh, fill=1, stroke=0)
            ks = p.get("koli_secenekleri") or []
            o = ks[0] if ks else {"koli_ici": p["koli_ici"], "koli": p["koli"], "net_kg": p.get("net_kg", "")}
            vals = [p["kod"], p["ad"], olcu(p), p["materyal"] or "—", val(o["koli_ici"]), dimsx(o["koli"]), val(o["net_kg"])]
            x = M + 4
            for (name, wd, al), v in zip(cols, vals):
                if name == "Kod": fit_text(c, x, y, v, "B", 7.5, wd - 6, INK, al)
                else: fit_text(c, x + (wd - 8 if al == "r" else 0), y, v, "N", 7.5, wd - 8, INK, al)
                x += wd
            y -= rh
    y -= 10
    note = ("Ölçü, ağırlık ve koli bilgileri üretici verilerine dayanır; ± %3 tolerans içerebilir. Baskılı ürünlerde minimum "
            "sipariş adedi tasarıma göre değişir. Sipariş öncesi güncel stok ve fiyat için lütfen bizimle iletişime geçin.")
    for ln in wrap(c, note, "R", 7.5, W - 2 * M):
        if y < BOT: break
        text(c, M, y, ln, "R", 7.5, MUTED); y -= 10
    c.showPage()

# ---------------- arka kapak ----------------
def back(c):
    page_no[0] += 1
    c.setFillColor(GRAY); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(white); c.roundRect(M, H / 2 - 120, W - 2 * M, 240, 12, fill=1, stroke=0)
    logo(c, M + 30, H / 2 + 20, 200, 80)
    text(c, M + 30, H / 2 - 5, COMPANY, "B", 12, INK)
    text(c, M + 30, H / 2 - 24, ADDRESS, "R", 9, INK)
    text(c, M + 30, H / 2 - 40, PHONE, "R", 9, INK)
    text(c, M + 30, H / 2 - 56, WEB, "B", 9, ORANGE)
    text(c, M + 30, H / 2 - 92, "Fiyat teklifi, numune ve özel baskı talepleriniz için bize ulaşın.", "R", 9, MUTED)
    text(c, W / 2, 40, f"© {YEAR} {COMPANY}", "R", 7.5, white, "c")
    c.showPage()

# ---------------- derleme ----------------
def build():
    c = canvas.Canvas(OUT, pagesize=A4)
    c.setTitle(f"EUPLUS {TITLE} {YEAR}"); c.setAuthor(COMPANY)
    c.setSubject("Karton bardak, kase, kutu, kapak ve kağıt çanta — paket servis ambalajları")
    toc = []; pg = 3
    for sec in ORDER:
        toc.append((SECTIONS[sec]["ad"], SECTIONS[sec]["en"], pg, len(items_of(sec)))); pg += 1
    cover(c); intro(c, toc, pg)
    for num, sec in enumerate(ORDER, start=1):
        before = page_no[0]
        section_page(c, num, sec)
        assert page_no[0] == before + 1, f"bölüm {sec} tek sayfaya sığmadı"
    assert page_no[0] + 1 == pg, "içindekiler sayfa numarası kaydı"
    index_table(c); back(c)
    c.save()
    compress(OUT)
    print("yazıldı:", OUT, "—", page_no[0], "sayfa,", round(os.path.getsize(OUT) / 1e6, 1), "MB")

def compress(path):
    import fitz
    doc = fitz.open(path)
    doc.rewrite_images(dpi_threshold=201, dpi_target=200, quality=82, lossy=True, lossless=True)
    logo_pdf = fitz.open("pdf", fitz.open(LOGO_SVG).convert_to_pdf())
    for pi, r in _logo_slots:
        doc[pi].show_pdf_page(fitz.Rect(*r), logo_pdf, 0)
    tmp = path + ".tmp"; doc.ez_save(tmp, garbage=4, deflate=True); doc.close(); os.replace(tmp, path)

if __name__ == "__main__":
    build()
