# -*- coding: utf-8 -*-
"""katalog/urunler.json'daki her ürünü e-ticaret için tek tek kaydeder:
urunler/<kod>-<ad>/  →  <slug>.jpg (1200×1200 beyaz) + <slug>.png + urun.json + ilan.md
ve toplu urunler/urunler.json + urunler/urunler.csv.

İki tedarikçi şeması desteklenir:
  crystal-pack : şeffaf PS/PET sunum kapları (olcu, hacim, materyal, koli, koli_ici, palet)
  promocup     : karton bardak / paket servis (agiz_capi, dip_capi, yukseklik, agirlik_g,
                 fisek_ici, koli_secenekleri[], net_kg, tedarikci_kodu, not)
Kullanım: python3 katalog/build_urunler.py   (depo kökünden)
"""
import json, os, re, csv, unicodedata
from PIL import Image

ROOT = os.path.abspath('.')
DATA = json.load(open('katalog/urunler.json', encoding='utf-8'))
SECTIONS = {int(k): v for k, v in DATA['bolumler'].items()}
P = DATA['urunler']
OUT = 'urunler'
RAW = 'https://raw.githubusercontent.com/euplus/euplus-brand-assets/main/urunler'
SUPPLIERS = {}
for d in os.listdir('kaynaklar'):
    f = os.path.join('kaynaklar', d, 'tedarikci.json')
    if os.path.exists(f): SUPPLIERS[d] = json.load(open(f, encoding='utf-8'))

TR = str.maketrans('çğıöşüÇĞİÖŞÜ', 'cgiosuCGIOSU')
def tr_lower(s):
    """Türkçe küçük harf: İ→i, I→ı (str.lower 'İ' için birleşik nokta üretir)."""
    return s.replace('İ', 'i').replace('I', 'ı').lower()
def slug(s):
    s = s.translate(TR).lower()
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s)).strip('-')

def supplier(p): return p.get('tedarikci') or SECTIONS[p['bolum']].get('tedarikci', 'crystal-pack')
def dims(s): return s.replace('x', ' × ') + ' mm' if s else '—'
def g(s): return s + ' g' if s else '—'

# ================= ürün tipi =================
def kind(p):
    a = tr_lower(p['ad'])
    if supplier(p) == 'promocup':
        if 'çanta' in a: return 'canta'
        if 'viyol' in a: return 'viyol'
        if 'tıpa' in a: return 'tipa'
        if 'holder' in a: return 'holder'
        if 'pet bardak' in a: return 'pet-bardak'
        if 'kapak' in a: return 'kapak-pc'
        if 'patates' in a: return 'patates-kutusu'
        if 'tava' in a: return 'tava'
        if 'pizza' in a: return 'pizza-kutusu'
        if 'sandviç' in a: return 'sandvic-kutusu'
        if 'oluklu' in a: return 'oluklu-kutu'
        if 'gıda kutusu' in a: return 'gida-kutusu'
        if 'salata' in a: return 'salata-kasesi'
        if 'dondurma' in a: return 'dondurma-kasesi'
        if 'çift katlı' in a: return 'cift-katli-bardak'
        if 'tek katlı' in a: return 'tek-katli-bardak'
        if 'soğuk' in a: return 'soguk-bardak'
        return 'karton'
    if 'kapak' in a: return 'kapak'
    if 'separatör' in a or 'seperatör' in a: return 'separator'
    if 'tabak' in a: return 'tabak'
    if 'kaşık' in a: return 'kasik'
    if 'kasa' in a: return 'kasa'
    if 'bardak' in a: return 'bardak'
    if 'kavanoz' in a or 'kavonoz' in a: return 'kavanoz'
    if 'şişe' in a: return 'sise'
    if 'kase' in a: return 'kase'
    return 'kutu'

def title(p):
    if supplier(p) == 'promocup': return p['ad']
    ad, hacim = p['ad'], p['hacim']
    if hacim and 'cc' not in ad.lower() and 'oz' not in ad.lower(): return f"{ad} {hacim} cc"
    return ad

# ================= Crystal Pack metinleri =================
USE_CP = {1: 'sütlü tatlı, puding, muhallebi, sütlaç, kazandibi, tiramisu ve benzeri tatlıların sunumu',
          2: 'lokum, çikolata, draje, badem şekeri, macaron ve kuruyemiş sunumu',
          3: 'süzme bal, petek bal ve krem bal sunumu'}
