# -*- coding: utf-8 -*-
"""katalog/urunler.json'daki her ürünü e-ticaret için tek tek kaydeder:
urunler/<kod>-<ad>/  →  <slug>.jpg (1200×1200 beyaz) + <slug>.png + urun.json + ilan.md
ve toplu urunler/urunler.json + urunler/urunler.csv.

Tedarikçi şemaları:
  crystal-pack : şeffaf PS/PET sunum kapları (olcu, hacim, materyal, koli, koli_ici, palet)
  promocup     : karton bardak / paket servis (agiz_capi, dip_capi, yukseklik, agirlik_g,
                 fisek_ici, koli_secenekleri[], net_kg, tedarikci_kodu, not)
  helmex       : fast food (varyantlar[], gsm, moq)
  bukap        : gıda ambalajları (crystal-pack alanları + alt_grup, agirlik_g, tedarikci_kodu, kaynak_sayfa, not)
Kullanım: python3 katalog/build_urunler.py   (depo kökünden)
"""
import json, os, re, csv, unicodedata
from PIL import Image, ImageFilter

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
    if supplier(p) == 'helmex': return kind_hx(a)
    if supplier(p) == 'bukap': return kind_bk(p)[0]
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
    if supplier(p) in ('promocup', 'helmex', 'bukap'): return p['ad']
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
    out.append(p['kod'].lower())
    return out

# ================= Helmex (fast food) metinleri =================
def kind_hx(a):
    for key, k in [('tepsi kağıdı', 'tepsi-kagidi'), ('ambalaj kağıdı', 'ambalaj-kagidi'), ('burger kutusu', 'burger-kutusu'), ('patates', 'patates-kabi'),
                   ('taşıma kutusu', 'tasima-kutusu'), ('tepsi', 'tepsi'), ('tavuk', 'tavuk-kutusu'), ('aile kovası', 'tavuk-kutusu'), ('dürüm', 'durum-kutusu'),
                   ('pizza', 'pizza-kutusu'), ('pasta', 'pasta-kutusu'), ('noodle', 'noodle-kutusu'), ('karton kova', 'kova'), ('karton kase', 'kase-hx'),
                   ('içecek bardağı', 'bardak-hx'), ('kılıf', 'kilif'), ('taşıyıcı', 'tasiyici'), ('lüks çanta', 'luks-canta'), ('çanta', 'canta-hx'),
                   ('torba', 'torba'), ('streç', 'strec'), ('sos kabı', 'sos-kabi'), ('ıslak mendil', 'islak-mendil'), ('peçete', 'pecete'), ('havlu', 'pecete'),
                   ('tuvalet', 'pecete'), ('filtre', 'filtre'), ('ahşap', 'catal-bicak')]:
        if key in a: return k
    return 'karton'
