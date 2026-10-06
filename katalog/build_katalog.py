#!/usr/bin/env python3
"""EUPLUS ürün kataloğu (PDF) üretici.

Kullanım:  python3 katalog/build_katalog.py
Girdi:     katalog/urunler.json (katalog="seffaf" bölümleri) + katalog/gorseller/*.png + logos/euplus/euplus.svg
Çıktı:     katalog/EUPLUS-Urun-Katalogu-2026.pdf
Bağımlılık: reportlab, Pillow (pip install reportlab pillow)
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
OUT = os.path.join(HERE, "EUPLUS-Urun-Katalogu-2026.pdf")
LOGO = os.path.join(ROOT, "logos", "euplus", "euplus-2048.png")
LOGO_SVG = os.path.join(ROOT, "logos", "euplus", "euplus.svg")
_logo_slots = []  # (sayfa indeksi, fitz Rect) — sıkıştırma sonrası vektör logo buraya gömülür
DATA = json.load(open(os.path.join(HERE, "urunler.json"), encoding="utf-8"))
YEAR = "2026"

# ---- marka renkleri (README renk tablosu) ----
ORANGE = HexColor("#EF7C00")
GRAY = HexColor("#878786")
INK = HexColor("#1A1A18")
MUTED = HexColor("#6B6B66")
LINE = HexColor("#E7E4DE")
PAPER = HexColor("#FBFAF8")

# ---- fontlar (Türkçe karakter desteği için TTF) ----
FONT_DIRS = ["/System/Library/Fonts/Supplemental", "/Library/Fonts", os.path.expanduser("~/Library/Fonts"),
             "/usr/share/fonts/truetype/dejavu", "/usr/share/fonts/truetype/msttcorefonts"]
def _find(*names):
    for d in FONT_DIRS:
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return p
    raise SystemExit(f"Font bulunamadı: {names}")
pdfmetrics.registerFont(TTFont("R", _find("Arial.ttf", "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont("B", _find("Arial Bold.ttf", "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont("N", _find("Arial Narrow.ttf", "Arial.ttf", "DejaVuSansCondensed.ttf")))

W, H = A4
M = 40            # yan kenar boşluğu
TOP = H - 58      # içerik üst sınırı
BOT = 46          # içerik alt sınırı

COMPANY = "EUPLUS Lojistik Ambalaj San. Tic. A.Ş."
ADDRESS = "Mersinli Mah. 2829 Sokak No:3, 1. Sanayi Sitesi, 35170 İzmir / TÜRKİYE"
PHONE = "Tel: +90 232 421 41 41   ·   Faks: +90 232 421 41 66"
WEB = "www.euplus.com.tr"

SECTIONS = {int(k): v for k, v in DATA["bolumler"].items() if v.get("katalog", "seffaf") == "seffaf"}
PRODUCTS = [p for p in DATA["urunler"] if p["bolum"] in SECTIONS]  # paket servis ürünleri build_katalog_servis.py'de
PER_PAGE = 9  # 3 x 3

_img_cache = {}
def img(path):
    if path not in _img_cache:
        im = Image.open(path)
        if path == LOGO and im.mode in ("RGBA", "LA", "P"):  # logoyu beyaz zemine düzleştir
            bg = Image.new("RGB", im.size, (255, 255, 255)); bg.paste(im.convert("RGBA"), mask=im.convert("RGBA").split()[3]); im = bg
        _img_cache[path] = ImageReader(im.convert("RGB") if im.mode != "RGBA" else im)
    return _img_cache[path]

def logo(c, x, y, w, h):
    """Logoyu vektör (SVG) olarak yerleştirmek üzere kaydeder; PyMuPDF yoksa PNG çizer."""
    try:
        import fitz  # noqa
        _logo_slots.append((page_no[0] - 1, (x, H - (y + h), x + w, H - y)))
    except ImportError:
        draw_fit(c, LOGO, x, y, w, h)

def draw_fit(c, path, x, y, w, h, pad=0):
    """Görseli (x,y,w,h) kutusuna oranını koruyarak ortalar."""
    r = img(path); iw, ih = r.getSize()
    s = min((w - 2 * pad) / iw, (h - 2 * pad) / ih)
    dw, dh = iw * s, ih * s
    c.drawImage(r, x + (w - dw) / 2, y + (h - dh) / 2, dw, dh, mask="auto")

def text(c, x, y, s, font="R", size=9, color=INK, align="l"):
    c.setFont(font, size); c.setFillColor(color)
    if align == "l": c.drawString(x, y, s)
    elif align == "r": c.drawRightString(x, y, s)
    else: c.drawCentredString(x, y, s)

def wrap(c, s, font, size, width):
    words = s.split(); lines = []; cur = ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width: cur = t
        else: lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines

def fmt_dims(s):
    return s.replace("x", " × ") + " mm" if s else "—"

def fmt_num(s, unit):
    return f"{s} {unit}" if s else "—"

# ---------------- sayfa iskeleti ----------------
page_no = [0]
def header_footer(c, section_title=None):
    page_no[0] += 1
    c.setFillColor(white); c.rect(0, 0, W, H, fill=1, stroke=0)
    # üst: logo + bölüm adı
    logo(c, M, H - 44, 70, 30)
    if section_title:
        text(c, W - M, H - 32, section_title.upper(), "B", 8.5, GRAY, "r")
    c.setStrokeColor(ORANGE); c.setLineWidth(1.2); c.line(M, H - 50, W - M, H - 50)
    # alt: firma + sayfa
    c.setStrokeColor(LINE); c.setLineWidth(0.6); c.line(M, 34, W - M, 34)
    text(c, M, 22, f"{COMPANY}   ·   {WEB}", "R", 7, MUTED)
    text(c, W - M, 22, str(page_no[0]), "B", 8, GRAY, "r")

# ---------------- kapak ----------------
def cover(c):
    page_no[0] += 1
    c.setFillColor(white); c.rect(0, 0, W, H, fill=1, stroke=0)
    logo(c, M, H - 150, 230, 100)
    text(c, M, H - 215, "Ürün Kataloğu", "B", 34, INK)
    text(c, M, H - 243, f"{YEAR}  ·  Şeffaf tatlı, çikolata ve bal ambalajları", "R", 12.5, MUTED)
    # ürün mozaiği 3x2
    picks = ["CP14", "CP41", "CP111", "CP165", "CP319", "CP185"]
    by = {p["kod"]: p for p in PRODUCTS}
    gx, gy, gw, gh, gap = M, 150, W - 2 * M, 430, 10
    cw = (gw - 2 * gap) / 3; ch = (gh - gap) / 2
    for i, k in enumerate(picks):
        x = gx + (i % 3) * (cw + gap); y = gy + gh - (i // 3 + 1) * ch - (i // 3) * gap
        c.setFillColor(PAPER); c.setStrokeColor(LINE); c.setLineWidth(0.6)
        c.roundRect(x, y, cw, ch, 8, fill=1, stroke=1)
        draw_fit(c, os.path.join(HERE, by[k]["gorsel"]), x, y, cw, ch, pad=16)
    # alt turuncu bant
    c.setFillColor(ORANGE); c.rect(0, 0, W, 92, fill=1, stroke=0)
    text(c, M, 60, COMPANY, "B", 11, white)
    text(c, M, 44, ADDRESS, "R", 8.5, white)
    text(c, M, 30, PHONE + "   ·   " + WEB, "R", 8.5, white)
    c.showPage()

# ---------------- giriş + içindekiler ----------------
def intro(c, toc):
    header_footer(c, "Katalog hakkında")
    y = TOP - 10
    text(c, M, y, "EUPLUS ile tatlınız hep vitrinde", "B", 20, INK); y -= 26
    body = ("EUPLUS Lojistik Ambalaj, gıda sektörüne yönelik şeffaf sunum ve servis ambalajlarını tek çatı altında "
            "sunar. Bu katalogda sütlü tatlılar, lokum ve çikolata ürünleri ile bal için tasarlanmış kristal şeffaf "
            "kase, kutu, kavanoz, tabak ve kapak çeşitlerini bulacaksınız. Tüm ürünler gıdayla temasa uygun "
            "polistiren (PS) veya PET hammaddeden üretilir; içeriği olduğu gibi gösterir, raf ömrü boyunca formunu korur.")
    for ln in wrap(c, body, "R", 10, W - 2 * M):
        text(c, M, y, ln, "R", 10, INK); y -= 14.5
    y -= 10
    # özellik kutuları
    feats = [("−10 °C", "Soğuk servis ve dolap saklama için uygun minimum sıcaklık"),
             ("+60 °C", "Sıcak dolum ve servis için uygun maksimum sıcaklık"),
             ("PS / PET", "Kristal şeffaf gövdeler PS, bombe ve düz kapaklar PET"),
             ("Euro palet", "Adetler 80 × 120 cm euro palet düzenine göre verilmiştir")]
    bw = (W - 2 * M - 3 * 10) / 4; bh = 74
    for i, (t, d) in enumerate(feats):
        x = M + i * (bw + 10)
        c.setFillColor(PAPER); c.setStrokeColor(LINE); c.roundRect(x, y - bh, bw, bh, 6, fill=1, stroke=1)
        text(c, x + 10, y - 24, t, "B", 14, ORANGE)
        yy = y - 40
        for ln in wrap(c, d, "R", 7.5, bw - 20):
            text(c, x + 10, yy, ln, "R", 7.5, MUTED); yy -= 10
    y -= bh + 34
    # içindekiler
    text(c, M, y, "İçindekiler", "B", 16, INK); y -= 8
    c.setStrokeColor(ORANGE); c.setLineWidth(1); c.line(M, y, M + 60, y); y -= 22
    for num, (title, en, pg, cnt) in enumerate(toc, start=1):
        text(c, M, y, f"{num:02d}", "B", 13, ORANGE)
        text(c, M + 30, y, title, "B", 12, INK)
        text(c, M + 30, y - 13, f"{en}  ·  {cnt} ürün", "R", 8, MUTED)
        text(c, W - M, y, str(pg), "B", 12, INK, "r")
        c.setStrokeColor(LINE); c.setLineWidth(0.5); c.line(M, y - 22, W - M, y - 22)
        y -= 40
    text(c, M, y, "Ürün listesi (tablo)", "B", 12, INK)
    text(c, W - M, y, str(toc[-1][2] + 1 + math.ceil(toc[-1][3] / PER_PAGE)), "B", 12, INK, "r")
    y -= 34
    # alan açıklamaları
    text(c, M, y, "Ürün kartlarındaki alanlar", "B", 10, INK); y -= 15
    legend = [("Ölçü", "En × boy × yükseklik, milimetre"), ("Hacim", "Nominal dolum hacmi, cc"),
              ("Koli", "Dış koli ölçüsü, milimetre"), ("Koli içi", "Bir kolideki ürün adedi"),
              ("Palet", "Bir euro palete sığan koli sayısı")]
    for k, v in legend:
        text(c, M, y, k, "B", 8.5, GRAY); text(c, M + 50, y, v, "R", 8.5, INK); y -= 12.5
    c.showPage()

# ---------------- bölüm ayırıcı ----------------
def divider(c, num, title, en, items, highlights):
    page_no[0] += 1
    c.setFillColor(white); c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(ORANGE); c.rect(0, H * 0.5, W, H * 0.5, fill=1, stroke=0)
    c.setFillColor(white); c.roundRect(W - M - 84, H - 52, 84, 44, 6, fill=1, stroke=0)
    logo(c, W - M - 78, H - 45, 72, 30)
    text(c, M, H - 190, f"{num:02d}", "B", 64, white)
    text(c, M, H - 240, title, "B", 30, white)
    text(c, M, H - 262, en, "R", 13, white)
    text(c, M, H * 0.5 + 24, f"{len(items)} ürün", "B", 10, white)
    by = {p["kod"]: p for p in PRODUCTS}
    gw = W - 2 * M; gap = 12; cw = (gw - 2 * gap) / 3; ch = 250; y = H * 0.5 - 40 - ch
    for i, k in enumerate(highlights):
        x = M + i * (cw + gap)
        c.setFillColor(PAPER); c.setStrokeColor(LINE); c.setLineWidth(0.6)
        c.roundRect(x, y, cw, ch, 8, fill=1, stroke=1)
        draw_fit(c, os.path.join(HERE, by[k]["gorsel"]), x, y + 26, cw, ch - 26, pad=14)
        text(c, x + cw / 2, y + 10, f"{k}  ·  {by[k]['ad']}", "B", 7.5, GRAY, "c")
    text(c, M, 22, f"{COMPANY}   ·   {WEB}", "R", 7, MUTED)
    c.showPage()

# ---------------- ürün kartı ----------------
def card(c, p, x, y, w, h):
    ph = 114  # fotoğraf alanı
    c.setFillColor(white); c.setStrokeColor(LINE); c.setLineWidth(0.7)
    c.roundRect(x, y, w, h, 7, fill=1, stroke=1)
    c.setStrokeColor(LINE); c.line(x + 8, y + h - ph - 6, x + w - 8, y + h - ph - 6)
    draw_fit(c, os.path.join(HERE, p["gorsel"]), x, y + h - ph - 4, w, ph, pad=10)
    ty = y + h - ph - 22
    text(c, x + 10, ty, p["kod"], "B", 11, ORANGE)
    lines = wrap(c, p["ad"], "B", 8.5, w - 20)[:2]
    for ln in lines:
        ty -= 12; text(c, x + 10, ty, ln, "B", 8.5, INK)
    if len(lines) == 1: ty -= 12  # tek satırlık adlarda hizayı koru
    ty -= 8
    rows = [("Ölçü", fmt_dims(p["olcu"])), ("Hacim", fmt_num(p["hacim"], "cc")), ("Materyal", p["materyal"] or "—"),
            ("Koli", fmt_dims(p["koli"])), ("Koli içi", fmt_num(p["koli_ici"], "adet")), ("Palet", fmt_num(p["palet"], "koli"))]
    for i, (k, v) in enumerate(rows):
        yy = ty - i * 10
        if i % 2 == 0:
            c.setFillColor(PAPER); c.rect(x + 6, yy - 3, w - 12, 10, fill=1, stroke=0)
        text(c, x + 10, yy, k, "B", 7, GRAY); text(c, x + 52, yy, v, "R", 7.5, INK)

def product_pages(c, title, items):
    cols, rows_ = 3, 3; gap = 12
    cw = (W - 2 * M - (cols - 1) * gap) / cols
    ch = (TOP - BOT - (rows_ - 1) * gap) / rows_
    for i, p in enumerate(items):
        k = i % PER_PAGE
        if k == 0:
            if i: c.showPage()
            header_footer(c, title)
        col, row = k % cols, k // cols
        x = M + col * (cw + gap); y = TOP - (row + 1) * ch - row * gap
        card(c, p, x, y, cw, ch)
    c.showPage()

# ---------------- ürün listesi tablosu ----------------
def index_table(c):
    cols = [("Kod", 52, "l"), ("Ürün", 132, "l"), ("Ölçü (mm)", 70, "l"), ("Hacim", 44, "r"), ("Materyal", 66, "l"),
            ("Koli (mm)", 70, "l"), ("Koli içi", 42, "r"), ("Palet", 38, "r")]
    def head(y):
        c.setFillColor(GRAY); c.rect(M, y - 4, W - 2 * M, 15, fill=1, stroke=0)
        x = M + 4
        for name, wd, al in cols:
            text(c, x + (wd - 6 if al == "r" else 0), y, name, "B", 7.5, white, al); x += wd
        return y - 15
    header_footer(c, "Ürün listesi"); y = TOP - 8
    text(c, M, y, "Ürün listesi", "B", 16, INK); y -= 24; y = head(y)
    rh = 12.2
    for sec in sorted(SECTIONS):
        items = [p for p in PRODUCTS if p["bolum"] == sec]
        if y - rh * 2 < BOT:
            c.showPage(); header_footer(c, "Ürün listesi"); y = TOP - 8; y = head(y)
        c.setFillColor(HexColor("#FDEBD9")); c.rect(M, y - 4, W - 2 * M, rh, fill=1, stroke=0)
        text(c, M + 4, y, SECTIONS[sec]["ad"], "B", 8, ORANGE); y -= rh
        for n, p in enumerate(items):
            if y - rh < BOT:
                c.showPage(); header_footer(c, "Ürün listesi"); y = TOP - 8; y = head(y)
            if n % 2: c.setFillColor(PAPER); c.rect(M, y - 4, W - 2 * M, rh, fill=1, stroke=0)
            vals = [p["kod"], p["ad"], p["olcu"].replace("x", "×") or "—", (p["hacim"] + " cc") if p["hacim"] else "—",
                    p["materyal"] or "—", p["koli"].replace("x", "×") or "—", p["koli_ici"] or "—", p["palet"] or "—"]
            x = M + 4
            for (name, wd, al), v in zip(cols, vals):
                f = "B" if name == "Kod" else "N"
                text(c, x + (wd - 6 if al == "r" else 0), y, v, f, 7.5, INK, al); x += wd
            y -= rh
    y -= 10
    note = ("Ölçü, hacim ve koli bilgileri üretici verilerine dayanır; ± %3 tolerans içerebilir. "
            "Sipariş öncesi güncel stok ve fiyat için lütfen bizimle iletişime geçin.")
    for ln in wrap(c, note, "R", 7.5, W - 2 * M):
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
    text(c, M + 30, H / 2 - 92, "Fiyat teklifi ve numune talepleriniz için bize ulaşın.", "R", 9, MUTED)
    text(c, W / 2, 40, f"© {YEAR} {COMPANY}", "R", 7.5, white, "c")
    c.showPage()

# ---------------- derleme ----------------
def build():
    c = canvas.Canvas(OUT, pagesize=A4)
    c.setTitle(f"EUPLUS Ürün Kataloğu {YEAR}"); c.setAuthor(COMPANY); c.setSubject("Şeffaf tatlı, çikolata ve bal ambalajları")
    # sayfa numaralarını önceden hesapla: kapak(1) + giriş(1), her bölüm: ayırıcı(1) + ürün sayfaları
    toc = []; pg = 3
    for sec in sorted(SECTIONS):
        items = [p for p in PRODUCTS if p["bolum"] == sec]
        toc.append((SECTIONS[sec]["ad"], SECTIONS[sec]["en"], pg, len(items)))
        pg += 1 + math.ceil(len(items) / PER_PAGE)
    cover(c); intro(c, toc)
    highlights = {1: ["CP14", "CP41", "CP60"], 2: ["CP111", "CP165", "CP185"], 3: ["CP319", "CP320", "CP364"]}
    for num, sec in enumerate(sorted(SECTIONS), start=1):
        items = [p for p in PRODUCTS if p["bolum"] == sec]
        divider(c, num, SECTIONS[sec]["ad"], SECTIONS[sec]["en"], items, highlights[sec])
        product_pages(c, f"{num:02d}  {SECTIONS[sec]['ad']}", items)
    index_table(c); back(c)
    c.save()
    compress(OUT)
    print("yazıldı:", OUT, "—", page_no[0], "sayfa,", round(os.path.getsize(OUT) / 1e6, 1), "MB")

def compress(path):
    """Görselleri 200 dpi'a indirip JPEG'e çevirir; şeffaflık (SMask) korunur. PyMuPDF yoksa atlanır."""
    try:
        import fitz
    except ImportError:
        print("uyarı: pymupdf yok, sıkıştırma atlandı (pip install pymupdf)"); return
    doc = fitz.open(path)
    doc.rewrite_images(dpi_threshold=201, dpi_target=200, quality=82, lossy=True, lossless=True)
    logo_pdf = fitz.open("pdf", fitz.open(LOGO_SVG).convert_to_pdf())
    for pi, r in _logo_slots:
        doc[pi].show_pdf_page(fitz.Rect(*r), logo_pdf, 0)
    tmp = path + ".tmp"; doc.ez_save(tmp, garbage=4, deflate=True); doc.close(); os.replace(tmp, path)

if __name__ == "__main__":
    build()