KIND_CP = {
 'kase': 'tek kullanımlık şeffaf tatlı kasesidir', 'kutu': 'tek kullanımlık şeffaf sunum kutusudur',
 'kavanoz': 'tek kullanımlık şeffaf kavanozdur', 'bardak': 'tek kullanımlık şeffaf sunum bardağıdır',
 'tabak': 'tek kullanımlık şeffaf sunum tabağıdır', 'kapak': 'kendi gövdesiyle uyumlu şeffaf kapaktır',
 'separator': 'kendi kabıyla uyumlu bölmeli separatördür (ayırıcı)', 'kasa': 'petek bal için tasarlanmış kasa (çerçeve) modelidir',
 'kasik': 'bal ve tatlı sunumu için tek kullanımlık kaşıktır', 'sise': 'şeker ve draje sunumu için şeffaf dekoratif şişedir'}
def mat_text_cp(mat):
    m = mat.upper()
    if 'PET' in m: return 'PET (polietilen tereftalat)'
    if 'GOLD' in m: return 'PS (polistiren), gold ve şeffaf seçenekli'
    return 'PS (polistiren)'

def aciklama_cp(p):
    k = kind(p); L = []
    L.append(f"{title(p)}, {KIND_CP[k]}. {USE_CP[p['bolum']][0].upper() + USE_CP[p['bolum']][1:]} için uygundur.")
    oz = []
    if p['olcu']: oz.append(f"ürün ölçüsü {dims(p['olcu'])}")
    if p['hacim']: oz.append(f"{p['hacim']} cc hacim")
    oz.append(f"{mat_text_cp(p['materyal'])} hammadde")
    L.append("Teknik özellikler: " + ", ".join(oz) + ".")
    L.append("Kristal berraklığındaki gövdesi ürünün içeriğini olduğu gibi gösterir; vitrinde ve raf ömrü boyunca "
             "formunu korur. Gıdayla temasa uygun hammaddeden üretilmiştir.")
    L.append("Soğuk sunum ve dolapta saklama için −10 °C'ye, sıcak dolum için +60 °C'ye kadar kullanılabilir.")
    if p['koli'] and p['koli_ici']:
        s = f"Toptan satış koli bazındadır: bir kolide {p['koli_ici']} adet, koli ölçüsü {dims(p['koli'])}"
        if p['palet']: s += f", bir euro palete {p['palet']} koli sığar"
        L.append(s + ".")
    return L

def tags_cp(p):
    k = kind(p); out = [tr_lower(title(p)), tr_lower(p['ad'])]
    if p['hacim']: out += [f"{p['hacim']} cc {k}", f"{p['hacim']}cc {k}"]
    out += {'kase': ['tatlı kasesi', 'sunum kasesi', 'plastik kase', 'şeffaf kase', 'tek kullanımlık kase'],
            'kutu': ['sunum kutusu', 'plastik kutu', 'şeffaf kutu', 'tatlı kutusu', 'tek kullanımlık kutu'],
            'kavanoz': ['plastik kavanoz', 'şeffaf kavanoz', 'pet kavanoz', 'kapaklı kavanoz'],
            'bardak': ['plastik bardak', 'şeffaf bardak', 'tatlı bardağı', 'sunum bardağı'],
            'tabak': ['plastik tabak', 'şeffaf tabak', 'sunum tabağı', 'servis tabağı'],
            'kapak': ['plastik kapak', 'şeffaf kapak', 'bombe kapak'],
            'separator': ['separatör', 'bölmeli ayırıcı', 'kutu içi ayırıcı'],
            'kasa': ['petek bal kasası', 'bal kasası', 'petek bal kabı'],
            'kasik': ['bal kaşığı', 'plastik kaşık', 'tek kullanımlık kaşık'],
            'sise': ['dekoratif şişe', 'şeker şişesi', 'plastik şişe']}[k]
    out += {1: ['sütlü tatlı kabı', 'puding kabı', 'tatlı ambalajı'], 2: ['lokum kutusu', 'çikolata kutusu', 'kuruyemiş kabı'],
            3: ['bal kabı', 'petek bal ambalajı', 'bal ambalajı']}[p['bolum']]
    if 'PET' in p['materyal'].upper(): out.append('pet ambalaj')
    out.append(tr_lower(p['kod']))
    return out

