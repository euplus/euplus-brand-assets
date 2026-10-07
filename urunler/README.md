# EUPLUS · Ürün Görselleri ve İlan Metinleri

Web sitesi, pazaryeri ilanı, katalog ve teklif dosyalarında kullanılmak üzere ürün
fotoğrafları ve hazır ilan metinleri. Her ürün kendi klasöründe:

```
urunler/<urun-slug>/
├── <urun-slug>.jpg   ← 1200×1200 beyaz zemin (pazaryeri)
├── <urun-slug>.png   ← şeffaf zemin (kendi siteniz, tasarım)
├── urun.json         ← yapısal veri (başlık, açıklama, etiket, ölçü)
└── ilan.md           ← kopyala-yapıştır ilan metni
```

Toplu içe aktarma için: [`urunler.csv`](urunler.csv) (Excel/pazaryeri) · [`urunler.json`](urunler.json) (API/otomasyon)

Bu dosyalar [`katalog/build_urunler.py`](../katalog/build_urunler.py) ile [`katalog/urunler.json`](../katalog/urunler.json) verisinden üretilir; elle düzenlemek yerine
kaynağı düzeltip betiği yeniden çalıştırın.

---

## Bardak kılıfı (sleeve) — 14 oz / 16 oz

| Ürün | Klasör | Görsel |
|---|---|---|
| 14oz - 16oz **Siyah** Karton Bardak Kılıfı | [`bardak-kilifi-siyah`](bardak-kilifi-siyah) | ⚠️ fotoğraf eklenmedi |
| 14oz - 16oz **Kraft** Karton Bardak Kılıfı | [`bardak-kilifi-kraft`](bardak-kilifi-kraft) | ⚠️ fotoğraf eklenmedi |

### 14oz - 16oz Siyah Karton Bardak Kılıfı

14 ve 16 oz karton bardaklar ile uyumlu bardak tutacağıdır. Karton Siyah Sleeve olarak da
tanımlanmaktadır. Çay, kahve, çorba gibi sıcak içeceklerin karton bardakta el yakmadan
içilmesine olanak sağlar. Çift bardak kullanma gereksinimini ortadan kaldırır.

Doğaya geri dönüşen kağıttan imal edilmiştir. Doğa ve çevre dostu bir üründür.

**Etiketler:** `14oz - 16oz Siyah Karton Bardak Kılıfı`, `siyah bardak kılıfı`,
`14oz bardak kılıfı`, `16 oz bardak kılıfı`, `karton sleeve`, `bardak sleevi`,
`bardak slivi`, `bardak tutacağı`, `bardak silivi`

### 14oz - 16oz Kraft Karton Bardak Kılıfı

14 ve 16 oz karton bardaklar ile uyumlu bardak tutacağıdır. Karton Kraft Sleeve olarak da
tanımlanmaktadır. Çay, kahve, çorba gibi sıcak içeceklerin karton bardakta el yakmadan
içilmesine olanak sağlar. Çift bardak kullanma gereksinimini ortadan kaldırır.

Doğaya geri dönüşen kağıttan imal edilmiştir. Doğa ve çevre dostu bir üründür.

**Etiketler:** `14oz - 16oz Kraft Karton Bardak Kılıfı`, `kraft bardak kılıfı`,
`14oz bardak kılıfı`, `16 oz bardak kılıfı`, `karton sleeve`, `bardak sleevi`,
`bardak slivi`, `bardak tutacağı`, `bardak silivi`

---

## Şeffaf sunum ambalajları — 93 ürün

Ölçü ve koli bilgileri [Ürün Kataloğu 2026](../katalog/EUPLUS-Urun-Katalogu-2026.pdf) ile aynıdır.
Her satırdaki klasörde ilan metni, etiketler ve iki formatta görsel bulunur.

### Sütlü Tatlı Kapları (42 ürün)

| Kod | Ürün | Hacim | Ölçü (mm) | Koli içi | Klasör |
|---|---|---|---|---|---|
| CP07 | Lumina Dikdörtgen Kase 300 cc | 300 cc | 118×59×63 | 352 | [`cp07-lumina-dikdortgen-kase`](cp07-lumina-dikdortgen-kase) |
| CP08 | Luxe Kare Kavanoz Kutu | 270 cc | 73×63×73 | 390 | [`cp08-luxe-kare-kavanoz-kutu`](cp08-luxe-kare-kavanoz-kutu) |
| CP09 | İnnova Kavanoz | 270 cc | 70×70×80 | 324 | [`cp09-innova-kavanoz`](cp09-innova-kavanoz) |
| CP10 | İnnova Kavanoz | 300 cc | 75×75×90 | — | [`cp10-innova-kavanoz`](cp10-innova-kavanoz) |
| CP73 | 180 cc Bodega Kase | 180 cc | 70×60×58 | 300 | [`cp73-180-cc-bodega-kase`](cp73-180-cc-bodega-kase) |
| CP74 | 250 cc Bodega Kase | 250 cc | 80×70×60 | 300 | [`cp74-250-cc-bodega-kase`](cp74-250-cc-bodega-kase) |
| CP75 | 380 cc Bodega Kase | 380 cc | 88×83×72 | 600 | [`cp75-380-cc-bodega-kase`](cp75-380-cc-bodega-kase) |
| CP74-K-B | 83 Çap Bodega Kapak (Bombe) | — | — | 600 | [`cp74-k-b-83-cap-bodega-kapak-bombe`](cp74-k-b-83-cap-bodega-kapak-bombe) |
| CP74-K-D | 83 Çap Bodega Kapak (Düz) | — | — | 600 | [`cp74-k-d-83-cap-bodega-kapak-duz`](cp74-k-d-83-cap-bodega-kapak-duz) |
| CP14 | Verrine Mika Kase 280 cc | 280 cc | 110×70×63 | 510 | [`cp14-verrine-mika-kase`](cp14-verrine-mika-kase) |
| CP15 | Verona Mika Kase 330 cc | 330 cc | 115×73×73 | 400 | [`cp15-verona-mika-kase`](cp15-verona-mika-kase) |
| CP16 | Mika Karaman Kase 270-300 cc | 270-300 cc | 106×75×90 | 400 | [`cp16-mika-karaman-kase`](cp16-mika-karaman-kase) |
| CP17 | Puding Kase 280 cc | 280 cc | 115×70×60 | 500 | [`cp17-puding-kase`](cp17-puding-kase) |
| CP13-16-K | 105 Çap Bombe Kapak | — | 105×90×30 | 1000 | [`cp13-16-k-105-cap-bombe-kapak`](cp13-16-k-105-cap-bombe-kapak) |
| CP40 | Fora Mika Kutu 300 cc | 300 cc | 115×115×45 | 500 | [`cp40-fora-mika-kutu`](cp40-fora-mika-kutu) |
| CP40-K | 115x115 Bombe Kapak | — | 115×115×25 | 1350 | [`cp40-k-115x115-bombe-kapak`](cp40-k-115x115-bombe-kapak) |
| CP39 | Lotus Kare Kase 260 cc | 260 cc | 116×65×65 | 700 | [`cp39-lotus-kare-kase`](cp39-lotus-kare-kase) |
| CP41 | Elegant Kutu 270 cc | 270 cc | 115×115×45 | 500 | [`cp41-elegant-kutu`](cp41-elegant-kutu) |
| CP42 | Elite Kutu 250 cc | 250 cc | 100×70×45 | 500 | [`cp42-elite-kutu`](cp42-elite-kutu) |
| CP11 | Tiny Kutu 220 cc | 220 cc | 102×80×64 | 800 | [`cp11-tiny-kutu`](cp11-tiny-kutu) |
| CP13 | Simple Kutu 220 cc | 220 cc | 105×60×50 | 1000 | [`cp13-simple-kutu`](cp13-simple-kutu) |
| CP12 | Class Kutu 160 cc | 160 cc | 118×70×40 | 1000 | [`cp12-class-kutu`](cp12-class-kutu) |
| CP12-K | 118 Çap Bombe Kapak | — | 118×90×25 | 1000 | [`cp12-k-118-cap-bombe-kapak`](cp12-k-118-cap-bombe-kapak) |
| CP61 | 200 cc Ayaklı Kase | 200 cc | 95×58×60 | 500 | [`cp61-200-cc-ayakli-kase`](cp61-200-cc-ayakli-kase) |
| CP62 | Daisy Ayaklı Kase 220 cc | 220 cc | 95×60×73 | 500 | [`cp62-daisy-ayakli-kase`](cp62-daisy-ayakli-kase) |
| CP60 | 240 cc Ayaklı Kase | 240 cc | 95×90×70 | 440 | [`cp60-240-cc-ayakli-kase`](cp60-240-cc-ayakli-kase) |
| CP65 | Swan Ayaklı Kase 240 cc | 240 cc | 79×81×139 | 600 | [`cp65-swan-ayakli-kase`](cp65-swan-ayakli-kase) |
| CP80 | 60 cc Prizma Kase | 60 cc | 49×29×45 | 1000 | [`cp80-60-cc-prizma-kase`](cp80-60-cc-prizma-kase) |
| CP81 | 120 cc Prizma Kase | 120 cc | 58×38×60 | 1000 | [`cp81-120-cc-prizma-kase`](cp81-120-cc-prizma-kase) |
| CP82 | 200 cc Prizma Kase | 200 cc | 70×40×165 | 1000 | [`cp82-200-cc-prizma-kase`](cp82-200-cc-prizma-kase) |
| CP83 | 240 cc Prizma Kase | 240 cc | — | 1000 | [`cp83-240-cc-prizma-kase`](cp83-240-cc-prizma-kase) |
| CP85 | Verona Bardak 60 cc | 60 cc | 50×45×65 | 360 | [`cp85-verona-bardak-60-cc`](cp85-verona-bardak-60-cc) |
| CP86 | Verona Bardak 150 cc | 150 cc | 70×55×80 | 300 | [`cp86-verona-bardak-150-cc`](cp86-verona-bardak-150-cc) |
| CP71 | Verona Bardak 240 cc | 240 cc | 80×45×100 | 300 | [`cp71-verona-bardak-240-cc`](cp71-verona-bardak-240-cc) |
| CP84 | Asimetrik Kap 250 cc | 250 cc | 110×55×72 | 300 | [`cp84-asimetrik-kap`](cp84-asimetrik-kap) |
| CP43 | Profiterol Kutu 500 cc | 500 cc | 210×130×60 | 110 | [`cp43-profiterol-kutu-500-cc`](cp43-profiterol-kutu-500-cc) |
| CP44 | Profiterol Kutu 1000 cc | 1000 cc | 210×130×85 | 150 | [`cp44-profiterol-kutu-1000-cc`](cp44-profiterol-kutu-1000-cc) |
| CP450 | 150 cc PET Kavanoz | 150 cc | 90×90×45 | 230 | [`cp450-150-cc-pet-kavanoz`](cp450-150-cc-pet-kavanoz) |
| CP460 | 250 cc PET Kavanoz | 250 cc | 90×90×60 | 130 | [`cp460-250-cc-pet-kavanoz`](cp460-250-cc-pet-kavanoz) |
| CP410 | 50 cc PET Kavanoz | 50 cc | 64×64×35 | 550 | [`cp410-50-cc-pet-kavanoz`](cp410-50-cc-pet-kavanoz) |
| CP420 | 100 cc PET Kavanoz | 100 cc | 64×64×55 | 500 | [`cp420-100-cc-pet-kavanoz`](cp420-100-cc-pet-kavanoz) |
| CP430 | 150 cc PET Kavanoz | 150 cc | 64×64×75 | 350 | [`cp430-150-cc-pet-kavanoz`](cp430-150-cc-pet-kavanoz) |