KIND_HX = {
 'burger-kutusu': ('kilitli kapaklı karton burger kutusudur', 'hamburger, tost ve sandviç servisi', ['hamburger kutusu', 'burger kutusu', 'karton hamburger kutusu', 'kraft burger kutusu', 'kilitli karton kutu', 'fast food kutusu']),
 'patates-kabi': ('açık ağızlı karton patates kabıdır', 'patates kızartması, soğan halkası ve atıştırmalık servisi', ['patates kabı', 'patates kutusu', 'karton patates kabı', 'kızartma kabı', 'fast food kabı']),
 'oluklu-kutu': ('N dalga mikro oluklu mukavvadan burger kutusudur', 'hamburger ve menü servisi', ['oluklu burger kutusu', 'mikro oluklu kutu', 'oluklu hamburger kutusu', 'menü kutusu', 'kraft kutu']),
 'tasima-kutusu': ('kilitli kapaklı karton taşıma kutusudur', 'sıcak ve soğuk yemek, salata ve makarna servisi', ['taşıma kutusu', 'takeaway kutusu', 'karton yemek kutusu', 'paket servis kutusu', 'kilitli yemek kutusu']),
 'tepsi': ('açık karton servis tepsisidir', 'patates, tavuk, sosisli ve atıştırmalık servisi', ['karton tepsi', 'sokak lezzeti tepsisi', 'servis tepsisi', 'kraft tepsi', 'açık servis kabı']),
 'tavuk-kutusu': ('kızarmış tavuk için kilitli karton kutudur', 'kızarmış tavuk, kanat ve nugget servisi', ['tavuk kutusu', 'kızarmış tavuk kutusu', 'karton tavuk kutusu', 'aile kovası', 'fast food kutusu']),
 'durum-kutusu': ('yastık tipi karton dürüm kutusudur', 'dürüm, wrap ve sandviç servisi', ['dürüm kutusu', 'wrap kutusu', 'yastık kutu', 'karton dürüm kabı', 'sandviç kutusu']),
 'pizza-kutusu': ('oluklu mukavva pizza kutusudur', 'pizza, pide ve lahmacun servisi', ['pizza kutusu', 'oluklu pizza kutusu', 'karton pizza kutusu', 'kraft pizza kutusu', 'baskılı pizza kutusu']),
 'pasta-kutusu': ('bristol karton pasta kutusudur', 'pasta, tatlı, donut ve kurabiye servisi', ['pasta kutusu', 'karton pasta kutusu', 'tatlı kutusu', 'donut kutusu', 'kapaklı pasta kutusu']),
 'noodle-kutusu': ('PE laminasyonlu yuvarlak karton noodle kutusudur', 'noodle, makarna ve sıcak yemek servisi', ['noodle kutusu', 'yuvarlak noodle kabı', 'karton makarna kutusu', 'paket servis kabı', 'sıcak yemek kabı']),
 'kova': ('PE kaplı bristol karton kovadır', 'kızarmış tavuk ve aile menüsü servisi', ['karton kova', 'tavuk kovası', 'aile menüsü kovası', 'kağıt kova', 'fast food kovası']),
 'kase-hx': ('karton salata kasesidir', 'salata, poke ve sıcak yemek servisi', ['karton kase', 'salata kasesi', 'kraft kase', 'poke kasesi', 'paket servis kasesi']),
 'bardak-hx': ('PE kaplı karton içecek bardağıdır', 'kahve, çay ve soğuk içecek servisi', ['karton bardak', 'kağıt bardak', 'kahve bardağı', 'soğuk içecek bardağı', 'baskılı karton bardak']),
 'kilif': ('oluklu karton bardak kılıfıdır', 'sıcak içecek bardaklarının el yakmadan tutulması', ['bardak kılıfı', 'karton sleeve', 'bardak tutacağı', 'kahve bardağı kılıfı']),
 'tasiyici': ('geri dönüştürülmüş kağıt hamurundan bardak taşıyıcıdır', 'birden fazla içeceğin güvenle taşınması', ['bardak taşıyıcı', 'viyol', 'cup holder', 'kahve taşıma viyolü']),
 'luks-canta': ('ip saplı lüks kağıt çantadır', 'mağaza, butik ve kurumsal hediye taşıması', ['lüks çanta', 'ip saplı çanta', 'karton çanta', 'butik çantası', 'ofset baskılı çanta']),
 'canta-hx': ('saplı kağıt taşıma çantasıdır', 'paket servis ve mağaza taşıması', ['kağıt çanta', 'kraft çanta', 'saplı kağıt çanta', 'paket servis çantası', 'baskılı kağıt çanta']),
 'torba': ('kağıt torbadır', 'sandviç, börek, hamburger ve fırın ürünü servisi', ['kağıt torba', 'yağlı kağıt torba', 'sandviç torbası', 'kraft torba', 'hamburger poşeti']),
 'ambalaj-kagidi': ('yağ geçirmez ambalaj kağıdıdır', 'hamburger, sandviç ve dürüm sarma', ['ambalaj kağıdı', 'hamburger sargı kağıdı', 'yağlı kağıt', 'sandviç kağıdı', 'baskılı ambalaj kağıdı']),
 'tepsi-kagidi': ('tepsi altı servis kağıdıdır', 'fast food tepsilerinde sunum', ['tepsi kağıdı', 'tepsi altı kağıdı', 'servis kağıdı', 'baskılı tepsi kağıdı']),
 'strec': ('palet sarma streç filmidir', 'palet ve koli sabitleme', ['streç film', 'palet streci', 'makine streç', 'el streci', 'ambalaj filmi']),
 'sos-kabi': ('menteşeli kapaklı şeffaf PP sos kabıdır', 'sos, ketçap ve mayonez servisi', ['sos kabı', 'menteşeli sos kabı', 'ketçap kabı', 'plastik sos kabı', 'tek kullanımlık sos kabı']),
 'islak-mendil': ('tek tek paketli ıslak mendildir', 'restoran ve paket servis ikramı', ['ıslak mendil', 'restoran ıslak mendili', 'baskılı ıslak mendil', 'tekli ıslak mendil']),
 'pecete': ('%100 selüloz kağıt üründür', 'restoran, kafe ve paket servis', ['peçete', 'kağıt havlu', 'dispenser peçete', 'selüloz peçete', 'restoran peçetesi']),
 'filtre': ('basınçlı fritöz filtre kağıdıdır', 'fritöz yağının süzülmesi', ['fritöz filtresi', 'henny penny filtre', 'filtre kağıdı', 'yağ filtresi']),
 'catal-bicak': ('huş ağacından tek kullanımlık çatal-bıçak ürünüdür', 'paket servis ve ikram', ['ahşap çatal', 'ahşap kaşık', 'ahşap bıçak', 'tek kullanımlık çatal bıçak', 'çatal bıçak seti']),
 'karton': ('karton gıda ambalajıdır', 'paket servis', ['karton ambalaj']),
}
def vlabel(v):
    if v.get('inc'): return v['inc']
    if v.get('olcu'): return v['olcu']
    if v.get('en') and v.get('boy'): return f"{v['en']}×{v['boy']}" + (f"×{v['koruk']}" if v.get('koruk') else '')
    if v.get('mikron'): return f"{v['mikron']} µ"
    return v.get('ad', '')