# ================= Promocup metinleri =================
KIND_PC = {
 'tek-katli-bardak': ('tek katlı karton sıcak içecek bardağıdır', 'kahve, çay, salep, sıcak çikolata ve bitki çayı servisi'),
 'cift-katli-bardak': ('çift katlı (çift cidarlı) karton sıcak içecek bardağıdır', 'filtre kahve, latte, çay ve sıcak çikolata gibi uzun süre sıcak tutulan içeceklerin servisi'),
 'soguk-bardak': ('karton soğuk içecek bardağıdır', 'soğuk içecek, gazlı içecek, milkshake, smoothie, mısır ve patates servisi'),
 'dondurma-kasesi': ('karton dondurma ve tatlı kasesidir', 'dondurma, dondurulmuş yoğurt, helva, meyve salatası ve meze servisi'),
 'salata-kasesi': ('kraft karton salata kasesidir', 'salata, poke bowl, makarna, pilav ve sıcak-soğuk yemek servisi'),
 'patates-kutusu': ('karton patates kızartması kutusudur', 'patates kızartması, soğan halkası, nugget ve atıştırmalık servisi'),
 'tava': ('açık karton servis tavasıdır (gıda tepsisi)', 'sosisli, tavuk, nugget, tatlı ve atıştırmalık servisi'),
 'gida-kutusu': ('kilitli kapaklı karton gıda kutusudur', 'hamburger, tost, sandviç ve menü servisi'),
 'oluklu-kutu': ('mikro oluklu mukavvadan üretilmiş kilitli gıda kutusudur', 'hamburger, menü, kızartma ve paket servis'),
 'pizza-kutusu': ('mikro oluklu mukavvadan üretilmiş pizza dilim kutusudur', 'dilim pizza, börek ve pide servisi'),
 'sandvic-kutusu': ('mikro oluklu mukavvadan üretilmiş sandviç kutusudur', 'baget sandviç, dürüm ve sosisli servisi'),
 'pet-bardak': ('kristal şeffaf PET soğuk içecek bardağıdır', 'bubble tea, frappe, limonata, smoothie ve soğuk kahve servisi'),
 'kapak-pc': ('bardak veya kase ile uyumlu plastik kapaktır', 'paket servis ve gel-al satışta taşıma güvenliği'),
 'viyol': ('kağıt hamurundan (pulp) üretilmiş bardak taşıyıcı viyoldür', 'birden fazla içeceğin güvenle taşınması'),
 'tipa': ('yudum kapağı ağzını kapatan PP tıpadır', 'paket servis sırasında dökülmenin önlenmesi'),
 'holder': ('karton pasta kutusu taşıyıcısıdır (holder)', 'pasta ve tatlı kutularının taşınması'),
 'canta': ('kağıt taşıma çantasıdır', 'paket servis, mağaza ve kurumsal hediye taşıması'),
 'karton': ('karton gıda ambalajıdır', 'paket servis'),
}
def materyal_pc(p):
    k = kind(p); m = p['materyal']
    if k in ('tek-katli-bardak', 'cift-katli-bardak', 'soguk-bardak', 'dondurma-kasesi'):
        return 'Gıdayla temasa uygun, içi PE (polietilen) kaplı karton; sıvı geçirmez, kokusuz'
    if k == 'salata-kasesi':
        return ('Gıdayla temasa uygun, içi PE kaplı kraft karton; soğuk ve sıcak yemeğe dayanıklı'
                + (f"; set içinde {m.split('+')[-1].strip()} kapak" if '+' in m else ''))
    if k in ('patates-kutusu', 'tava', 'gida-kutusu'):
        return 'Gıdayla temasa uygun karton; kraft veya beyaz yüzey seçeneği'
    if k in ('oluklu-kutu', 'pizza-kutusu', 'sandvic-kutusu'):
        return 'Mikro oluklu (E dalga) mukavva; ısıyı korur, buharı dengeler, ezilmeye dayanıklı'
    if k == 'pet-bardak': return 'PET (polietilen tereftalat), kristal şeffaf'
    if k == 'kapak-pc':
        return {'PS': 'PS (polistiren); siyah ve beyaz renk seçeneği', 'PP': 'PP (polipropilen); hafif buzlu görünüm, ısıya dayanıklı',
                'PET': 'PET (polietilen tereftalat); kristal şeffaf görünüm'}.get(m, m)
    if k == 'viyol': return 'Geri dönüştürülmüş kağıt hamuru (pulp); gri'
    if k == 'tipa': return 'PP (polipropilen); siyah ve beyaz'
    if k == 'canta': return m + '; burgu veya düz sap, SOS (yassı dipli) seçeneği'
    return m or 'Karton'

