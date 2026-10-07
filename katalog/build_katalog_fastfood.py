#!/usr/bin/env python3
"""EUPLUS fast food & restoran ambalajları kataloğu (PDF) üretici.

Kullanım:  python3 katalog/build_katalog_fastfood.py
Girdi:     katalog/urunler.json (katalog="fastfood" bölümleri) + katalog/gorseller/hx-*.jpg
           + logos/euplus/euplus.svg (vektör logo)
Çıktı:     katalog/EUPLUS-Fast-Food-Katalogu-2026.pdf
Bağımlılık: reportlab, Pillow, pymupdf

Kaynak: Helmex 2023 kataloğu (kaynaklar/helmex). Bölümler üç grupta; her bölüm: başlık bloğu,
1–3 tanıtım fotoğrafı ve genel tablo motoru (bölümün `sutunlar` ya da `tablolar` tanımı).
Uzun tablolar (çanta, kağıt) sonraki sayfaya taşar. Şeffaf kaplar için build_katalog.py,
Promocup paket servis için build_katalog_servis.py kullanılır; üçü aynı görsel dili paylaşır.
"""
import json, math, os, io
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, white
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "EUPLUS-Fast-Food-Katalogu-2026.pdf")
LOGO_SVG = os.path.join(ROOT, "logos", "euplus", "euplus.svg")
DATA = json.load(open(os.path.join(HERE, "urunler.json"), encoding="utf-8"))
YEAR = "2026"
TITLE = "Fast Food & Restoran Ambalajları"

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
M = 40; TOP = H - 58; BOT = 46; CW = W - 2 * M
COMPANY = "EUPLUS Lojistik Ambalaj San. Tic. A.Ş."
ADDRESS = "Mersinli Mah. 2829 Sokak No:3, 1. Sanayi Sitesi, 35170 İzmir / TÜRKİYE"
PHONE = "Tel: +90 232 421 41 41   ·   Faks: +90 232 421 41 66"
WEB = "www.euplus.com.tr"

SECTIONS = {int(k): v for k, v in DATA["bolumler"].items() if v.get("katalog") == "fastfood"}
ORDER = sorted(SECTIONS)
PRODUCTS = [p for p in DATA["urunler"] if p["bolum"] in SECTIONS]
GROUPS = {1: ("Karton Servis Ambalajları", "Paper Takeaway Products", "gorseller/hx-burger-kutusu.jpg"),
          2: ("Kağıt Çanta ve Ambalaj Kağıtları", "Paper Bags & Wraps", "gorseller/hx-luks-canta.jpg"),
          3: ("Tamamlayıcı Ürünler", "Complementary Products", "gorseller/hx-ahsap-catal-bicak.jpg")}
def items_of(sec): return [p for p in PRODUCTS if p["bolum"] == sec]
def by_code(): return {p["kod"]: p for p in PRODUCTS}

# ---------------- yardımcılar ----------------
_img_cache = {}
def img(path):
    if path not in _img_cache:
        im = Image.open(path); _img_cache[path] = ImageReader(im if im.mode == "RGBA" else im.convert("RGB"))
    return _img_cache[path]
def gpath(rel): return os.path.join(HERE, rel)

def logo(c, x, y, w, h):
    _logo_slots.append((page_no[0] - 1, (x, H - (y + h), x + w, H - y)))

def draw_fit(c, path, x, y, w, h, pad=0):
    r = img(path); iw, ih = r.getSize()
    s = min((w - 2 * pad) / iw, (h - 2 * pad) / ih); dw, dh = iw * s, ih * s
    c.drawImage(r, x + (w - dw) / 2, y + (h - dh) / 2, dw, dh, mask="auto")

def rounded_image(c, path, x, y, w, h, r=10):
    c.saveState(); p = c.beginPath(); p.roundRect(x, y, w, h, r); c.clipPath(p, stroke=0, fill=0)
    ir = img(path); iw, ih = ir.getSize(); s = max(w / iw, h / ih); dw, dh = iw * s, ih * s
    c.drawImage(ir, x + (w - dw) / 2, y + (h - dh) / 2, dw, dh, mask="auto"); c.restoreState()
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.roundRect(x, y, w, h, r, fill=0, stroke=1)

def text(c, x, y, s, font="R", size=9, color=INK, align="l"):
    c.setFont(font, size); c.setFillColor(color)
    if align == "l": c.drawString(x, y, s)
    elif align == "r": c.drawRightString(x, y, s)
    else: c.drawCentredString(x, y, s)