def aciklama_hx(p):
    k = kind(p); what, use, _ = KIND_HX[k]; sec = SECTIONS[p['bolum']]; L = []
    L.append(f"{title(p)}, {what}. {use[0].upper() + use[1:]} için uygundur.")
    oz = []
    if p.get('olcu'): oz.append(f"ölçü {p['olcu'].replace('x', ' × ')}" + ('' if any(u in p['olcu'] for u in ('cm', 'mm', 'µ', 'ml', 'lt')) else ' mm'))
    if p.get('hacim'): oz.append(f"hacim {p['hacim']}" + ('' if any(u in str(p['hacim']) for u in ('ml', 'lt', 'oz')) else ' cc'))
    if p.get('materyal'): oz.append(f"{p['materyal']} hammadde")
    if p.get('gsm') and p['gsm'] not in (p.get('materyal') or ''): oz.append(f"{p['gsm']}")
    if p.get('agirlik_g'): oz.append(f"ürün ağırlığı {p['agirlik_g']} g")
    L.append("Teknik özellikler: " + (", ".join(oz) if oz else "ölçü ve kalite siparişe göre belirlenir") + ".")
    grp = sec.get('grup', 1)
    if grp == 1: L.append("Gıdayla temasa uygun karton; beyaz, kraft veya siyah yüzey seçeneği. Flekso, ofset ya da dijital baskı ile markanıza özel tasarım yapılır; standart ölçüler dışında talebe göre özel ölçü üretilir, tasarım ve numune 1–2 haftada hazırlanır.")
    elif grp == 2: L.append("Gıdayla temasa uygun kağıt; beyaz veya kahve. Flekso ya da ofset baskı ile markanıza özel üretilir; standart ölçüler dışındaki talepler için özel üretim yapılır.")
    else: L.append((sec.get('notlar') or ["Markanıza özel baskı ve etiket seçeneği için bizimle iletişime geçin"])[0].rstrip('.') + ".")
    vs = p.get('varyantlar') or []
    if vs: L.append(f"{len(vs)} standart ölçü / seçenek: " + ", ".join(vlabel(v) for v in vs) + ".")
    if p.get('koli_ici'):
        s = f"Toptan satış koli bazındadır: bir kolide {p['koli_ici']} adet"
        if p.get('koli'): s += f", koli ölçüsü {p['koli'].replace('x', ' × ')} mm"
        if p.get('palet'): s += f", bir palete {p['palet']} koli"
        L.append(s + ".")
    elif p.get('moq'): L.append("Siparişe özel üretimdir; minimum sipariş " + (p['moq'] if 'adet' in p['moq'] else p['moq'] + ' adet') + ".")
    else: L.append("Sipariş adedi, koli düzeni ve teslimat için bizimle iletişime geçin.")
    return L