def aciklama_pc(p):
    k = kind(p); L = []
    what, use = KIND_PC[k]
    L.append(f"{title(p)}, {what}. {use[0].upper() + use[1:]} için uygundur.")
    oz = []
    if p.get('agiz_capi') and p.get('dip_capi'):
        oz.append(f"ağız çapı {p['agiz_capi']} mm, dip çapı {p['dip_capi']} mm, yükseklik {p['yukseklik']} mm")
    elif p.get('agiz_capi'): oz.append(f"çap {p['agiz_capi']} mm")
    elif p['olcu']: oz.append(f"ürün ölçüsü {dims(p['olcu'])}")
    if p['hacim']: oz.append(('hacim ' + p['hacim']) if 'oz' in p['hacim'] else f"{p['hacim']} cc hacim")
    if p.get('agirlik_g'): oz.append(f"ürün ağırlığı {p['agirlik_g']} g")
    L.append("Teknik özellikler: " + (", ".join(oz) if oz else "ölçü ve ağırlık siparişe göre belirlenir") + ".")
    L.append(materyal_pc(p) + ". Gıdayla temasa uygun hammaddeden üretilmiştir.")
    if k in ('tek-katli-bardak', 'cift-katli-bardak'):
        L.append("Ofset, flekso veya dijital baskı ile markanıza özel baskılı; baskısız beyaz veya kraft olarak da sunulur. "
                 "Sıcak içecek için tasarlanmıştır" + ("; çift cidar yapısı kılıf (sleeve) gerektirmez." if k == 'cift-katli-bardak' else "; PS yudum kapakları ile uyumludur."))
    elif k in ('soguk-bardak', 'dondurma-kasesi', 'salata-kasesi', 'pet-bardak'):
        L.append("Ofset, flekso veya dijital baskı ile markanıza özel baskı yapılabilir; baskısız olarak da sunulur. "
                 "Uyumlu kapaklarla paket servis için güvenle kullanılır.")
    elif k in ('patates-kutusu', 'tava', 'gida-kutusu', 'oluklu-kutu', 'pizza-kutusu', 'sandvic-kutusu'):
        L.append("Baskılı veya baskısız, kraft ya da beyaz karton seçeneğiyle üretilir; markanıza özel baskı (ofset / flekso / dijital) yapılabilir. "
                 "Düz sevk edilir, kullanım anında katlanır. Farklı ölçüler için bizimle iletişime geçin.")
    elif k == 'kapak-pc':
        L.append((p.get('not') or 'Uyumlu bardak ve kaselerle kullanılır') + ". Sıkı oturur, taşıma sırasında dökülmeyi önler.")
    elif k == 'canta':
        L.append("Ölçü, kağıt ve sap tipi siparişe göre belirlenir: körük 9–26 cm, genişlik 22–55 cm, yükseklik 20–62 cm. "
                 "Ofset veya flekso baskı ile markanıza özel üretilir.")
    else:
        L.append((p.get('not') or 'Paket servis ve gel-al satış için pratik çözüm') + ".")
    # koli
    ks = p.get('koli_secenekleri') or []
    if k == 'canta':
        L.append("Toptan satış siparişe özel üretimdir: minimum sipariş 25.000 adettir.")
    elif ks and ks[0]['koli_ici']:
        o = ks[0]
        s = f"Toptan satış koli bazındadır: bir kolide {o['koli_ici']} adet"
        if p.get('fisek_ici'): s += f" ({p['fisek_ici']} adetlik fişekler hâlinde)"
        if o['koli']: s += f", koli ölçüsü {dims(o['koli'])}"
        if o['net_kg']: s += f", koli net ağırlığı {o['net_kg']} kg"
        if len(ks) > 1:
            s += ". Alternatif koli: " + "; ".join(f"{x['koli_ici']} adet, {dims(x['koli'])}" + (f", {x['net_kg']} kg" if x['net_kg'] else '') for x in ks[1:])
        L.append(s + ".")
    return L