def fit_text(c, x, y, s, font, size, width, color=INK, align="l", min_size=5.5):
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
def val(s): return str(s) if s not in ("", None) else "—"

def chips(c, x, y, items):
    for t in items:
        tw = pdfmetrics.stringWidth(t, "B", 7) + 24
        c.setStrokeColor(ORANGE); c.setLineWidth(0.8); c.setFillColor(white); c.roundRect(x, y - 4.5, tw, 14, 7, fill=1, stroke=1)
        c.setFillColor(ORANGE); c.circle(x + 8.5, y + 2.5, 2.2, fill=1, stroke=0)
        text(c, x + 15, y, t, "B", 7, INK); x += tw + 6

# ---------------- sayfa iskeleti ----------------
page_no = [0]; _logo_slots = []
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
    text(c, M, H - 215, TITLE, "B", 30, INK)
    text(c, M, H - 243, f"Ürün Kataloğu {YEAR}  ·  Burger, pizza ve tavuk kutuları, bardak, çanta, kağıt ve tamamlayıcı ürünler", "R", 11, MUTED)
    rounded_image(c, gpath("gorseller/hx-kapak-hero.jpg"), M, 120, CW, 440, r=12)
    c.setFillColor(ORANGE); c.rect(0, 0, W, 92, fill=1, stroke=0)
    text(c, M, 60, COMPANY, "B", 11, white); text(c, M, 44, ADDRESS, "R", 8.5, white); text(c, M, 30, PHONE + "   ·   " + WEB, "R", 8.5, white)
    c.showPage()