def tags_hx(p):
    k = kind(p); out = [tr_lower(p['ad'])] + KIND_HX[k][2]
    out += ['fast food ambalajı', 'paket servis ambalajı', 'restoran ambalajı', 'toptan ambalaj', p['kod'].lower()]
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
    out.append(p['kod'].lower())
    return out

# ================= Bukap (gıda ambalajları) metinleri =================
KIND_BK = [  # (ad içinde aranan regex, tür, ne olduğu, etiketler) — sıra önemli
 ('set', 'set', 'tek kullanımlık hazır yemek setidir', ['çatal bıçak seti', 'hazır yemek seti', 'paket servis seti', 'plastik çatal kaşık seti', 'peçeteli set']),
 ('karıştırıcı', 'karistirici', 'tek kullanımlık içecek karıştırıcısıdır', ['karıştırıcı', 'kahve karıştırıcı', 'plastik karıştırıcı', 'çay karıştırıcı']),
 ('dondurma kaşığı', 'dondurma-kasigi', 'tek kullanımlık dondurma kaşığıdır', ['dondurma kaşığı', 'plastik dondurma kaşığı', 'tatlı kaşığı', 'renkli kaşık']),
 ('çatal', 'catal', 'tek kullanımlık plastik çataldır', ['plastik çatal', 'tek kullanımlık çatal', 'paket servis çatalı', 'catering çatal']),
 ('kaşık', 'kasik', 'tek kullanımlık plastik kaşıktır', ['plastik kaşık', 'tek kullanımlık kaşık', 'paket servis kaşığı', 'catering kaşık']),
 ('bıçak', 'bicak', 'tek kullanımlık plastik bıçaktır', ['plastik bıçak', 'tek kullanımlık bıçak', 'paket servis bıçağı', 'catering bıçak']),
 (r'\bkapağı\b', 'kapak', 'uyumlu gövdesine sıkı oturan kapaktır', ['plastik kapak', 'bardak kapağı', 'kase kapağı', 'yedek kapak']),
 ('şişe', 'sise', 'kapaklı PET şişedir', ['pet şişe', 'plastik şişe', 'meyve suyu şişesi', 'ayran şişesi', 'boş pet şişe']),
 ('viyol bardak', 'viyol', 'kağıt hamurundan bardak taşıyıcı viyoldür', ['bardak taşıyıcı', 'viyol', 'kahve taşıma viyolü', 'cup holder']),
 ('yumurta', 'yumurta', 'şeffaf PET yumurta viyolüdür', ['yumurta viyolü', 'plastik yumurta kabı', 'şeffaf yumurta kutusu', 'yumurta ambalajı']),
 ('çanta', 'canta', 'saplı kraft kağıt çantadır', ['kraft çanta', 'kağıt çanta', 'saplı kağıt çanta', 'paket servis çantası']),
 ('poşet', 'poset', 'şeffaf OPP poşettir', ['opp poşet', 'şeffaf poşet', 'körüklü poşet', 'kurabiye poşeti', 'şekerleme poşeti']),
 ('tabak', 'tabak', 'tek kullanımlık plastik tabaktır', ['plastik tabak', 'tek kullanımlık tabak', 'servis tabağı', 'parti tabağı']),
 (r'\bsos\b', 'sos', 'porsiyonluk sos kabıdır', ['sos kabı', 'kapaklı sos kabı', 'ketçap kabı', 'porsiyon kabı', 'plastik sos kabı']),
 ('salata', 'salata', 'kapaklı salata kabıdır', ['salata kabı', 'kapaklı salata kabı', 'şeffaf salata kasesi', 'paket servis salata kabı']),
 (r'\bbarda[kğ]', 'bardak', 'tek kullanımlık bardaktır', ['tek kullanımlık bardak', 'içecek bardağı', 'servis bardağı']),
 ('alüminyum', 'aluminyum', 'alüminyum folyo kaptır', ['alüminyum kap', 'folyo kap', 'alüminyum tepsi', 'fırın kabı', 'paket servis kabı']),
 ('kapama', 'kapama', 'üst film kapama (top seal) makinesine uygun kaptır', ['üst film kapama kabı', 'top seal kap', 'kapama tepsisi', 'vakumlu ambalaj', 'hazır yemek kabı']),
 ('kase', 'kase', 'tek kullanımlık kasedir', ['plastik kase', 'tek kullanımlık kase', 'kapaklı kase', 'servis kasesi']),
 ('kutu', 'kutu', 'şeffaf sunum kutusudur', ['şeffaf kutu', 'plastik kutu', 'sunum kutusu', 'hediye kutusu']),
 ('sızdırmaz', 'kap', 'sızdırmaz kapaklı şeffaf gıda kabıdır', ['sızdırmaz kap', 'kapaklı plastik kap', 'şeffaf saklama kabı', 'menteşeli kap', 'paket servis kabı']),
 ('kurabiye', 'kap', 'kapaklı şeffaf kurabiye kabıdır', ['kurabiye kabı', 'kurabiye kutusu', 'şeffaf kurabiye kabı', 'pastane ambalajı', 'menteşeli kap']),
 ('pasta|kek|baklava|kazandibi', 'kap', 'kapaklı tatlı ve pasta sunum kabıdır', ['pasta kabı', 'tatlı kabı', 'kek kabı', 'pastane ambalajı', 'kapaklı sunum kabı']),
 ('dondurma|küvet', 'kap', 'dondurma kabıdır', ['dondurma kabı', 'dondurma kutusu', 'dondurma ambalajı', 'kapaklı dondurma kabı']),
 ('peynir|sushi|meze|kahvaltı|kebap|tavuk|yemek|hamburger|sandviç', 'kap', 'kapaklı yemek ve sunum kabıdır', ['yemek kabı', 'paket servis kabı', 'kapaklı yemek kabı', 'take away kap', 'mikrodalga kabı']),
 ('', 'kap', 'tek kullanımlık gıda kabıdır', ['plastik kap', 'tek kullanımlık kap', 'gıda kabı', 'saklama kabı']),
]
USE_BK = {  # alt grup → kullanım alanı
 'Paketleme Kapları': 'şekerleme, kuruyemiş, lokum, kurabiye ve hediyelik ürünlerin sunumu', 'Pasta ve Kek Kapları': 'pasta, kek, cheesecake, baklava ve tatlı sunumu',
 'Kurabiye Kapları': 'kurabiye, bisküvi, pasta ve tatlı satışı', 'Makaron Kapları': 'makaron, çikolata ve bonbon sunumu',
 'Dondurma Kapları': 'dondurma, sorbe ve soğuk tatlı servisi', 'Sızdırmaz Kaplar': 'tatlı, salata, meze, zeytin ve sulu gıdaların sızdırmadan taşınması',
 'Soğuk İçecek Bardakları': 'soğuk kahve, limonata, smoothie, milkshake ve meyve kokteyli servisi', 'Plastik Şişeler': 'ayran, meyve suyu, limonata ve soğuk içecek dolumu',
 'Karton Bardaklar': 'kahve, çay ve sıcak içecek servisi', 'Viyoller': 'birden fazla içeceğin güvenle taşınması', 'Kraft Çantalar': 'paket servis ve gel-al siparişlerinin taşınması',
 'Mikrodalga Yemek Kapları': 'sıcak yemek, pilav ve ana yemeğin paket servisi', 'Tavuk Kapları': 'döner tavuk, kızarmış tavuk ve et yemeklerinin paket servisi',
 'Çok Amaçlı Kaplar': 'meze, kahvaltılık, salata ve atıştırmalık sunumu', 'Kahvaltı ve Bölmeli Kaplar': 'kahvaltı tabağı, meze ve bölmeli yemek servisi',
 'Meze Kapları': 'meze, salata ve soğuk başlangıç sunumu', 'Sandviç Kapları': 'üçgen sandviç ve tost sunumu', 'Çorba Kaseleri': 'çorba ve sıcak sulu yemeklerin paket servisi',
 'Sos Kapları': 'ketçap, mayonez, sos, reçel ve bal porsiyonu', 'Salata Kapları': 'salata, makarna, meyve ve soğuk yemek servisi', 'Kraft Kaseler': 'salata, poke bowl, makarna ve sıcak yemek servisi',
 'Alüminyum Kaplar': 'fırın yemekleri, künefe, sütlaç ve sıcak yemeklerin pişirilmesi ve paket servisi',
 'Üst Film Kapama Yemek Kapları': 'hazır yemek, catering ve tabldot servisi', 'Üst Film Kapama Et Kapları': 'kırmızı et, tavuk ve şarküteri ürünlerinin paketlenmesi',
 'PP Köşeli Kaseler': 'tatlı, salata, börek ve şarküteri satışı', 'Kaymak Kapları': 'kaymak, tereyağı ve kahvaltılık ürün satışı',
 'PP Yuvarlak Kaseler': 'çorba, yoğurt, turşu, zeytin ve sulu gıdaların saklanması', 'Helva Kapları': 'helva, tahin ve tatlı satışı', 'Yumurta Viyolleri': 'tavuk ve bıldırcın yumurtası satışı',
 'Peynir Kapları': 'peynir, tereyağı ve kahvaltılık ürün satışı', 'Parti Bardak ve Tabakları': 'parti, doğum günü ve organizasyon ikramı',
 'İtalyan Serisi Tabak ve Bardaklar': 'yemek, pizza ve içecek servisi', 'PP Bardaklar': 'su, çay, ayran ve içecek servisi', 'Standart Tabaklar': 'yemek, pasta ve ikram servisi',
 'Plastik Çatallar': 'paket servis, catering ve ikram', 'Plastik Kaşıklar': 'paket servis, catering ve ikram', 'Plastik Bıçaklar': 'paket servis, catering ve ikram',
 'Dondurma Kaşıkları': 'dondurma, tatlı ve puding servisi', 'Hazır Yemek Setleri': 'paket servis ve catering siparişleri',
}
MAT_BK = {'PET': 'PET (polietilen tereftalat); kristal şeffaf, darbeye dayanıklı', 'PP': 'PP (polipropilen); hafif, esnek ve ısıya dayanıklı',
          'PS': 'PS (polistiren); sert ve parlak yüzeyli', 'PS (strafor)': 'genleştirilmiş polistiren (strafor); ısı yalıtımlı ve hafif',
          'OPP': 'OPP (oriented polipropilen) film; parlak ve şeffaf', 'Karton': 'gıdayla temasa uygun karton', 'Alüminyum': 'gıdaya uygun alüminyum folyo',
          'PET / PP': 'PET kapak ve PP gövde'}