### Lokum & Çikolata Kapları (30 ürün)

| Kod | Ürün | Hacim | Ölçü (mm) | Koli içi | Klasör |
|---|---|---|---|---|---|
| CP110 | Specific 270 cc | 270 cc | 128×128×31 | 350 | [`cp110-specific-270-cc`](cp110-specific-270-cc) |
| CP111 | Specific 450 cc | 450 cc | 157×157×34 | 175 | [`cp111-specific-450-cc`](cp111-specific-450-cc) |
| CP112 | Specific 700 cc | 700 cc | 198×198×34 | 120 | [`cp112-specific-700-cc`](cp112-specific-700-cc) |
| CP110 3-S | Şeffaf 3 Bölme Separatör | — | 120×120×30 | — | [`cp110-3-s-seffaf-3-bolme-separator`](cp110-3-s-seffaf-3-bolme-separator) |
| CP111 2-S | Gold 2 Bölme Separatör | — | 155×155×30 | — | [`cp111-2-s-gold-2-bolme-separator`](cp111-2-s-gold-2-bolme-separator) |
| CP111 3-S | Gold 3 Bölme Separatör | — | 155×155×30 | — | [`cp111-3-s-gold-3-bolme-separator`](cp111-3-s-gold-3-bolme-separator) |
| CP112 6-S | Kahverengi 6 Bölme Separatör | — | 195×195×30 | — | [`cp112-6-s-kahverengi-6-bolme-separator`](cp112-6-s-kahverengi-6-bolme-separator) |
| CP141 | Angular Kutu 770 cc | 770 cc | 122×260×33 | 90 | [`cp141-angular-kutu`](cp141-angular-kutu) |
| CP142 | Chocolate Kutu 300 cc | 300 cc | 90×175×31 | 200 | [`cp142-chocolate-kutu-300-cc`](cp142-chocolate-kutu-300-cc) |
| CP143 | Chocolate Kutu 450 cc | 450 cc | 175×90×58 | 105 | [`cp143-chocolate-kutu-450-cc`](cp143-chocolate-kutu-450-cc) |
| CP144 | Chocolate Kutu 600 cc | 600 cc | 140×192×36 | 120 | [`cp144-chocolate-kutu-600-cc`](cp144-chocolate-kutu-600-cc) |
| CP140 | Square Kutu 350 cc | 350 cc | 118×118×35 | 280 | [`cp140-square-kutu`](cp140-square-kutu) |
| CP160 | Kare Draje Kutu 100 cc | 100 cc | 85×102×38 | 750 | [`cp160-kare-draje-kutu-100-cc`](cp160-kare-draje-kutu-100-cc) |
| CP161 | Kare Draje Kutu 200 cc | 200 cc | 85×102×47 | 800 | [`cp161-kare-draje-kutu-200-cc`](cp161-kare-draje-kutu-200-cc) |
| CP165 | Mini Cup 100 cc | 100 cc | 70×68×76 | 1000 | [`cp165-mini-cup`](cp165-mini-cup) |
| CP170 | Ayıcık Kutu 500 cc | 500 cc | 170×100×71 | 60 | [`cp170-ayicik-kutu-500-cc`](cp170-ayicik-kutu-500-cc) |
| CP171 | Crystal Şişe 250 cc | 250 cc | 28×58×200 | 250 | [`cp171-crystal-sise`](cp171-crystal-sise) |
| CP181 | Büyük Creta Kutu 800 cc | 800 cc | 106×190×75 | 60 | [`cp181-buyuk-creta-kutu`](cp181-buyuk-creta-kutu) |
| CP185 | Gift Kutu Büyük 1200 cc | 1200 cc | 167×167×95 | 48 | [`cp185-gift-kutu-buyuk`](cp185-gift-kutu-buyuk) |
| CP189 | Macaron Kutu 6'lı | — | 170×60×55 | 185 | [`cp189-macaron-kutu-6-li`](cp189-macaron-kutu-6-li) |
| CP190 | Kalp Kutu 100 cc | 100 cc | 79×79×29 | 660 | [`cp190-kalp-kutu-100-cc`](cp190-kalp-kutu-100-cc) |
| CP191 | Kalp Kutu 150 cc | 150 cc | 92×92×36 | 360 | [`cp191-kalp-kutu-150-cc`](cp191-kalp-kutu-150-cc) |
| CP192 | Orta Kalp Kutu 300 cc | 300 cc | 120×120×50 | 450 | [`cp192-orta-kalp-kutu`](cp192-orta-kalp-kutu) |
| CP193 | Büyük Kalp Kutu 500 cc | 500 cc | 160×140×50 | 280 | [`cp193-buyuk-kalp-kutu`](cp193-buyuk-kalp-kutu) |
| CP200 | Oval Açık Tabak 150 cc | 150 cc | 121×191×15 | 600 | [`cp200-oval-acik-tabak-150-cc`](cp200-oval-acik-tabak-150-cc) |
| CP201 | Oval Açık Tabak 400 cc | 400 cc | 188×275×15 | 280 | [`cp201-oval-acik-tabak-400-cc`](cp201-oval-acik-tabak-400-cc) |
| CP202 | Oval Açık Tabak 600 cc | 600 cc | 210×307×15 | 180 | [`cp202-oval-acik-tabak-600-cc`](cp202-oval-acik-tabak-600-cc) |
| CP203 | Kalp Tabak (Açık) 350 cc | 350 cc | 230×210×15 | 300 | [`cp203-kalp-tabak-acik`](cp203-kalp-tabak-acik) |
| CP204 | Papatya Tabak (Açık) 300 cc | 300 cc | 185×185×15 | 560 | [`cp204-papatya-tabak-acik`](cp204-papatya-tabak-acik) |
| CP205 | Yuvarlak Açık Tabak 500 cc | 500 cc | 208×208×21 | 300 | [`cp205-yuvarlak-acik-tabak`](cp205-yuvarlak-acik-tabak) |