def tags_pc(p):
    k = kind(p); a = tr_lower(p['ad']); out = [a]
    hac = p['hacim']
    base = {
     'tek-katli-bardak': ['karton bardak', 'kağıt bardak', 'tek katlı karton bardak', 'sıcak içecek bardağı', 'kahve bardağı', 'çay bardağı', 'baskılı karton bardak', 'tek kullanımlık bardak'],
     'cift-katli-bardak': ['çift katlı karton bardak', 'double wall bardak', 'kılıfsız karton bardak', 'kahve bardağı', 'sıcak içecek bardağı', 'baskılı karton bardak', 'karton bardak'],
     'soguk-bardak': ['soğuk içecek bardağı', 'karton soğuk bardak', 'milkshake bardağı', 'kola bardağı', 'mısır bardağı', 'karton bardak', 'baskılı karton bardak'],
     'dondurma-kasesi': ['dondurma kasesi', 'karton dondurma kabı', 'dondurma bardağı', 'tatlı kasesi', 'karton kase', 'baskılı dondurma kasesi'],
     'salata-kasesi': ['salata kasesi', 'kraft salata kabı', 'karton salata kasesi', 'poke bowl kabı', 'kraft kase', 'paket servis kabı', 'kapaklı salata kasesi'],
     'patates-kutusu': ['patates kutusu', 'patates kızartması kutusu', 'karton patates kabı', 'fast food kutusu', 'kraft patates kutusu'],
     'tava': ['karton tava', 'gıda tavası', 'karton servis tepsisi', 'sosisli kabı', 'tavuk kabı', 'kraft tava'],
     'gida-kutusu': ['hamburger kutusu', 'karton gıda kutusu', 'menü kutusu', 'kilitli karton kutu', 'kraft hamburger kutusu', 'fast food kutusu'],
     'oluklu-kutu': ['oluklu hamburger kutusu', 'oluklu gıda kutusu', 'mikro oluklu kutu', 'menü kutusu', 'kraft kutu', 'paket servis kutusu'],
     'pizza-kutusu': ['pizza dilim kutusu', 'üçgen pizza kutusu', 'oluklu pizza kutusu', 'dilim pizza kabı', 'kraft pizza kutusu'],
     'sandvic-kutusu': ['sandviç kutusu', 'baget kutusu', 'oluklu sandviç kutusu', 'dürüm kutusu', 'sosisli kutusu', 'kraft kutu'],
     'pet-bardak': ['pet bardak', 'şeffaf bardak', 'bubble tea bardağı', 'plastik bardak', 'soğuk içecek bardağı', '95 mm pet bardak', 'kapaklı pet bardak'],
     'kapak-pc': ['bardak kapağı', 'plastik kapak', 'yudum kapağı' if 'yudum' in a or 'ps' in a else 'şeffaf kapak', 'karton bardak kapağı', 'kahve bardağı kapağı' if 'ps' in a else 'kase kapağı'],
     'viyol': ['bardak taşıyıcı', 'viyol', 'bardak viyolü', 'kahve taşıma viyolü', 'cup holder', 'karton bardak taşıyıcı'],
     'tipa': ['kapak tıpası', 'bardak kapağı tıpası', 'kahve kapağı tıpası', 'plastik tıpa', 'yudum kapağı tıpası'],
     'holder': ['pasta kutusu holder', 'pasta taşıyıcı', 'karton holder', 'kutu taşıyıcı'],
     'canta': ['kağıt çanta', 'kraft çanta', 'karton çanta', 'baskılı kağıt çanta', 'paket servis çantası', 'saplı kağıt çanta', 'burgu saplı çanta' if 'burgu' in a else 'düz saplı çanta'],
     'karton': ['karton ambalaj'],
    }[k]
    out += base
    if hac and 'oz' in hac: out += [f"{hac} bardak", f"{hac.replace(' ', '')} karton bardak"]
    elif hac: out += [f"{hac} cc {('salata kasesi' if k == 'salata-kasesi' else 'dondurma kasesi' if k == 'dondurma-kasesi' else 'bardak')}"]
    out += ['paket servis ambalajı', 'karton ambalaj' if k not in ('pet-bardak', 'kapak-pc', 'tipa') else 'plastik ambalaj', 'toptan ambalaj']
    out.append(tr_lower(p['kod']))
    return out