def kind_bk(p):
    a = tr_lower(p['ad'])
    for key, k, what, tg in KIND_BK:
        if re.search(key, a): return k, what, tg
def aciklama_bk(p):
    k, what, _ = kind_bk(p); L = []
    use = USE_BK.get(p.get('alt_grup', ''), 'gıda sunumu ve paket servis')
    L.append(f"{title(p)}, {what}. {use[0].upper() + use[1:]} için uygundur.")
    oz = []
    if p['olcu']: oz.append(('ağız çapı ' + p['olcu'][1:] + ' mm') if p['olcu'].startswith('Ø') else
                            (f"uzunluk {p['olcu']} mm" if 'x' not in p['olcu'] else f"ürün ölçüsü {dims(p['olcu'])}"))
    if p['hacim']: oz.append(f"{p['hacim']} cc hacim")
    if p.get('agirlik_g'): oz.append(f"ürün ağırlığı {p['agirlik_g']} g")
    if p['materyal']: oz.append(f"{p['materyal']} hammadde")
    L.append("Teknik özellikler: " + (", ".join(oz) if oz else "ölçü ve materyal bilgisi için bizimle iletişime geçin") + ".")
    m = MAT_BK.get(p['materyal'])
    L.append((m[0].upper() + m[1:] + ". " if m else "") + "Gıdayla temasa uygun hammaddeden üretilmiştir; hijyenik ve tek kullanımlıktır.")
    L.append("Üretici beyanına göre −10 °C'de 24 saate, +60 °C'de 1 saate kadar kullanıma uygundur.")
    if p['koli'] and p['koli_ici']: L.append(f"Toptan satış koli bazındadır: bir kolide {p['koli_ici']} adet, koli ölçüsü {dims(p['koli'])}.")
    elif p['koli_ici']: L.append(f"Toptan satış koli bazındadır: bir kolide {p['koli_ici']} adet.")
    else: L.append("Koli düzeni, sipariş adedi ve teslimat için bizimle iletişime geçin.")
    if p.get('not'): L[-1] += " Not: " + p['not']
    return L