### Bal Kapları (21 ürün)

| Kod | Ürün | Hacim | Ölçü (mm) | Koli içi | Klasör |
|---|---|---|---|---|---|
| CP316 | Honey Kutu 250 cc | 250 cc | 87×114×45 | 470 | [`cp316-honey-kutu-250-cc`](cp316-honey-kutu-250-cc) |
| CP317 | Honey Kutu 500 cc | 500 cc | 114×150×46 | 240 | [`cp317-honey-kutu-500-cc`](cp317-honey-kutu-500-cc) |
| CP318 | Honey Kutu 650 cc | 650 cc | 126×170×48 | 200 | [`cp318-honey-kutu-650-cc`](cp318-honey-kutu-650-cc) |
| CP319 | Honey Kutu 1000 cc | 1000 cc | 126×225×52 | 140 | [`cp319-honey-kutu-1000-cc`](cp319-honey-kutu-1000-cc) |
| CP320 | Standart Honey Kutu 500 cc | 500 cc | 117×117×53 | 180 | [`cp320-standart-honey-kutu-500-cc`](cp320-standart-honey-kutu-500-cc) |
| CP321 | Standart Honey Kutu 1000 cc | 1000 cc | 117×206×53 | 80 | [`cp321-standart-honey-kutu-1000-cc`](cp321-standart-honey-kutu-1000-cc) |
| CP322 | Honeycomb Kutu 400 cc | 400 cc | 119×140×40 | 200 | [`cp322-honeycomb-kutu-400-cc`](cp322-honeycomb-kutu-400-cc) |
| CP323 | Honeycomb Kutu 1000 cc | 1000 cc | 116×205×55 | 180 | [`cp323-honeycomb-kutu-1000-cc`](cp323-honeycomb-kutu-1000-cc) |
| CP324 | Honeycomb Kutu 1350 cc | 1350 cc | 165×232×53 | 50 | [`cp324-honeycomb-kutu-1350-cc`](cp324-honeycomb-kutu-1350-cc) |
| CP360 | Yuvarlak Honey Kutu 300 cc | 300 cc | 104×104×53 | 360 | [`cp360-yuvarlak-honey-kutu-300-cc`](cp360-yuvarlak-honey-kutu-300-cc) |
| CP361 | Yuvarlak Honey Kutu 650 cc | 600 cc | 156×156×55 | 185 | [`cp361-yuvarlak-honey-kutu-650-cc`](cp361-yuvarlak-honey-kutu-650-cc) |
| CP362 | Yuvarlak Honey Kutu 700 cc | 600 cc | 156×156×58 | 185 | [`cp362-yuvarlak-honey-kutu-700-cc`](cp362-yuvarlak-honey-kutu-700-cc) |
| CP363 | Yuvarlak Honey Kutu 1520 cc | 1520 cc | 230×230×53 | 70 | [`cp363-yuvarlak-honey-kutu-1520-cc`](cp363-yuvarlak-honey-kutu-1520-cc) |
| CP364 | Altıgen Honey Kutu 1600 cc | 1600 cc | 230×230×53 | 50 | [`cp364-altigen-honey-kutu`](cp364-altigen-honey-kutu) |
| CP313 | Küçük Boy Kasa 300 cc | 300 cc | 90×140×44 | 220 | [`cp313-kucuk-boy-kasa`](cp313-kucuk-boy-kasa) |
| CP314 | Orta Boy Kasa 400 cc | 400 cc | 111×157×46 | 165 | [`cp314-orta-boy-kasa`](cp314-orta-boy-kasa) |
| CP315 | Büyük Boy Kasa 500 cc | 500 cc | 114×180×44 | 150 | [`cp315-buyuk-boy-kasa`](cp315-buyuk-boy-kasa) |
| CP310 | Açık Küçük Tabak 250 cc | 250 cc | 108×135×26 | 620 | [`cp310-acik-kucuk-tabak`](cp310-acik-kucuk-tabak) |
| CP311 | Açık Orta Tabak 450 cc | 450 cc | 128×172×27 | 360 | [`cp311-acik-orta-tabak`](cp311-acik-orta-tabak) |
| CP312 | Açık Büyük Tabak 500 cc | 500 cc | 144×195×27 | 360 | [`cp312-acik-buyuk-tabak`](cp312-acik-buyuk-tabak) |
| CP370 | Honey Kaşık | — | 125×30 | 4500 | [`cp370-honey-kasik`](cp370-honey-kasik) |

---

## Paket servis ambalajları — 72 ürün

Ölçü ve koli bilgileri [Paket Servis Kataloğu 2026](../katalog/EUPLUS-Paket-Servis-Katalogu-2026.pdf) ile aynıdır.
Bardak, kase, PET ürün ve kapaklarda kaynak katalogda ürün başına değil **kategori başına** tanıtım fotoğrafı
bulunduğu için bu ürünlerin JPG/PNG görselleri kategori fotoğrafıdır (PNG opak). Kutular ve kağıt çantalar
ürüne özel, şeffaf zeminli görsellerle gelir. Kodlardaki `PC` öneki kaynak kataloğu belirtir; ürünler EUPLUS
markasıyla listelenir.


### Tek Katlı Sıcak İçecek Bardakları (5 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-TB04 | 4 oz Tek Katlı Sıcak İçecek Bardağı | Ø63/Ø46×60 | PE kaplı karton | 1000 | [`pc-tb04-4-oz-tek-katli-sicak-icecek-bardagi`](pc-tb04-4-oz-tek-katli-sicak-icecek-bardagi) |
| PC-TB07 | 7 oz Tek Katlı Sıcak İçecek Bardağı | Ø72/Ø51×80 | PE kaplı karton | 3000 | [`pc-tb07-7-oz-tek-katli-sicak-icecek-bardagi`](pc-tb07-7-oz-tek-katli-sicak-icecek-bardagi) |
| PC-TB08 | 8 oz Tek Katlı Sıcak İçecek Bardağı | Ø80/Ø57×88 | PE kaplı karton | 2000 | [`pc-tb08-8-oz-tek-katli-sicak-icecek-bardagi`](pc-tb08-8-oz-tek-katli-sicak-icecek-bardagi) |
| PC-TB14 | 14 oz Tek Katlı Sıcak İçecek Bardağı | Ø90/Ø60×110 | PE kaplı karton | 1000 | [`pc-tb14-14-oz-tek-katli-sicak-icecek-bardagi`](pc-tb14-14-oz-tek-katli-sicak-icecek-bardagi) |
| PC-TB16 | 16 oz Tek Katlı Sıcak İçecek Bardağı | Ø90/Ø63×135 | PE kaplı karton | 1000 | [`pc-tb16-16-oz-tek-katli-sicak-icecek-bardagi`](pc-tb16-16-oz-tek-katli-sicak-icecek-bardagi) |

### Çift Katlı Sıcak İçecek Bardakları (3 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-CB08 | 8 oz Çift Katlı Sıcak İçecek Bardağı | Ø80/Ø57×88 | PE kaplı karton | 600 | [`pc-cb08-8-oz-cift-katli-sicak-icecek-bardagi`](pc-cb08-8-oz-cift-katli-sicak-icecek-bardagi) |
| PC-CB14 | 14 oz Çift Katlı Sıcak İçecek Bardağı | Ø90/Ø60×110 | PE kaplı karton | 500 | [`pc-cb14-14-oz-cift-katli-sicak-icecek-bardagi`](pc-cb14-14-oz-cift-katli-sicak-icecek-bardagi) |
| PC-CB16 | 16 oz Çift Katlı Sıcak İçecek Bardağı | Ø90/Ø63×135 | PE kaplı karton | 360 | [`pc-cb16-16-oz-cift-katli-sicak-icecek-bardagi`](pc-cb16-16-oz-cift-katli-sicak-icecek-bardagi) |