# ---------------- giriş + içindekiler ----------------
def intro(c, toc, index_page):
    header_footer(c, "Katalog hakkında")
    y = TOP - 10
    text(c, M, y, "Fast food ve restoranın tüm ambalajı tek elden", "B", 19, INK); y -= 24
    body = ("EUPLUS Lojistik Ambalaj, fast food, restoran, kafe ve paket servis işletmeleri için karton kutudan kağıt çantaya, "
            "bardaktan peçeteye bütün servis ambalajlarını tek çatı altında sunar. Bu katalogda burger, tavuk, pizza ve pasta kutuları, "
            "patates kapları, tepsiler, noodle kutuları, kovalar, kaseler, karton bardaklar; düz ve burgu saplı kağıt çantalar, yağlı kağıt "
            "torbalar, lüks çantalar, ambalaj ve tepsi kağıtları ile streç film, sos kabı, ıslak mendil, peçete, fritöz filtresi ve "
            "ahşap çatal-bıçak yer alır. Karton ürünlerde beyaz, kraft veya siyah yüzey; flekso, ofset ya da dijital baskı ile "
            "markanıza özel tasarım yapılır. Standart ölçüler dışındaki talepler için özel üretim mümkündür.")
    for ln in wrap(c, body, "R", 9.5, CW): text(c, M, y, ln, "R", 9.5, INK); y -= 13.5
    y -= 6
    feats = [("Gıdaya uygun", "Tüm ürünler gıdayla temasa uygun hammaddeden üretilir"),
             ("Özel baskı", "Flekso, ofset veya dijital baskı ile markanıza özel tasarım"),
             ("Özel ölçü", "Standart ölçüler dışında talebe göre üretim, 1–2 haftada numune"),
             ("Palet bazlı", "Adetler koli ve 80×120 / 100×120 palet düzenine göre verilmiştir")]
    bw = (CW - 3 * 10) / 4; bh = 62
    for i, (t, d) in enumerate(feats):
        x = M + i * (bw + 10)
        c.setFillColor(PAPER); c.setStrokeColor(LINE); c.roundRect(x, y - bh, bw, bh, 6, fill=1, stroke=1)
        text(c, x + 10, y - 20, t, "B", 12, ORANGE); yy = y - 33
        for ln in wrap(c, d, "R", 7, bw - 20): text(c, x + 10, yy, ln, "R", 7, MUTED); yy -= 9
    y -= bh + 22
    text(c, M, y, "İçindekiler", "B", 15, INK); y -= 7
    c.setStrokeColor(ORANGE); c.setLineWidth(1); c.line(M, y, M + 60, y); y -= 14
    col_w = (CW - 16) / 2; n = len(toc); half = math.ceil(n / 2); y0 = y
    for i, (num, title, pg, cnt, grp) in enumerate(toc):
        col = 0 if i < half else 1; row = i if i < half else i - half
        x = M + col * (col_w + 16); yy = y0 - row * 14.5
        text(c, x, yy, f"{num:02d}", "B", 8.5, ORANGE)
        fit_text(c, x + 20, yy, title, "B", 8.5, col_w - 50, INK)
        text(c, x + col_w, yy, str(pg), "B", 8.5, INK, "r")
        c.setStrokeColor(LINE); c.setLineWidth(0.3); c.line(x, yy - 4, x + col_w, yy - 4)
    y = y0 - half * 14.5 - 6
    text(c, M + 20, y, "Ürün listesi (tablo)", "B", 8.5, INK); text(c, M + col_w, y, str(index_page), "B", 8.5, INK, "r")
    y -= 20
    text(c, M, y, "Tablolardaki alanlar", "B", 9, INK); y -= 12
    legend = [("Koli içi", "Bir kolideki ürün adedi; parantez içi fişek düzeni (ör. 125×4)"), ("Koli ölçüsü", "Dış koli ölçüsü U × G × Y, milimetre"),
              ("Palet", "Bir palete sığan koli (veya paket) sayısı"), ("MOQ", "Minimum sipariş adedi"),
              ("Üst / alt ölçü", "Kutu ve tepsilerde üst ağız ve taban ölçüsü, milimetre"), ("gsm", "Kağıt / karton gramajı")]
    for i, (k, v) in enumerate(legend):
        x = M + (i % 2) * (CW / 2); yy = y - (i // 2) * 11
        text(c, x, yy, k, "B", 7.5, GRAY); text(c, x + 56, yy, v, "R", 7.5, INK)
    c.showPage()

# ---------------- grup ayırıcı ----------------
def divider(c, gnum, secs, start_num):
    page_no[0] += 1
    title, en, pic = GROUPS[gnum]
    c.setFillColor(white); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(ORANGE); c.rect(0, H * 0.5, W, H * 0.5, fill=1, stroke=0)
    c.setFillColor(white); c.roundRect(W - M - 84, H - 52, 84, 44, 6, fill=1, stroke=0); logo(c, W - M - 78, H - 45, 72, 30)
    text(c, M, H - 170, f"{gnum:02d}", "B", 64, white)
    text(c, M, H - 215, title, "B", 26, white); text(c, M, H - 236, en, "R", 13, white)
    y = H - 268
    for i, s in enumerate(secs):
        text(c, M, y, f"{start_num + i:02d}  {SECTIONS[s]['ad']}", "B", 9.5, white); y -= 13.5
        if y < H * 0.5 + 12: break
    rounded_image(c, gpath(pic), M, 60, CW, H * 0.5 - 90, r=10)
    text(c, M, 40, f"{COMPANY}   ·   {WEB}", "R", 7, MUTED)
    c.showPage()

# ---------------- tablo motoru ----------------
ROW_H = 12.2
def rows_for(products):
    out = []
    for p in products:
        if p.get("varyantlar"):
            for v in p["varyantlar"]:
                r = dict(p); r.pop("varyantlar", None); r.update(v); out.append(r)
        else: out.append(p)
    return out

def tables_of(sec_id):
    sec = SECTIONS[sec_id]; items = items_of(sec_id); bc = {p["kod"]: p for p in items}
    if sec.get("tablolar"):
        return [(t.get("baslik"), t["sutunlar"], rows_for([bc[k] for k in t["urunler"] if k in bc])) for t in sec["tablolar"]]
    return [(None, sec["sutunlar"], rows_for(items))]

def table_height(tables):
    return sum((14 if t[0] else 0) + 15 + len(t[2]) * ROW_H + 10 for t in tables)

def draw_table(c, y, cols, rows, title, sec_title, continued=False):
    """Tabloyu çizer; gerekirse yeni sayfaya taşar. Yeni y döner."""
    scale = CW / sum(w for _, _, w, _ in cols); cols = [(n, k, w * scale, a) for n, k, w, a in cols]
    def head(y, cont=False):
        if title:
            text(c, M, y + 2, title + (" (devam)" if cont else ""), "B", 8.5, INK); y -= 13
        c.setFillColor(GRAY); c.rect(M, y - 4, CW, 15, fill=1, stroke=0); x = M + 4
        for name, _, w, al in cols:
            fit_text(c, x + (w - 8 if al == "r" else 0), y, name, "B", 7, w - 8, white, al); x += w
        return y - 15
    y = head(y, continued)
    for i, r in enumerate(rows):
        if y - ROW_H < BOT:
            c.showPage(); header_footer(c, sec_title + " (devam)"); y = TOP - 10; y = head(y, True)
        if i % 2: c.setFillColor(PAPER); c.rect(M, y - 4, CW, ROW_H, fill=1, stroke=0)
        x = M + 4
        for name, key, w, al in cols:
            v = r.get(key, ""); v = val(v)
            if key in ("koli",) and v != "—": v = dimsx(v)
            f = "B" if key == "kod" else "N"; col = ORANGE if key == "kod" else INK
            fit_text(c, x + (w - 8 if al == "r" else 0), y, v, f, 7.5, w - 8, col, al); x += w
        y -= ROW_H
    c.setStrokeColor(LINE); c.setLineWidth(0.5); c.line(M, y + ROW_H - 4, W - M, y + ROW_H - 4)
    return y - 8

# ---------------- bölüm sayfası ----------------
def section_pages(c, num, sec_id):
    sec = SECTIONS[sec_id]; tables = tables_of(sec_id); stitle = f"{num:02d}  {sec['ad']}"
    header_footer(c, stitle)
    y = TOP - 14
    text(c, M, y - 10, f"{num:02d}", "B", 30, ORANGE)
    fit_text(c, M + 48, y, sec["ad"], "B", 18, CW - 48, INK)
    fit_text(c, M + 48, y - 14, f"{sec['en']}  ·  {sec.get('slogan', '')}", "R", 9, CW - 48, MUTED)
    y -= 34
    for ln in wrap(c, sec.get("ozet", ""), "R", 8.5, CW)[:3]: text(c, M, y, ln, "R", 8.5, INK); y -= 11.5
    y -= 6; chips(c, M, y, ["Gıdaya uygun", "Özel baskı yapılır", "Özel ölçü üretilir"]); y -= 20
    # tanıtım fotoğrafları
    pics = [sec.get(k) for k in ("gorsel", "gorsel2", "gorsel3") if sec.get(k)]
    th = table_height(tables); notes_h = 12 * len(sec.get("notlar", [])) + (10 if sec.get("notlar") else 0)
    avail = y - BOT - th - notes_h - 14
    hero_h = max(110, min(250, avail))
    gap = 10; pw = (CW - gap * (len(pics) - 1)) / len(pics)
    if len(pics) == 1:
        iw, ih = img(gpath(pics[0])).getSize(); nat = CW * ih / iw
        if 150 <= nat < hero_h: hero_h = nat
    for i, pic in enumerate(pics): rounded_image(c, gpath(pic), M + i * (pw + gap), y - hero_h, pw, hero_h)
    y -= hero_h + 18
    for title, cols, rows in tables:
        if y - 40 < BOT: c.showPage(); header_footer(c, stitle + " (devam)"); y = TOP - 10
        y = draw_table(c, y, cols, rows, title, stitle)
    notes = sec.get("notlar", [])
    if notes:
        need = sum(len(wrap(c, n, "R", 7, CW - 12)) for n in notes) * 9.5 + 14
        if y - need < BOT: c.showPage(); header_footer(c, stitle + " (devam)"); y = TOP - 10
        c.setFillColor(TINT); c.roundRect(M, y - need, CW, need, 6, fill=1, stroke=0); yy = y - 11
        for n in notes:
            for ln in wrap(c, n, "R", 7, CW - 12): text(c, M + 6, yy, ln, "R", 7, INK); yy -= 9.5
        y -= need + 8
    c.showPage()

# ---------------- ürün listesi ----------------
def index_table(c):
    cols = [("Kod", 92, "l"), ("Ürün", 150, "l"), ("Ölçü", 92, "l"), ("Materyal", 96, "l"), ("Koli içi", 46, "r"), ("Palet", 39, "r")]
    def head(y):
        c.setFillColor(GRAY); c.rect(M, y - 4, CW, 15, fill=1, stroke=0); x = M + 4
        for name, wd, al in cols: text(c, x + (wd - 8 if al == "r" else 0), y, name, "B", 7, white, al); x += wd
        return y - 15
    header_footer(c, "Ürün listesi"); y = TOP - 8
    text(c, M, y, "Ürün listesi", "B", 16, INK); y -= 24; y = head(y); rh = 12.2
    for num, sec in enumerate(ORDER, start=1):
        items = items_of(sec)
        if y - rh * 2 < BOT: c.showPage(); header_footer(c, "Ürün listesi"); y = TOP - 8; y = head(y)
        c.setFillColor(TINT); c.rect(M, y - 4, CW, rh, fill=1, stroke=0)
        text(c, M + 4, y, f"{num:02d}  {SECTIONS[sec]['ad']}", "B", 8, ORANGE); y -= rh
        for n, p in enumerate(items):
            if y - rh < BOT: c.showPage(); header_footer(c, "Ürün listesi"); y = TOP - 8; y = head(y)
            if n % 2: c.setFillColor(PAPER); c.rect(M, y - 4, CW, rh, fill=1, stroke=0)
            nv = len(p.get("varyantlar") or [])
            vals = [p["kod"], p["ad"] + (f"  ({nv} ölçü)" if nv else ""), p.get("olcu") or "—", p.get("materyal") or "—",
                    val(p.get("koli_ici")), val(p.get("palet"))]
            x = M + 4
            for (name, wd, al), v in zip(cols, vals):
                fit_text(c, x + (wd - 8 if al == "r" else 0), y, v, "B" if name == "Kod" else "N", 7.5, wd - 8, INK, al); x += wd
            y -= rh
    y -= 10
    note = ("Ölçü, ağırlık ve koli bilgileri üretici verilerine dayanır; ± %3 tolerans içerebilir. Baskılı ürünlerde minimum sipariş adedi "
            "tasarıma göre değişir; klişe bedeli ayrıca bildirilir. Sipariş öncesi güncel stok ve fiyat için lütfen bizimle iletişime geçin.")
    for ln in wrap(c, note, "R", 7.5, CW):
        if y < BOT: break
        text(c, M, y, ln, "R", 7.5, MUTED); y -= 10
    c.showPage()

def back(c):
    page_no[0] += 1
    c.setFillColor(GRAY); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(white); c.roundRect(M, H / 2 - 120, CW, 240, 12, fill=1, stroke=0)
    logo(c, M + 30, H / 2 + 20, 200, 80)
    text(c, M + 30, H / 2 - 5, COMPANY, "B", 12, INK); text(c, M + 30, H / 2 - 24, ADDRESS, "R", 9, INK)
    text(c, M + 30, H / 2 - 40, PHONE, "R", 9, INK); text(c, M + 30, H / 2 - 56, WEB, "B", 9, ORANGE)
    text(c, M + 30, H / 2 - 92, "Fiyat teklifi, numune ve özel baskı talepleriniz için bize ulaşın.", "R", 9, MUTED)
    text(c, W / 2, 40, f"© {YEAR} {COMPANY}", "R", 7.5, white, "c")
    c.showPage()

# ---------------- derleme ----------------
def render(c, starts=None):
    """starts: {sec_id: sayfa} — ilk geçişte None (sayfalar ölçülür)."""
    global _logo_slots
    page_no[0] = 0; _logo_slots = []
    found = {}
    toc = [(i, SECTIONS[s]["ad"], (starts or {}).get(s, 0), len(items_of(s)), SECTIONS[s].get("grup", 1)) for i, s in enumerate(ORDER, start=1)]
    index_page = (starts or {}).get("index", 0)
    cover(c); intro(c, toc, index_page)
    cur_group = None
    for num, s in enumerate(ORDER, start=1):
        g = SECTIONS[s].get("grup", 1)
        if g != cur_group:
            cur_group = g; secs = [x for x in ORDER if SECTIONS[x].get("grup", 1) == g]
            divider(c, g, secs, ORDER.index(secs[0]) + 1)
        found[s] = page_no[0] + 1
        section_pages(c, num, s)
    found["index"] = page_no[0] + 1
    index_table(c); back(c)
    return found

def build():
    # 1. geçiş: sayfa numaraları
    tmp = canvas.Canvas(io.BytesIO(), pagesize=A4); starts = render(tmp)
    # 2. geçiş: gerçek çıktı
    c = canvas.Canvas(OUT, pagesize=A4)
    c.setTitle(f"EUPLUS {TITLE} {YEAR}"); c.setAuthor(COMPANY); c.setSubject("Fast food ve restoran paket servis ambalajları")
    found = render(c, starts); assert found == starts, "sayfa numaraları iki geçişte farklı"
    c.save(); compress(OUT)
    print("yazıldı:", OUT, "—", page_no[0], "sayfa,", round(os.path.getsize(OUT) / 1e6, 1), "MB")

def compress(path):
    import fitz
    doc = fitz.open(path)
    doc.rewrite_images(dpi_threshold=201, dpi_target=200, quality=82, lossy=True, lossless=True)
    logo_pdf = fitz.open("pdf", fitz.open(LOGO_SVG).convert_to_pdf())
    for pi, r in _logo_slots: doc[pi].show_pdf_page(fitz.Rect(*r), logo_pdf, 0)
    tmp = path + ".tmp"; doc.ez_save(tmp, garbage=4, deflate=True); doc.close(); os.replace(tmp, path)

if __name__ == "__main__":
    build()