def tags_bk(p):
    k, _, tg = kind_bk(p); out = [tr_lower(p['ad'])] + tg
    if p['hacim'] and k not in ('catal', 'kasik', 'bicak'): out.append(f"{p['hacim']} cc {tg[0]}")
    if p.get('alt_grup'): out.append(tr_lower(p['alt_grup']))
    if p['materyal'] in ('PET', 'PP', 'PS'): out.append(p['materyal'].lower() + ' ' + {'catal': 'çatal', 'kasik': 'kaşık', 'bicak': 'bıçak'}.get(k, 'ambalaj'))
    out += ['gıda ambalajı', {'Karton': 'karton ambalaj', 'Alüminyum': 'alüminyum ambalaj', 'OPP': 'şeffaf ambalaj'}.get(p['materyal'], 'plastik ambalaj'),
            'tek kullanımlık ambalaj', 'horeca ambalaj', 'toptan ambalaj', 'paket servis ambalajı']
    return out[:13] + [p['kod'].lower()]

def dedupe(ts, n=14):
    seen = set(); res = []
    for t in ts:
        t = t.strip()
        if t and t not in seen: seen.add(t); res.append(t)
    return res[:n]

def aciklama(p):
    return {'promocup': aciklama_pc, 'helmex': aciklama_hx, 'bukap': aciklama_bk}.get(supplier(p), aciklama_cp)(p)