### Soğuk İçecek Bardakları (6 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-SB09 | 9 oz Soğuk İçecek Bardağı | Ø77/Ø51×103 | PE kaplı karton | 2000 | [`pc-sb09-9-oz-soguk-icecek-bardagi`](pc-sb09-9-oz-soguk-icecek-bardagi) |
| PC-SB12 | 12 oz Soğuk İçecek Bardağı | Ø80/Ø51×119 | PE kaplı karton | 2000 | [`pc-sb12-12-oz-soguk-icecek-bardagi`](pc-sb12-12-oz-soguk-icecek-bardagi) |
| PC-SB16 | 16 oz Soğuk İçecek Bardağı | Ø90/Ø63×135 | PE kaplı karton | 1000 | [`pc-sb16-16-oz-soguk-icecek-bardagi`](pc-sb16-16-oz-soguk-icecek-bardagi) |
| PC-SB22 | 22 oz Soğuk İçecek Bardağı | Ø90/Ø61×169 | PE kaplı karton | 1000 | [`pc-sb22-22-oz-soguk-icecek-bardagi`](pc-sb22-22-oz-soguk-icecek-bardagi) |
| PC-SB29 | 29 oz Soğuk İçecek Bardağı | Ø104/Ø62×198 | PE kaplı karton | 848 | [`pc-sb29-29-oz-soguk-icecek-bardagi`](pc-sb29-29-oz-soguk-icecek-bardagi) |
| PC-SB32 | 32 oz Soğuk İçecek Bardağı | Ø105/Ø75×177 | PE kaplı karton | 500 | [`pc-sb32-32-oz-soguk-icecek-bardagi`](pc-sb32-32-oz-soguk-icecek-bardagi) |

### Dondurma Kaseleri (5 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-DK100 | 100 cc Dondurma Kasesi | Ø85/Ø73×44 | PE kaplı karton | 1000 | [`pc-dk100-100-cc-dondurma-kasesi`](pc-dk100-100-cc-dondurma-kasesi) |
| PC-DK200 | 200 cc Dondurma Kasesi | Ø90/Ø75×65 | PE kaplı karton | 1000 | [`pc-dk200-200-cc-dondurma-kasesi`](pc-dk200-200-cc-dondurma-kasesi) |
| PC-DK250 | 250 cc Dondurma Kasesi | Ø97/Ø80×48 | PE kaplı karton | 1000 | [`pc-dk250-250-cc-dondurma-kasesi`](pc-dk250-250-cc-dondurma-kasesi) |
| PC-DK300 | 300 cc Dondurma Kasesi | Ø90/Ø66×82 | PE kaplı karton | 2000 | [`pc-dk300-300-cc-dondurma-kasesi`](pc-dk300-300-cc-dondurma-kasesi) |
| PC-DK400 | 400 cc Dondurma Kasesi | Ø115/Ø100×70 | PE kaplı karton | 700 | [`pc-dk400-400-cc-dondurma-kasesi`](pc-dk400-400-cc-dondurma-kasesi) |

### Salata Kaseleri (12 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-SK550 | 550 cc Salata Kasesi | Ø145/Ø127×52 | Kraft karton | 500 | [`pc-sk550-550-cc-salata-kasesi`](pc-sk550-550-cc-salata-kasesi) |
| PC-SK550-PET | 550 cc Salata Kasesi + PET Kapak | Ø145/Ø127×52 | Kraft karton + PET | 300+300 | [`pc-sk550-pet-550-cc-salata-kasesi-pet-kapak`](pc-sk550-pet-550-cc-salata-kasesi-pet-kapak) |
| PC-SK550-PP | 550 cc Salata Kasesi + PP Kapak | Ø145/Ø127×52 | Kraft karton + PP | 300+300 | [`pc-sk550-pp-550-cc-salata-kasesi-pp-kapak`](pc-sk550-pp-550-cc-salata-kasesi-pp-kapak) |
| PC-SK750 | 750 cc Salata Kasesi | Ø145/Ø125×65 | Kraft karton | 500 | [`pc-sk750-750-cc-salata-kasesi`](pc-sk750-750-cc-salata-kasesi) |
| PC-SK750-PET | 750 cc Salata Kasesi + PET Kapak | Ø145/Ø125×65 | Kraft karton + PET | 300+300 | [`pc-sk750-pet-750-cc-salata-kasesi-pet-kapak`](pc-sk750-pet-750-cc-salata-kasesi-pet-kapak) |
| PC-SK750-PP | 750 cc Salata Kasesi + PP Kapak | Ø145/Ø125×65 | Kraft karton + PP | 300+300 | [`pc-sk750-pp-750-cc-salata-kasesi-pp-kapak`](pc-sk750-pp-750-cc-salata-kasesi-pp-kapak) |
| PC-SK1000 | 1000 cc Salata Kasesi | Ø187/Ø164×55 | Kraft karton | 300 | [`pc-sk1000-1000-cc-salata-kasesi`](pc-sk1000-1000-cc-salata-kasesi) |
| PC-SK1000-PET | 1000 cc Salata Kasesi + PET Kapak | Ø187/Ø164×55 | Kraft karton + PET | 200+200 | [`pc-sk1000-pet-1000-cc-salata-kasesi-pet-kapak`](pc-sk1000-pet-1000-cc-salata-kasesi-pet-kapak) |
| PC-SK1000-PP | 1000 cc Salata Kasesi + PP Kapak | Ø187/Ø164×55 | Kraft karton + PP | 200+200 | [`pc-sk1000-pp-1000-cc-salata-kasesi-pp-kapak`](pc-sk1000-pp-1000-cc-salata-kasesi-pp-kapak) |
| PC-SK1300 | 1300 cc Salata Kasesi | Ø187/Ø161×70 | Kraft karton | 300 | [`pc-sk1300-1300-cc-salata-kasesi`](pc-sk1300-1300-cc-salata-kasesi) |
| PC-SK1300-PET | 1300 cc Salata Kasesi + PET Kapak | Ø187/Ø161×70 | Kraft karton + PET | 200+200 | [`pc-sk1300-pet-1300-cc-salata-kasesi-pet-kapak`](pc-sk1300-pet-1300-cc-salata-kasesi-pet-kapak) |
| PC-SK1300-PP | 1300 cc Salata Kasesi + PP Kapak | Ø187/Ø161×70 | Kraft karton + PP | 200+200 | [`pc-sk1300-pp-1300-cc-salata-kasesi-pp-kapak`](pc-sk1300-pp-1300-cc-salata-kasesi-pp-kapak) |

### Patates Kızartması Kutuları (2 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-PK-01 | Orta Boy Patates Kızartması Kutusu | 85×30×110 | Karton | — | [`pc-pk-01-orta-boy-patates-kizartmasi-kutusu`](pc-pk-01-orta-boy-patates-kizartmasi-kutusu) |
| PC-PK-02 | Büyük Boy Patates Kızartması Kutusu | 83×40×130 | Karton | — | [`pc-pk-02-buyuk-boy-patates-kizartmasi-kutusu`](pc-pk-02-buyuk-boy-patates-kizartmasi-kutusu) |

### Gıda Tavaları (2 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-TV-01 | Gıda Tavası 01 | 70×120×40 | Karton | — | [`pc-tv-01-gida-tavasi-01`](pc-tv-01-gida-tavasi-01) |
| PC-TV-02 | Gıda Tavası 02 | 45×155×40 | Karton | — | [`pc-tv-02-gida-tavasi-02`](pc-tv-02-gida-tavasi-02) |

### Gıda Kutuları (2 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-HK-01 | Gıda Kutusu 01 (Hamburger) | 95×95×70 | Karton | — | [`pc-hk-01-gida-kutusu-01-hamburger`](pc-hk-01-gida-kutusu-01-hamburger) |
| PC-HK-02 | Gıda Kutusu 02 (Menü) | 150×150×100 | Karton | — | [`pc-hk-02-gida-kutusu-02-menu`](pc-hk-02-gida-kutusu-02-menu) |