def dedupe(ts, n=14):
    seen = set(); res = []
    for t in ts:
        t = t.strip()
        if t and t not in seen: seen.add(t); res.append(t)
    return res[:n]

def aciklama(p): return aciklama_pc(p) if supplier(p) == 'promocup' else aciklama_cp(p)
def tags(p): return dedupe(tags_pc(p) if supplier(p) == 'promocup' else tags_cp(p))

# ================= görseller =================
def white_square(im, size=1200, pad=0.06):
    im = im.convert('RGBA')
    bg = Image.new('RGB', (size, size), 'white')
    m = int(size * pad); box = size - 2 * m
    r = min(box / im.width, box / im.height)
    im2 = im.resize((max(1, int(im.width * r)), max(1, int(im.height * r))), Image.LANCZOS)
    bg.paste(im2, ((size - im2.width) // 2, (size - im2.height) // 2), im2)
    return bg

# ================= üretim =================
rows = []
for p in P:
    sup = supplier(p); sec = SECTIONS[p['bolum']]
    sl = f"{slug(p['kod'])}-{slug(p['ad'])}"
    d = os.path.join(OUT, sl); os.makedirs(d, exist_ok=True)
    src = Image.open(os.path.join('katalog', p['gorsel']))
    transparent = src.mode in ('RGBA', 'LA') or (src.mode == 'P' and 'transparency' in src.info)
    white_square(src).save(os.path.join(d, sl + '.jpg'), quality=92, optimize=True, subsampling=0)
    png = src.convert('RGBA') if transparent else src.convert('RGB')
    png.thumbnail((1600, 1600), Image.LANCZOS); png.save(os.path.join(d, sl + '.png'), optimize=True)
    shared = sec.get('gorsel') == p['gorsel']
    ac = aciklama(p); tg = tags(p)
    ks = p.get('koli_secenekleri') or []
    rec = {
        'stok_kodu': p['kod'], 'baslik': title(p), 'urun_adi': p['ad'],
        'kategori': sec['ad'], 'kategori_en': sec['en'], 'katalog': sec.get('katalog', 'seffaf'), 'tur': kind(p),
        'olcu_mm': p['olcu'], 'hacim_cc': p['hacim'] if p['hacim'] and 'oz' not in p['hacim'] else '',
        'hacim': p['hacim'], 'materyal': p['materyal'],
        'agiz_capi_mm': p.get('agiz_capi', ''), 'dip_capi_mm': p.get('dip_capi', ''), 'yukseklik_mm': p.get('yukseklik', ''),
        'agirlik_g': p.get('agirlik_g', ''), 'fisek_ici_adet': p.get('fisek_ici', ''),
        'koli_olcusu_mm': p['koli'], 'koli_ici_adet': p['koli_ici'], 'koli_net_kg': p.get('net_kg', ''), 'palet_koli': p['palet'],
        'koli_secenekleri': ks,
        'min_siparis': ('25.000 adet (siparişe özel üretim)' if kind(p) == 'canta' else (p['koli_ici'] + ' adet (1 koli)') if p['koli_ici'] else 'Bizimle iletişime geçin'),
        'not': p.get('not', ''),
        'aciklama': ac, 'aciklama_html': '<p>' + '</p>\n<p>'.join(ac) + '</p>',
        'etiketler': tg, 'marka': 'EUPLUS',
        'gorseller': {'jpg': f"{RAW}/{sl}/{sl}.jpg", 'png': f"{RAW}/{sl}/{sl}.png", 'png_seffaf': transparent,
                      'not': 'Kategori tanıtım fotoğrafı; ürüne özel fotoğraf yok' if shared else ''},
        'kaynak': {'tedarikci': sup, 'tedarikci_ad': SUPPLIERS.get(sup, {}).get('ad', sup),
                   'tedarikci_kodu': p.get('tedarikci_kodu') or (p['kod'] if sup == 'crystal-pack' else ''),
                   'katalog': f"kaynaklar/{sup}/" + (SUPPLIERS.get(sup, {}).get('kataloglar') or [{'dosya': ''}])[0]['dosya']},
    }
    json.dump(rec, open(os.path.join(d, 'urun.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(d, 'ilan.md'), 'w', encoding='utf-8') as f:
        f.write(f"# {rec['baslik']}\n\n**Stok kodu:** {p['kod']}  ·  **Kategori:** {rec['kategori']}  ·  **Marka:** EUPLUS\n\n")
        f.write('\n\n'.join(ac) + '\n\n')
        f.write('| Özellik | Değer |\n|---|---|\n')
        if sup == 'promocup':
            tbl = []
            if p.get('agiz_capi'): tbl.append(('Ağız çapı', p['agiz_capi'] + ' mm'))
            if p.get('dip_capi'): tbl.append(('Dip çapı', p['dip_capi'] + ' mm'))
            if p.get('yukseklik'): tbl.append(('Yükseklik', p['yukseklik'] + ' mm'))
            if p['olcu'] and not p.get('agiz_capi'): tbl.append(('Ürün ölçüsü', dims(p['olcu'])))
            if p['hacim']: tbl.append(('Hacim', p['hacim'] if 'oz' in p['hacim'] else p['hacim'] + ' cc'))
            tbl.append(('Materyal', p['materyal'] or '—'))
            if p.get('agirlik_g'): tbl.append(('Ürün ağırlığı', g(p['agirlik_g'])))
            if p.get('fisek_ici'): tbl.append(('Fişek içi adet', p['fisek_ici']))
            for i, o in enumerate(ks):
                suf = '' if i == 0 else f' (alternatif {i})'
                if o['koli_ici']: tbl.append(('Koli içi adet' + suf, o['koli_ici']))
                if o['koli']: tbl.append(('Koli ölçüsü' + suf, dims(o['koli'])))
                if o['net_kg']: tbl.append(('Koli net ağırlık' + suf, o['net_kg'] + ' kg'))
            if kind(p) == 'canta': tbl.append(('Minimum sipariş', '25.000 adet'))
            if p.get('not'): tbl.append(('Not', p['not']))
        else:
            tbl = [('Ürün ölçüsü', dims(p['olcu'])), ('Hacim', (p['hacim'] + ' cc') if p['hacim'] else '—'), ('Materyal', p['materyal'] or '—'),
                   ('Koli ölçüsü', dims(p['koli'])), ('Koli içi adet', p['koli_ici'] or '—'), ('Euro palet', (p['palet'] + ' koli') if p['palet'] else '—')]
        for k_, v_ in tbl: f.write(f"| {k_} | {v_} |\n")
        f.write('\n**Etiketler:** ' + ', '.join(f'`{t}`' for t in tg) + '\n\n')
        f.write(f"**Görseller:** [JPG (1200×1200, beyaz zemin)]({sl}.jpg) · [PNG ({'şeffaf' if transparent else 'opak, kategori fotoğrafı'})]({sl}.png)\n")
    rows.append((p, sl, rec))

json.dump([r[2] for r in rows], open(os.path.join(OUT, 'urunler.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
with open(os.path.join(OUT, 'urunler.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['Stok Kodu', 'Ürün Adı', 'Kategori', 'Marka', 'Açıklama', 'Ürün Ölçüsü (mm)', 'Hacim', 'Materyal',
                'Ağız Çapı (mm)', 'Dip Çapı (mm)', 'Yükseklik (mm)', 'Ürün Ağırlığı (g)', 'Fişek İçi Adet',
                'Koli Ölçüsü (mm)', 'Koli İçi Adet', 'Koli Net Ağırlık (kg)', 'Euro Palet (koli)', 'Min. Sipariş',
                'Etiketler', 'Görsel URL (JPG)', 'Görsel URL (PNG)'])
    for p, sl, rec in rows:
        w.writerow([rec['stok_kodu'], rec['baslik'], rec['kategori'], 'EUPLUS', ' '.join(rec['aciklama']),
                    p['olcu'], (p['hacim'] if 'oz' in p['hacim'] else (p['hacim'] + ' cc' if p['hacim'] else '')), p['materyal'],
                    rec['agiz_capi_mm'], rec['dip_capi_mm'], rec['yukseklik_mm'], rec['agirlik_g'], rec['fisek_ici_adet'],
                    p['koli'], p['koli_ici'], rec['koli_net_kg'], p['palet'], rec['min_siparis'],
                    ', '.join(rec['etiketler']), rec['gorseller']['jpg'], rec['gorseller']['png']])
from collections import Counter
print('ürün klasörü:', len(rows), dict(Counter(supplier(p) for p, _, _ in rows)))