def tags(p):
    return dedupe({'promocup': tags_pc, 'helmex': tags_hx, 'bukap': tags_bk}.get(supplier(p), tags_cp)(p))

# ================= görseller =================
def white_square(im, size=1200, pad=0.06, sharpen=False):
    im = im.convert('RGBA')
    bg = Image.new('RGB', (size, size), 'white')
    m = int(size * pad); box = size - 2 * m
    r = min(box / im.width, box / im.height)
    im2 = im.resize((max(1, int(im.width * r)), max(1, int(im.height * r))), Image.LANCZOS)
    if sharpen and r > 1.5:  # küçük kaynak görsel büyütülünce yumuşar
        a = im2.split()[3]; im2 = im2.convert('RGB').filter(ImageFilter.UnsharpMask(radius=1.6, percent=70, threshold=2)); im2.putalpha(a)
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
    white_square(src, sharpen=(sup == 'bukap')).save(os.path.join(d, sl + '.jpg'), quality=92, optimize=True, subsampling=0)
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
        'min_siparis': ('25.000 adet (siparişe özel üretim)' if kind(p) == 'canta' else (p['koli_ici'] + ' adet (1 koli)') if p['koli_ici'] else ((p['moq'] if 'adet' in p['moq'] else p['moq'] + ' adet') if p.get('moq') else 'Bizimle iletişime geçin')),
        'gsm': p.get('gsm', ''), 'moq': p.get('moq', ''), 'varyantlar': p.get('varyantlar', []),
        'not': p.get('not', ''), 'alt_kategori': p.get('alt_grup', ''),
        'aciklama': ac, 'aciklama_html': '<p>' + '</p>\n<p>'.join(ac) + '</p>',
        'etiketler': tg, 'marka': 'EUPLUS',
        'gorseller': {'jpg': f"{RAW}/{sl}/{sl}.jpg", 'png': f"{RAW}/{sl}/{sl}.png", 'png_seffaf': transparent,
                      'not': 'Kategori tanıtım fotoğrafı; ürüne özel fotoğraf yok' if shared else ''},
        'kaynak': {'tedarikci': sup, 'tedarikci_ad': SUPPLIERS.get(sup, {}).get('ad', sup),
                   'tedarikci_kodu': p.get('tedarikci_kodu') or (p['kod'] if sup == 'crystal-pack' else ''),
                   'kaynak_sayfa': p.get('kaynak_sayfa', ''),
                   'katalog': f"kaynaklar/{sup}/" + (SUPPLIERS.get(sup, {}).get('kataloglar') or [{'dosya': ''}])[0]['dosya']},
    }
    json.dump(rec, open(os.path.join(d, 'urun.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    with open(os.path.join(d, 'ilan.md'), 'w', encoding='utf-8') as f:
        f.write(f"# {rec['baslik']}\n\n**Stok kodu:** {p['kod']}  ·  **Kategori:** {rec['kategori']}  ·  **Marka:** EUPLUS\n\n")
        f.write('\n\n'.join(ac) + '\n\n')
        f.write('| Özellik | Değer |\n|---|---|\n')
        if sup == 'helmex':
            tbl = [(k_, v_) for k_, v_ in [('Ölçü', p.get('olcu')), ('Hacim', p.get('hacim')), ('Materyal', p.get('materyal')), ('Gramaj', p.get('gsm')),
                                           ('Ürün ağırlığı', g(p['agirlik_g']) if p.get('agirlik_g') else ''), ('Koli içi adet', p.get('koli_ici')), ('Koli ölçüsü', dims(p['koli']) if p.get('koli') else ''),
                                           ('Palet', (p['palet'] + ' koli') if p.get('palet') else ''), ('Minimum sipariş', (p['moq'] if 'adet' in p['moq'] else p['moq'] + ' adet') if p.get('moq') else ''), ('Not', p.get('not'))] if v_]
        elif sup == 'bukap':
            tbl = [(k_, v_) for k_, v_ in [('Alt kategori', p.get('alt_grup')), ('Ürün ölçüsü', dims(p['olcu']) if p['olcu'] else ''), ('Hacim', (p['hacim'] + ' cc') if p['hacim'] else ''),
                                           ('Ürün ağırlığı', g(p['agirlik_g']) if p.get('agirlik_g') else ''), ('Materyal', p['materyal']), ('Koli ölçüsü', dims(p['koli']) if p['koli'] else ''),
                                           ('Koli içi adet', p['koli_ici'])] if v_]
        elif sup == 'promocup':
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
        vs = p.get('varyantlar') or []
        if vs:
            cols = sec.get('sutunlar') or []
            for t in sec.get('tablolar') or []:
                if p['kod'] in t.get('urunler', []): cols = t['sutunlar']
            cols = [c for c in cols if c[1] not in ('kod',) and any(v.get(c[1]) for v in vs)]
            if cols:
                f.write(f"\n**Standart ölçüler ({len(vs)}):**\n\n| " + ' | '.join(c[0] for c in cols) + " |\n|" + '---|' * len(cols) + "\n")
                for v in vs: f.write('| ' + ' | '.join(str(v.get(c[1], '') or '—') for c in cols) + ' |\n')
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