### Oluklu Gıda Kutuları (5 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-OHK-01 | Oluklu Gıda Kutusu 01 | 150×150×100 | Mikro oluklu mukavva | — | [`pc-ohk-01-oluklu-gida-kutusu-01`](pc-ohk-01-oluklu-gida-kutusu-01) |
| PC-OHK-02 | Oluklu Gıda Kutusu 02 | 200×200×75 | Mikro oluklu mukavva | — | [`pc-ohk-02-oluklu-gida-kutusu-02`](pc-ohk-02-oluklu-gida-kutusu-02) |
| PC-OHK-03 | Oluklu Gıda Kutusu 03 | 200×150×75 | Mikro oluklu mukavva | — | [`pc-ohk-03-oluklu-gida-kutusu-03`](pc-ohk-03-oluklu-gida-kutusu-03) |
| PC-OPZ-01 | Oluklu Pizza Dilim Kutusu | 220×210×40 | Mikro oluklu mukavva | — | [`pc-opz-01-oluklu-pizza-dilim-kutusu`](pc-opz-01-oluklu-pizza-dilim-kutusu) |
| PC-OSK-01 | Oluklu Sandviç Kutusu | 290×90×75 | Mikro oluklu mukavva | — | [`pc-osk-01-oluklu-sandvic-kutusu`](pc-osk-01-oluklu-sandvic-kutusu) |

### PET Bardak ve Kapaklar (7 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-PB12 | 12 oz PET Bardak (95 mm Ø) – 350 ml | Ø95 | PET | 1000 | [`pc-pb12-12-oz-pet-bardak-95-mm-350-ml`](pc-pb12-12-oz-pet-bardak-95-mm-350-ml) |
| PC-PB14 | 14 oz PET Bardak (95 mm Ø) – 400 ml | Ø95 | PET | 1000 | [`pc-pb14-14-oz-pet-bardak-95-mm-400-ml`](pc-pb14-14-oz-pet-bardak-95-mm-400-ml) |
| PC-PB16 | 16 oz PET Bardak (95 mm Ø) – 470 ml | Ø95 | PET | 1000 | [`pc-pb16-16-oz-pet-bardak-95-mm-470-ml`](pc-pb16-16-oz-pet-bardak-95-mm-470-ml) |
| PC-LCT | Pipetsiz Kapak Ø95 mm | Ø95 | PET | 1000 | [`pc-lct-pipetsiz-kapak-95-mm`](pc-lct-pipetsiz-kapak-95-mm) |
| PC-LDO | Delikli Bombeli Kapak Ø95 mm | Ø95 | PET | 1000 | [`pc-ldo-delikli-bombeli-kapak-95-mm`](pc-ldo-delikli-bombeli-kapak-95-mm) |
| PC-LCX | "X" Delikli Düz Kapak Ø95 mm | Ø95 | PET | 1000 | [`pc-lcx-x-delikli-duz-kapak-95-mm`](pc-lcx-x-delikli-duz-kapak-95-mm) |
| PC-LBT | Yudum Kapak Ø95 mm | Ø95 | PET | 1000 | [`pc-lbt-yudum-kapak-95-mm`](pc-lbt-yudum-kapak-95-mm) |

### Bardak Kapakları (5 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-LST71 | 7 oz PS Yudum Kapak (Siyah / Beyaz) | — | PS | 2000 | [`pc-lst71-7-oz-ps-yudum-kapak-siyah-beyaz`](pc-lst71-7-oz-ps-yudum-kapak-siyah-beyaz) |
| PC-LBT80 | 8 oz PS Yudum Kapak 80 mm Ø (Siyah / Beyaz) | Ø80 | PS | 1000 | [`pc-lbt80-8-oz-ps-yudum-kapak-80-mm-siyah-beyaz`](pc-lbt80-8-oz-ps-yudum-kapak-80-mm-siyah-beyaz) |
| PC-LBT90 | 12-16 oz PS Yudum Kapak 90 mm Ø (Siyah / Beyaz) | Ø90 | PS | 1000 | [`pc-lbt90-12-16-oz-ps-yudum-kapak-90-mm-siyah-beyaz`](pc-lbt90-12-16-oz-ps-yudum-kapak-90-mm-siyah-beyaz) |
| PC-CL90 | 16-22 oz Soğuk İçecek Kapağı 90 mm Ø | Ø90 | PET | 2000 | [`pc-cl90-16-22-oz-soguk-icecek-kapagi-90-mm`](pc-cl90-16-22-oz-soguk-icecek-kapagi-90-mm) |
| PC-CL80 | 8-12 oz Soğuk İçecek Kapağı 80 mm Ø | Ø80 | PET | 2000 | [`pc-cl80-8-12-oz-soguk-icecek-kapagi-80-mm`](pc-cl80-8-12-oz-soguk-icecek-kapagi-80-mm) |

### Şeffaf Kase Kapakları (9 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-KP145-PP | 145 mm Ø PP Kapak | Ø145 | PP | 400 | [`pc-kp145-pp-145-mm-pp-kapak`](pc-kp145-pp-145-mm-pp-kapak) |
| PC-KP145-PET | 145 mm Ø PET Kapak | Ø145 | PET | 400 | [`pc-kp145-pet-145-mm-pet-kapak`](pc-kp145-pet-145-mm-pet-kapak) |
| PC-KP187-PP | 187 mm Ø PP Kapak | Ø187 | PP | 300 | [`pc-kp187-pp-187-mm-pp-kapak`](pc-kp187-pp-187-mm-pp-kapak) |
| PC-KP187-PET | 187 mm Ø PET Kapak | Ø187 | PET | 300 | [`pc-kp187-pet-187-mm-pet-kapak`](pc-kp187-pet-187-mm-pet-kapak) |
| PC-KP101-PP | 101 mm Ø PP Kapak (250 cc) | Ø101 | PP | 2000 | [`pc-kp101-pp-101-mm-pp-kapak-250-cc`](pc-kp101-pp-101-mm-pp-kapak-250-cc) |
| PC-KP101-PET | 101 mm Ø PET Kapak (250 cc) | Ø101 | PET | 2000 | [`pc-kp101-pet-101-mm-pet-kapak-250-cc`](pc-kp101-pet-101-mm-pet-kapak-250-cc) |
| PC-KP87-PET | 87 mm Ø PET Kapak (100 cc) | Ø87 | PET | 3000 | [`pc-kp87-pet-87-mm-pet-kapak-100-cc`](pc-kp87-pet-87-mm-pet-kapak-100-cc) |
| PC-KP90-PET | 90 mm Ø PET Kapak (200 cc) | Ø90 | PET | 2000 | [`pc-kp90-pet-90-mm-pet-kapak-200-cc`](pc-kp90-pet-90-mm-pet-kapak-200-cc) |
| PC-KP104-PS | 104 mm Ø PS Kapak (29 oz) | Ø104 | PS | 800 | [`pc-kp104-ps-104-mm-ps-kapak-29-oz`](pc-kp104-ps-104-mm-ps-kapak-29-oz) |

### Taşıma ve Aksesuarlar (5 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-HOLDER | Pasta Kutusu / Holder | — | Karton | 500 | [`pc-holder-pasta-kutusu-holder`](pc-holder-pasta-kutusu-holder) |
| PC-TIPA50 | Kapak Tıpası PP 50 mm (Siyah / Beyaz) | — | PP | 500 | [`pc-tipa50-kapak-tipasi-pp-50-mm-siyah-beyaz`](pc-tipa50-kapak-tipasi-pp-50-mm-siyah-beyaz) |
| PC-TIPA109 | Kapak Tıpası PP 109 mm (Siyah / Beyaz) | — | PP | 5000 | [`pc-tipa109-kapak-tipasi-pp-109-mm-siyah-beyaz`](pc-tipa109-kapak-tipasi-pp-109-mm-siyah-beyaz) |
| PC-VIYOL2 | 2'li Bardak Taşıyıcı Viyol (Gri) | — | Kağıt hamuru (pulp) | 480 | [`pc-viyol2-2-li-bardak-tasiyici-viyol-gri`](pc-viyol2-2-li-bardak-tasiyici-viyol-gri) |
| PC-VIYOL4 | 4'lü Bardak Taşıyıcı Viyol (Gri) | — | Kağıt hamuru (pulp) | 220 | [`pc-viyol4-4-lu-bardak-tasiyici-viyol-gri`](pc-viyol4-4-lu-bardak-tasiyici-viyol-gri) |

### Kağıt Çantalar (4 ürün)

| Kod | Ürün | Ölçü (mm) | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|
| PC-CNT-BK-DS | Beyaz Kraft Çanta – Düz Saplı | — | Beyaz kraft kağıt | min. 25.000 | [`pc-cnt-bk-ds-beyaz-kraft-canta-duz-sapli`](pc-cnt-bk-ds-beyaz-kraft-canta-duz-sapli) |
| PC-CNT-KR-DS | Kraft Çanta – Düz Saplı | — | Kraft kağıt | min. 25.000 | [`pc-cnt-kr-ds-kraft-canta-duz-sapli`](pc-cnt-kr-ds-kraft-canta-duz-sapli) |
| PC-CNT-KR-BS | Kraft Çanta – Burgu Saplı | — | Kraft kağıt | min. 25.000 | [`pc-cnt-kr-bs-kraft-canta-burgu-sapli`](pc-cnt-kr-bs-kraft-canta-burgu-sapli) |
| PC-CNT-BK-BS | Beyaz Kraft Çanta – Burgu Saplı | — | Beyaz kraft kağıt | min. 25.000 | [`pc-cnt-bk-bs-beyaz-kraft-canta-burgu-sapli`](pc-cnt-bk-bs-beyaz-kraft-canta-burgu-sapli) |

---

## Fast food & restoran ambalajları — 81 ürün

Ölçü ve koli bilgileri [Fast Food & Restoran Ambalajları Kataloğu 2026](../katalog/EUPLUS-Fast-Food-Katalogu-2026.pdf) ile aynıdır.
Kaynak katalogdaki görseller kategori fotoğrafı ve mockup'tır; mockup'lardaki tedarikçi logosu kaldırıldı, PNG'ler opaktır.
Ölçü tablosu olan ürünler (pizza, pasta kutusu, çantalar, torbalar, kağıtlar, ıslak mendil, peçete, çatal-bıçak seti) tek ürün
olarak listelenir; standart ölçüler `urun.json` içindeki `varyantlar` alanında ve `ilan.md` tablosundadır. Kodlardaki `HX` öneki
kaynak kataloğu belirtir; ürünler EUPLUS markasıyla listelenir.


### Karton servis ambalajları


#### Burger Kutuları (3 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-XBS01 | Küçük Burger Kutusu | 102×102×64 | 230 gsm karton | 500 (125x4) | [`hx-xbs01-kucuk-burger-kutusu`](hx-xbs01-kucuk-burger-kutusu) |
| HX-XBS02 | Orta Burger Kutusu | 112×114×72 | 270 gsm karton | 500 (125x4) | [`hx-xbs02-orta-burger-kutusu`](hx-xbs02-orta-burger-kutusu) |
| HX-XBS03 | Büyük Burger Kutusu | 151×141×78 | 300 gsm karton | 300 (150x2) | [`hx-xbs03-buyuk-burger-kutusu`](hx-xbs03-buyuk-burger-kutusu) |

#### Patates Kapları (2 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-XF01 | Küçük Patates Kabı | 93×38 / 77×35 × h110 | 230 gsm karton | 1000 (200x5) | [`hx-xf01-kucuk-patates-kabi`](hx-xf01-kucuk-patates-kabi) |
| HX-XF02 | Orta Patates Kabı | 100×40 / 73×33 × h153 | 250 gsm karton | 1000 (200x5) | [`hx-xf02-orta-patates-kabi`](hx-xf02-orta-patates-kabi) |

#### Mikro Oluklu Burger Kutuları (3 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-XC01 | Mikro Oluklu Burger Kutusu (S) | 102×102×64 | N dalga mikro oluklu mukavva (TL90/S85/MK110) | 200 (50x4) | [`hx-xc01-mikro-oluklu-burger-kutusu-s`](hx-xc01-mikro-oluklu-burger-kutusu-s) |
| HX-XC02 | Mikro Oluklu Burger Kutusu (M) | 112×114×72 | N dalga mikro oluklu mukavva (TL90/S85/MK110) | 200 (50x4) | [`hx-xc02-mikro-oluklu-burger-kutusu-m`](hx-xc02-mikro-oluklu-burger-kutusu-m) |
| HX-XC03 | Mikro Oluklu Burger Kutusu (L) | 195×110×78 | N dalga mikro oluklu mukavva (TL90/S85/MK110) | 250 (125x2) | [`hx-xc03-mikro-oluklu-burger-kutusu-l`](hx-xc03-mikro-oluklu-burger-kutusu-l) |

#### Taşıma Kutuları (6 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-XNO1 | Taşıma Kutusu No.1 | 130×105 / 113×90 × h65 | Karton; PE veya OPP astar seçenekli | 500 (100x5) | [`hx-xno1-tasima-kutusu-no-1`](hx-xno1-tasima-kutusu-no-1) |
| HX-XNO2 | Taşıma Kutusu No.2 | 140×103 / 195×140 × h50 | Karton; PE veya OPP astar seçenekli | 280 (70x4) | [`hx-xno2-tasima-kutusu-no-2`](hx-xno2-tasima-kutusu-no-2) |
| HX-XNO3 | Taşıma Kutusu No.3 | 140×103 / 140×103 × h76 | Karton; PE veya OPP astar seçenekli | 180 (45x4) | [`hx-xno3-tasima-kutusu-no-3`](hx-xno3-tasima-kutusu-no-3) |
| HX-XNO4 | Taşıma Kutusu No.4 | 188×147 / 113×90 × h90 | Karton; PE veya OPP astar seçenekli | 120 (30x4) | [`hx-xno4-tasima-kutusu-no-4`](hx-xno4-tasima-kutusu-no-4) |
| HX-XNO5 | Taşıma Kutusu No.5 | 151×120 / 151×120 × h146 | Karton; PE veya OPP astar seçenekli | 160 (40x4) | [`hx-xno5-tasima-kutusu-no-5`](hx-xno5-tasima-kutusu-no-5) |
| HX-XNO8 | Taşıma Kutusu No.8 | 140×110 / 140×110 × h70 | Karton; PE veya OPP astar seçenekli | 300 (50x6) | [`hx-xno8-tasima-kutusu-no-8`](hx-xno8-tasima-kutusu-no-8) |

#### Sokak Lezzeti Tepsileri (5 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-XTRAY1 | Sokak Lezzeti Tepsisi No.1 | 157×122,5 / 87×52,5 × h35 | Kraft karton; PE veya OPP astar seçenekli | 500 (125x4) | [`hx-xtray1-sokak-lezzeti-tepsisi-no-1`](hx-xtray1-sokak-lezzeti-tepsisi-no-1) |
| HX-XTRAY2 | Sokak Lezzeti Tepsisi No.2 | 196×149 / 114×67 × h41 | Kraft karton; PE veya OPP astar seçenekli | 500 (125x4) | [`hx-xtray2-sokak-lezzeti-tepsisi-no-2`](hx-xtray2-sokak-lezzeti-tepsisi-no-2) |
| HX-XTRAY3 | Sokak Lezzeti Tepsisi No.3 | 221×175 / 127×81 × h47 | Kraft karton; PE veya OPP astar seçenekli | 500 (125x4) | [`hx-xtray3-sokak-lezzeti-tepsisi-no-3`](hx-xtray3-sokak-lezzeti-tepsisi-no-3) |
| HX-XTRAY4 | Sokak Lezzeti Tepsisi No.4 | 240×190 / 130×80 × h55 | Kraft karton; PE veya OPP astar seçenekli | 500 (125x4) | [`hx-xtray4-sokak-lezzeti-tepsisi-no-4`](hx-xtray4-sokak-lezzeti-tepsisi-no-4) |
| HX-XTRAY5 | Sokak Lezzeti Tepsisi No.5 | 266×185 / 172×91 × h47 | Kraft karton; PE veya OPP astar seçenekli | 500 (125x4) | [`hx-xtray5-sokak-lezzeti-tepsisi-no-5`](hx-xtray5-sokak-lezzeti-tepsisi-no-5) |

#### Tavuk Kutuları ve Aile Kovası (4 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-FC0 | Tavuk Kutusu (S) | 144×84×54 | 230 gsm karton | 400 | [`hx-fc0-tavuk-kutusu-s`](hx-fc0-tavuk-kutusu-s) |
| HX-FC1 | Tavuk Kutusu (M) | 174×105×61 | 250 gsm karton | 300 | [`hx-fc1-tavuk-kutusu-m`](hx-fc1-tavuk-kutusu-m) |
| HX-FC3 | Tavuk Kutusu (L) | 218×116×73 | 270 gsm karton | 200 | [`hx-fc3-tavuk-kutusu-l`](hx-fc3-tavuk-kutusu-l) |
| HX-FC4 | Aile Kovası | 158×158×200 | 300 gsm karton | 100 | [`hx-fc4-aile-kovasi`](hx-fc4-aile-kovasi) |

#### Dürüm Kutuları (2 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-XW01 | Dürüm Kutusu (küçük) | 80×30 / 70×30 × h225 | Karton | 400 (100x4) | [`hx-xw01-durum-kutusu-kucuk`](hx-xw01-durum-kutusu-kucuk) |
| HX-XW02 | Dürüm Kutusu (büyük) | 125×30 / 115×30 × h225 | Karton | 500 (100x5) | [`hx-xw02-durum-kutusu-buyuk`](hx-xw02-durum-kutusu-buyuk) |

#### Pizza Kutuları (1 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-PIZZA | Pizza Kutusu (13 ölçü) | 127×127×45 – 470×470×50 | Oluklu mukavva | MOQ 2.800 – 14.000 adet (boya göre) | [`hx-pizza-pizza-kutusu`](hx-pizza-pizza-kutusu) |

#### Pasta Kutuları (1 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-PASTA | Pasta Kutusu (15 ölçü) | 14×14×5 – 32×32×8 cm | 250–285 gsm bristol karton | 50 (25x2) çember | [`hx-pasta-pasta-kutusu`](hx-pasta-pasta-kutusu) |

#### Yuvarlak Noodle Kutuları (2 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-NOODLE16 | 16 oz Noodle Kutusu (450 ml) | 78×87 / 80 × h94 | 280 gsm kraft & beyaz kağıt + PE laminasyon | 500 | [`hx-noodle16-16-oz-noodle-kutusu-450-ml`](hx-noodle16-16-oz-noodle-kutusu-450-ml) |
| HX-NOODLE26 | 26 oz Noodle Kutusu (750 ml) | 83×100 / 94 × h95 | 280 gsm kraft & beyaz kağıt + PE laminasyon | 500 | [`hx-noodle26-26-oz-noodle-kutusu-750-ml`](hx-noodle26-26-oz-noodle-kutusu-750-ml) |

#### Karton Kovalar (3 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-KOVA60 | 60 oz Karton Kova (1750 cc) | 150×125×132 | 250-300 gsm bristol + PE | 240 | [`hx-kova60-60-oz-karton-kova-1750-cc`](hx-kova60-60-oz-karton-kova-1750-cc) |
| HX-KOVA85 | 85 oz Karton Kova (2500 cc) | 193×145×147 | 250-300 gsm bristol + PE | 400 | [`hx-kova85-85-oz-karton-kova-2500-cc`](hx-kova85-85-oz-karton-kova-2500-cc) |
| HX-KOVA130 | 130 oz Karton Kova (4000 cc) | 211×160×170 | 250-300 gsm bristol + PE | 300 | [`hx-kova130-130-oz-karton-kova-4000-cc`](hx-kova130-130-oz-karton-kova-4000-cc) |

#### Karton Kaseler (5 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-XB016 | 16 oz Karton Kase | 111 | Karton | 10x50 - 500 | [`hx-xb016-16-oz-karton-kase`](hx-xb016-16-oz-karton-kase) |
| HX-XB020 | 20 oz Karton Kase | 145 | Karton | 10x50 - 500 | [`hx-xb020-20-oz-karton-kase`](hx-xb020-20-oz-karton-kase) |
| HX-XB026 | 26 oz Karton Kase | 145 | Karton | 10x50 - 500 | [`hx-xb026-26-oz-karton-kase`](hx-xb026-26-oz-karton-kase) |
| HX-XB032 | 32 oz Karton Kase | 187 | Karton | 6x50 - 300 | [`hx-xb032-32-oz-karton-kase`](hx-xb032-32-oz-karton-kase) |
| HX-XB038 | 38 oz Karton Kase | 187 | Karton | 6x50 - 300 | [`hx-xb038-38-oz-karton-kase`](hx-xb038-38-oz-karton-kase) |

#### Karton Bardaklar (11 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-SPX4 | Sıcak İçecek Bardağı 4 oz | Ø62,87 / Ø45,22 × 64,36 | Kağıt + PE | 1.000 | [`hx-spx4-sicak-icecek-bardagi-4-oz`](hx-spx4-sicak-icecek-bardagi-4-oz) |
| HX-SPX7 | Sıcak İçecek Bardağı 7 oz | Ø72,9 / Ø51,69 × 77 | Kağıt + PE | 2.000 | [`hx-spx7-sicak-icecek-bardagi-7-oz`](hx-spx7-sicak-icecek-bardagi-7-oz) |
| HX-SPX9T | Sıcak İçecek Bardağı 9T oz (Tall) | Ø80,3 / Ø51,51 × 95,25 | Kağıt + PE | 1.000 | [`hx-spx9t-sicak-icecek-bardagi-9t-oz-tall`](hx-spx9t-sicak-icecek-bardagi-9t-oz-tall) |
| HX-SPX9S | Sıcak İçecek Bardağı 9S oz (Squat) | Ø80,05 / Ø56,4 × 87,75 | Kağıt + PE | 1.000 | [`hx-spx9s-sicak-icecek-bardagi-9s-oz-squat`](hx-spx9s-sicak-icecek-bardagi-9s-oz-squat) |
| HX-SPX12 | Sıcak İçecek Bardağı 12 oz | — | Kağıt + PE | 1.000 | [`hx-spx12-sicak-icecek-bardagi-12-oz`](hx-spx12-sicak-icecek-bardagi-12-oz) |
| HX-SPX16 | Sıcak İçecek Bardağı 16 oz | — | Kağıt + PE | 1.000 | [`hx-spx16-sicak-icecek-bardagi-16-oz`](hx-spx16-sicak-icecek-bardagi-16-oz) |
| HX-SPX20 | Sıcak İçecek Bardağı 20 oz | — | Kağıt + PE | 600 | [`hx-spx20-sicak-icecek-bardagi-20-oz`](hx-spx20-sicak-icecek-bardagi-20-oz) |
| HX-DPX12 | Soğuk İçecek Bardağı 12 oz | — | PE + Kağıt + PE | 2.000 | [`hx-dpx12-soguk-icecek-bardagi-12-oz`](hx-dpx12-soguk-icecek-bardagi-12-oz) |
| HX-DPX16 | Soğuk İçecek Bardağı 16 oz | — | PE + Kağıt + PE | 1.000 | [`hx-dpx16-soguk-icecek-bardagi-16-oz`](hx-dpx16-soguk-icecek-bardagi-16-oz) |
| HX-DPX22 | Soğuk İçecek Bardağı 22 oz | — | PE + Kağıt + PE | 1.000 | [`hx-dpx22-soguk-icecek-bardagi-22-oz`](hx-dpx22-soguk-icecek-bardagi-22-oz) |
| HX-DPX32 | Soğuk İçecek Bardağı 32 oz | — | PE + Kağıt + PE | 500 | [`hx-dpx32-soguk-icecek-bardagi-32-oz`](hx-dpx32-soguk-icecek-bardagi-32-oz) |

#### Bardak Kılıfı ve Taşıyıcı (4 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-XPS8 | Bardak Kılıfı 8 oz | 241×75 | Oluklu karton | 1000 (100x10) | [`hx-xps8-bardak-kilifi-8-oz`](hx-xps8-bardak-kilifi-8-oz) |
| HX-XPS12-16 | Bardak Kılıfı 10-12-16 oz | 258×75 | Oluklu karton | 1000 (100x10) | [`hx-xps12-16-bardak-kilifi-10-12-16-oz`](hx-xps12-16-bardak-kilifi-10-12-16-oz) |
| HX-XCC02 | 2'li Bardak Taşıyıcı | — | Geri dönüştürülmüş kağıt hamuru | 428 | [`hx-xcc02-2-li-bardak-tasiyici`](hx-xcc02-2-li-bardak-tasiyici) |
| HX-XCC04 | 4'lü Bardak Taşıyıcı | — | Geri dönüştürülmüş kağıt hamuru | 210 | [`hx-xcc04-4-lu-bardak-tasiyici`](hx-xcc04-4-lu-bardak-tasiyici) |

### Kağıt çanta ve ambalaj kağıtları


#### Düz Saplı Kağıt Çantalar (1 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-CANTA-DUZ | Düz Saplı Kağıt Çanta (18 ölçü) | 18×10×33 – 46×16×46 cm | 70-80-90-100 gsm kraft / beyaz kağıt | MOQ 20.000 | [`hx-canta-duz-duz-sapli-kagit-canta`](hx-canta-duz-duz-sapli-kagit-canta) |

#### Burgu Saplı Kağıt Çantalar (2 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-CANTA-BURGU | Burgu Saplı Kağıt Çanta (flekso) (17 ölçü) | 18×8×23 – 54×14×50 cm | 70-80-90-100 gsm kraft / beyaz kağıt | MOQ 10.000 | [`hx-canta-burgu-burgu-sapli-kagit-canta-flekso`](hx-canta-burgu-burgu-sapli-kagit-canta-flekso) |
| HX-CANTA-BURGU-OFSET | Burgu Saplı Kağıt Çanta (ofset) (5 ölçü) | 22,5×8×23,5 – 34,7×14×40 cm | 100 gsm beyaz kağıt | MOQ 1.000 | [`hx-canta-burgu-ofset-burgu-sapli-kagit-canta-ofset`](hx-canta-burgu-ofset-burgu-sapli-kagit-canta-ofset) |

#### Sapsız Kağıt Torbalar (3 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-TORBA-DUZ | Yağlı Kağıt Torba (körüksüz) (14 ölçü) | 11×13,5 – 30×30,5 cm | 35–40 gsm greaseproof / sülfit / şamua kağıt | — | [`hx-torba-duz-yagli-kagit-torba-koruksuz`](hx-torba-duz-yagli-kagit-torba-koruksuz) |
| HX-TORBA-KORUK | Yağlı Kağıt Torba (körüklü) (7 ölçü) | 10×19×5 – 25,5×32×7 cm | 35–40 gsm greaseproof / sülfit / şamua kağıt | — | [`hx-torba-koruk-yagli-kagit-torba-koruklu`](hx-torba-koruk-yagli-kagit-torba-koruklu) |
| HX-SOS-TORBA | SOS Kraft Torba (3 ölçü) | 13,5×24×7 – 19×30×11 cm | 50 gsm kahve kraft | — | [`hx-sos-torba-sos-kraft-torba`](hx-sos-torba-sos-kraft-torba) |

#### Lüks Çantalar (2 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-LUKS-BEYAZ | Lüks Çanta (beyaz) (26 ölçü) | 8×6×18 – 55×12×38 cm | 210 / 250 / 300 gsm, mat veya parlak laminasyon | MOQ 250 | [`hx-luks-beyaz-luks-canta-beyaz`](hx-luks-beyaz-luks-canta-beyaz) |
| HX-LUKS-KAHVE | Lüks Çanta (kahve) (26 ölçü) | 8×6×18 – 55×12×38 cm | 200 gsm kahve | MOQ 250 | [`hx-luks-kahve-luks-canta-kahve`](hx-luks-kahve-luks-canta-kahve) |

#### Ambalaj Kağıdı ve Tepsi Kağıdı (2 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-AMBALAJ-KAGIDI | Ambalaj Kağıdı (burger sargısı) (7 ölçü) | 20×20 – 40×40 cm | 40 gsm (27 / 40 / 60 gsm seçenekli) | — | [`hx-ambalaj-kagidi-ambalaj-kagidi-burger-sargisi`](hx-ambalaj-kagidi-ambalaj-kagidi-burger-sargisi) |
| HX-TEPSI-KAGIDI | Tepsi Kağıdı (7 ölçü) | 20×20 – 40×40 cm | 70 gsm (40 / 70 / 80 / 90 gsm seçenekli) | — | [`hx-tepsi-kagidi-tepsi-kagidi`](hx-tepsi-kagidi-tepsi-kagidi) |

### Tamamlayıcı ürünler


#### Streç Film (2 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-STREC-MAKINE | Makine Tipi Streç Film (3 ölçü) | 500 mm × 2030–2880 m | LLDPE | — | [`hx-strec-makine-makine-tipi-strec-film`](hx-strec-makine-makine-tipi-strec-film) |
| HX-STREC-EL | El Tipi Streç Film (3 ölçü) | 500 mm × 270–300 m | LLDPE | — | [`hx-strec-el-el-tipi-strec-film`](hx-strec-el-el-tipi-strec-film) |

#### Menteşeli Sos Kapları (3 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-SOSKABI-1OZ | Menteşeli Sos Kabı 1 oz | — | PP, şeffaf | 1.000 | [`hx-soskabi-1oz-menteseli-sos-kabi-1-oz`](hx-soskabi-1oz-menteseli-sos-kabi-1-oz) |
| HX-SOSKABI-2OZ | Menteşeli Sos Kabı 2 oz | — | PP, şeffaf | 1.000 | [`hx-soskabi-2oz-menteseli-sos-kabi-2-oz`](hx-soskabi-2oz-menteseli-sos-kabi-2-oz) |
| HX-SOSKABI-4OZ | Menteşeli Sos Kabı 4 oz | — | PP, şeffaf | 500 | [`hx-soskabi-4oz-menteseli-sos-kabi-4-oz`](hx-soskabi-4oz-menteseli-sos-kabi-4-oz) |

#### Islak Mendil (1 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-ISLAK-MENDIL | Islak Mendil (10 ölçü) | 6×8 – 7×12 cm | PET/MET/PE, PET/ALU/PE, PAP/MET/PE veya PAP/ALU/PE poşet; nonwoven havlu | — | [`hx-islak-mendil-islak-mendil`](hx-islak-mendil-islak-mendil) |

#### Peçete ve Kağıt Havlu (6 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-PECETE | Peçete (6 ölçü) | — | %100 selüloz | — | [`hx-pecete-pecete`](hx-pecete-pecete) |
| HX-MAKINE-HAVLU | Otomatik makine havlusu (4 ölçü) | — | %100 selüloz | — | [`hx-makine-havlu-otomatik-makine-havlusu`](hx-makine-havlu-otomatik-makine-havlusu) |
| HX-TUVALET-KAGIDI | Tuvalet kağıdı | — | %100 selüloz | 24 | [`hx-tuvalet-kagidi-tuvalet-kagidi`](hx-tuvalet-kagidi-tuvalet-kagidi) |
| HX-DISP-PECETE | Dispenser peçete (2 ölçü) | — | %100 selüloz | — | [`hx-disp-pecete-dispenser-pecete`](hx-disp-pecete-dispenser-pecete) |
| HX-DISP-Z-PECETE | Dispenser Z peçete (2 ölçü) | — | %100 selüloz | — | [`hx-disp-z-pecete-dispenser-z-pecete`](hx-disp-z-pecete-dispenser-z-pecete) |
| HX-END-HAVLU | Endüstriyel havlu | — | %100 selüloz | 1 | [`hx-end-havlu-endustriyel-havlu`](hx-end-havlu-endustriyel-havlu) |

#### Fritöz Filtre Kağıdı (1 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-FILTRE-KAGIDI | Fritöz Filtre Kağıdı | 54×36 cm | nonwoven 50 gsm | 500 | [`hx-filtre-kagidi-fritoz-filtre-kagidi`](hx-filtre-kagidi-fritoz-filtre-kagidi) |

#### Limon Sosu (1 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-LIMON-SOS | Limon Sosu 500 ml | — | PET, şeffaf | 20 | [`hx-limon-sos-limon-sosu-500-ml`](hx-limon-sos-limon-sosu-500-ml) |

#### Ahşap Çatal Bıçak (4 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-KASIK | Ahşap Kaşık 13 cm | 13 cm | Huş ağacı | 2.000 | [`hx-kasik-ahsap-kasik-13-cm`](hx-kasik-ahsap-kasik-13-cm) |
| HX-CATAL | Ahşap Çatal 13 cm | 13 cm | Huş ağacı | 2.000 | [`hx-catal-ahsap-catal-13-cm`](hx-catal-ahsap-catal-13-cm) |
| HX-BICAK | Ahşap Bıçak 13 cm | 13 cm | Huş ağacı | 2.000 | [`hx-bicak-ahsap-bicak-13-cm`](hx-bicak-ahsap-bicak-13-cm) |
| HX-CATAL-BICAK-SET | Ahşap Çatal Bıçak Seti (9 ölçü) | 13 cm | Huş ağacı; kahve sülfit kağıt; 1 kat beyaz 11 gsm peçete | — | [`hx-catal-bicak-set-ahsap-catal-bicak-seti`](hx-catal-bicak-set-ahsap-catal-bicak-seti) |

#### Kızartma Yağı (1 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-KIZARTMA-YAGI | Kızartma Yağı 18 lt | — | Teneke | — | [`hx-kizartma-yagi-kizartma-yagi-18-lt`](hx-kizartma-yagi-kizartma-yagi-18-lt) |

---

## Doğrudan bağlantı (hotlink)

```
https://raw.githubusercontent.com/euplus/euplus-brand-assets/main/urunler/<klasör>/<klasör>.jpg
https://raw.githubusercontent.com/euplus/euplus-brand-assets/main/urunler/<klasör>/<klasör>.png
```

Örnek:

```
https://raw.githubusercontent.com/euplus/euplus-brand-assets/main/urunler/cp07-lumina-dikdortgen-kase/cp07-lumina-dikdortgen-kase.jpg
```
