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

## Fast food & restoran ambalajları — 79 ürün

Ölçü ve koli bilgileri [Fast Food & Restoran Ambalajları Kataloğu 2026](../katalog/EUPLUS-Fast-Food-Katalogu-2026.pdf) ile aynıdır.
Kaynak katalogdaki görseller kategori fotoğrafı ve mockup'tır; mockup'lardaki tedarikçi logosu kaldırıldı, PNG'ler opaktır.
Ölçü tablosu olan ürünler (pizza, pasta kutusu, çantalar, torbalar, kağıtlar, ıslak mendil, peçete, çatal-bıçak seti) tek ürün
olarak listelenir; standart ölçüler `urun.json` içindeki `varyantlar` alanında ve `ilan.md` tablosundadır. Kodlardaki `HX` öneki
kaynak kataloğu belirtir; ürünler EUPLUS markasıyla listelenir. Kaynaktaki gıda ürünleri (limon sosu, kızartma yağı) alınmadı.


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

#### Ahşap Çatal Bıçak (4 ürün)

| Kod | Ürün | Ölçü | Materyal | Koli içi / MOQ | Klasör |
|---|---|---|---|---|---|
| HX-KASIK | Ahşap Kaşık 13 cm | 13 cm | Huş ağacı | 2.000 | [`hx-kasik-ahsap-kasik-13-cm`](hx-kasik-ahsap-kasik-13-cm) |
| HX-CATAL | Ahşap Çatal 13 cm | 13 cm | Huş ağacı | 2.000 | [`hx-catal-ahsap-catal-13-cm`](hx-catal-ahsap-catal-13-cm) |
| HX-BICAK | Ahşap Bıçak 13 cm | 13 cm | Huş ağacı | 2.000 | [`hx-bicak-ahsap-bicak-13-cm`](hx-bicak-ahsap-bicak-13-cm) |
| HX-CATAL-BICAK-SET | Ahşap Çatal Bıçak Seti (9 ölçü) | 13 cm | Huş ağacı; kahve sülfit kağıt; 1 kat beyaz 11 gsm peçete | — | [`hx-catal-bicak-set-ahsap-catal-bicak-seti`](hx-catal-bicak-set-ahsap-catal-bicak-seti) |

---

## Gıda ambalajları (Bukap) — 342 ürün

Ölçü ve koli bilgileri [Gıda Ambalaj Kataloğu 2026](../katalog/EUPLUS-Gida-Ambalaj-Katalogu-2026.pdf) ile aynıdır.
Görseller kaynak katalogdaki gömülü ürün fotoğraflarından birebir çıkarıldı; PNG'ler şeffaftır. Kaynak PDF sıkıştırılmış olduğundan
fotoğrafların uzun kenarı 250–450 px'ti; 300 px altındaki 151 görsel Real-ESRGAN ile 4× büyütüldü ([`katalog/upscale.py`](../katalog/upscale.py)),
orijinaller `katalog/gorseller/orijinal/` altında saklanır.
Kodlar katalogdaki BKP kodlarıdır; CP kodlu çatal-kaşık-bıçak ve tabaklar `BK-CP…`, katalogda aynı kodu paylaşan ikinci ürünler `-2` alır
(ayrıntı: [`kaynaklar/bukap/tedarikci.json`](../kaynaklar/bukap/tedarikci.json)).

Karton bardaklar ve kapakları, kraft çantalar ve çorba kaseleri (24 ürün) PDF katalogda **yer almaz**; bu ürünler burada
ve CSV'de durur (`urun.json` → `pdf_katalogda: false`).


### Pastane & Kafe Kapları (75 ürün)

#### Paketleme Kapları (15 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP6440 | 70x75 Silindir Kutu | 70×75 | 100 cc | PET | 570 | [`bkp6440-70x75-silindir-kutu`](bkp6440-70x75-silindir-kutu) |
| BKP6445 | 70x100 Silindir Kutu | 70×100 | 150 cc | PET | 471 | [`bkp6445-70x100-silindir-kutu`](bkp6445-70x100-silindir-kutu) |
| BKP6465 | 70x190 Silindir Kutu | 70×190 | 200 cc | PET | 252 | [`bkp6465-70x190-silindir-kutu`](bkp6465-70x190-silindir-kutu) |
| BK-ACIBADEM | Tekli Acıbadem Kabı | 110×110×40 | — | PET | 1000 | [`bk-acibadem-tekli-acibadem-kabi`](bk-acibadem-tekli-acibadem-kabi) |
| BKP6480 | 130x120 Konik Kutu | 130×120×85 | 200 cc | PET | 140 | [`bkp6480-130x120-konik-kutu`](bkp6480-130x120-konik-kutu) |
| BKP6470 | 70x300 Silindir Kutu | 70×300 | 290 cc | PET | 150 | [`bkp6470-70x300-silindir-kutu`](bkp6470-70x300-silindir-kutu) |
| BKP6445-G | 70x100 Silindir Kutu Gold | 70×100 | 150 cc | PET | 471 | [`bkp6445-g-70x100-silindir-kutu-gold`](bkp6445-g-70x100-silindir-kutu-gold) |
| BKP6465-G | 70x190 Silindir Kutu Gold | 70×190 | 200 cc | PET | 252 | [`bkp6465-g-70x190-silindir-kutu-gold`](bkp6465-g-70x190-silindir-kutu-gold) |
| BKP6470-G | 70x300 Silindir Kutu Gold | 70×300 | 290 cc | PET | 150 | [`bkp6470-g-70x300-silindir-kutu-gold`](bkp6470-g-70x300-silindir-kutu-gold) |
| BKP6610 | 6x18 OPP Poşet | 6×18×4×4 | 100 cc | OPP | 5000 | [`bkp6610-6x18-opp-poset`](bkp6610-6x18-opp-poset) |
| BKP6615 | 7,5x19 OPP Poşet | 7,5×19×4,5×4,5 | 150 cc | OPP | 4000 | [`bkp6615-7-5x19-opp-poset`](bkp6615-7-5x19-opp-poset) |
| BKP6620 | 7,5x21 OPP Poşet | 7,5×21×4,5×4,5 | 150 cc | OPP | 4000 | [`bkp6620-7-5x21-opp-poset`](bkp6620-7-5x21-opp-poset) |
| BKP6630 | 8x28 OPP Poşet | 8×28×5×5 | 200 cc | OPP | 3000 | [`bkp6630-8x28-opp-poset`](bkp6630-8x28-opp-poset) |
| BKP6630-G | 8x28 OPP Poşet Baskılı | 8×28×5×5 | 200 cc | OPP | 3000 | [`bkp6630-g-8x28-opp-poset-baskili`](bkp6630-g-8x28-opp-poset-baskili) |
| BKP6640 | 10x31 OPP Poşet | 10×31×7×7 | 250 cc | OPP | 2000 | [`bkp6640-10x31-opp-poset`](bkp6640-10x31-opp-poset) |

#### Pasta ve Kek Kapları (22 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP805 | Kubbe Kapaklı Pasta Kabı H60 | 210×140×60 | — | PET | 300 | [`bkp805-kubbe-kapakli-pasta-kabi-h60`](bkp805-kubbe-kapakli-pasta-kabi-h60) |
| BKP810 | Kubbe Kapaklı Pasta Kabı H80 | 210×140×80 | 700 cc | PET | 150 | [`bkp810-kubbe-kapakli-pasta-kabi-h80`](bkp810-kubbe-kapakli-pasta-kabi-h80) |
| BKP815 | Kubbe Kapaklı Pasta Kabı H100 | 210×140×100 | 800 cc | PET | 150 | [`bkp815-kubbe-kapakli-pasta-kabi-h100`](bkp815-kubbe-kapakli-pasta-kabi-h100) |
| BKP825 | Baton Kek Kabı H60 | 135×200×60 | — | PP | 500 | [`bkp825-baton-kek-kabi-h60`](bkp825-baton-kek-kabi-h60) |
| BKP830 | Baton Kek Kabı H70 | 135×200×70 | — | PP | 500 | [`bkp830-baton-kek-kabi-h70`](bkp830-baton-kek-kabi-h70) |
| BKP6810 | Üçgen Kek Kabı Gold | 120×155×55 | — | PET | 200 | [`bkp6810-ucgen-kek-kabi-gold`](bkp6810-ucgen-kek-kabi-gold) |
| BKP140 | Üçgen Kek Kabı Kendinden Kapaklı | 100×175×55 | — | PET | 500 | [`bkp140-ucgen-kek-kabi-kendinden-kapakli`](bkp140-ucgen-kek-kabi-kendinden-kapakli) |
| BKP6820 | Üçgen Kek Kabı Siyah | 120×155×55 | — | PET | 200 | [`bkp6820-ucgen-kek-kabi-siyah`](bkp6820-ucgen-kek-kabi-siyah) |
| BKP6850 | 4'lü Baklava Kabı | 105×105×50 | — | PP | 1050 | [`bkp6850-4-lu-baklava-kabi`](bkp6850-4-lu-baklava-kabi) |
| BKP6860-6870 | 12x12 Kare Pasta Kabı | 120×120×90 | — | PET | 200 | [`bkp6860-6870-12x12-kare-pasta-kabi`](bkp6860-6870-12x12-kare-pasta-kabi) |
| BKP6200-6240 | Dikdörtgen Kapaklı Kase 500 cc | 130×210×60 | 500 cc | PET | 500 | [`bkp6200-6240-dikdortgen-kapakli-kase-500-cc`](bkp6200-6240-dikdortgen-kapakli-kase-500-cc) |
| BKP6220-6240 | Dikdörtgen Kapaklı Kase 1000 cc | 130×210×80 | 1000 cc | PET | 500 | [`bkp6220-6240-dikdortgen-kapakli-kase-1000-cc`](bkp6220-6240-dikdortgen-kapakli-kase-1000-cc) |
| BKP6120 | Sekizgen 4 Bölmeli Kap | 230×230×45 | — | PET | 175 | [`bkp6120-sekizgen-4-bolmeli-kap`](bkp6120-sekizgen-4-bolmeli-kap) |
| BKP6115 | Sekizgen Bölmesiz Kap | 230×230×40 | — | PET | 175 | [`bkp6115-sekizgen-bolmesiz-kap`](bkp6115-sekizgen-bolmesiz-kap) |
| BKP6300 | Menteşeli Dikdörtgen Kap STK250 | 115×170×40 | 250 cc | PET | 500 | [`bkp6300-menteseli-dikdortgen-kap-stk250`](bkp6300-menteseli-dikdortgen-kap-stk250) |
| BKP6310 | Menteşeli Dikdörtgen Kap STK375 | 304×203×32 | 375 cc | PET | 400 | [`bkp6310-menteseli-dikdortgen-kap-stk375`](bkp6310-menteseli-dikdortgen-kap-stk375) |
| BKP6320 | Menteşeli Dikdörtgen Kap STK500 | 150×200×45 | 500 cc | PET | 250 | [`bkp6320-menteseli-dikdortgen-kap-stk500`](bkp6320-menteseli-dikdortgen-kap-stk500) |
| BKP6330 | Menteşeli Dikdörtgen Kap STK750 | 180×240×40 | 750 cc | PET | 200 | [`bkp6330-menteseli-dikdortgen-kap-stk750`](bkp6330-menteseli-dikdortgen-kap-stk750) |
| BKP6340 | Menteşeli Dikdörtgen Kap STK1000 | 200×280×45 | 1000 cc | PET | 200 | [`bkp6340-menteseli-dikdortgen-kap-stk1000`](bkp6340-menteseli-dikdortgen-kap-stk1000) |
| BK-4BK1000 | 4 Bölmeli Kap 1000 cc | 314×445×32 | 1000 cc | PET | 150 | [`bk-4bk1000-4-bolmeli-kap-1000-cc`](bk-4bk1000-4-bolmeli-kap-1000-cc) |
| BKP250 | Sızdırmaz Baklava Kabı MF31 500 cc | 160×255×40 | 500 cc | PET | 400 | [`bkp250-sizdirmaz-baklava-kabi-mf31-500-cc`](bkp250-sizdirmaz-baklava-kabi-mf31-500-cc) |
| BKP260 | Sızdırmaz Baklava Kabı MF31 1000 cc | 215×290×40 | 1000 cc | PET | 200 | [`bkp260-sizdirmaz-baklava-kabi-mf31-1000-cc`](bkp260-sizdirmaz-baklava-kabi-mf31-1000-cc) |

#### Makaron Kapları (8 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP6755 | 2'li Macaron Kutusu | 50×50×66 | 50 cc | PET | 470 | [`bkp6755-2-li-macaron-kutusu`](bkp6755-2-li-macaron-kutusu) |
| BKP6760 | 4'lü Macaron Kutusu | 50×50×134 | 120 cc | PET | 360 | [`bkp6760-4-lu-macaron-kutusu`](bkp6760-4-lu-macaron-kutusu) |
| BKP6765 | 6'lı Macaron Kutusu | 50×50×200 | 200 cc | PET | 240 | [`bkp6765-6-li-macaron-kutusu`](bkp6765-6-li-macaron-kutusu) |
| BKP6670 | 6'lı Yatay Macaron Kutusu Gold | 195×50×45 | 200 cc | PET | 500 | [`bkp6670-6-li-yatay-macaron-kutusu-gold`](bkp6670-6-li-yatay-macaron-kutusu-gold) |
| BKP6680 | 12'li Yatay Macaron Kutusu Gold | 195×100×45 | 400 cc | PET | 500 | [`bkp6680-12-li-yatay-macaron-kutusu-gold`](bkp6680-12-li-yatay-macaron-kutusu-gold) |
| BKP6685 | 24'lü Yatay Macaron Kutusu Gold | 195×200×45 | 400 cc | PET | 200 | [`bkp6685-24-lu-yatay-macaron-kutusu-gold`](bkp6685-24-lu-yatay-macaron-kutusu-gold) |
| BKP6790 | 27'li Yatay Macaron Kutusu Siyah | 160×290×50 | 750 cc | PET | 300 | [`bkp6790-27-li-yatay-macaron-kutusu-siyah`](bkp6790-27-li-yatay-macaron-kutusu-siyah) |
| BKP6689 | 7'li Yuvarlak Macaron Kutusu Siyah | 160×60 | 400 cc | PET | 360 | [`bkp6689-7-li-yuvarlak-macaron-kutusu-siyah`](bkp6689-7-li-yuvarlak-macaron-kutusu-siyah) |

#### Dondurma Kapları (16 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP1460 | Dondurma Kabı Beyaz 250 cc | 140×100×55 | 250 cc | PS | 1500 | [`bkp1460-dondurma-kabi-beyaz-250-cc`](bkp1460-dondurma-kabi-beyaz-250-cc) |
| BKP1470 | Dondurma Bombe Kapağı 250 cc | 140×100×40 | — | PET | 1500 | [`bkp1470-dondurma-bombe-kapagi-250-cc`](bkp1470-dondurma-bombe-kapagi-250-cc) |
| BKP1480 | Dondurma Kabı Beyaz 500 cc | 210×100×65 | 500 cc | PS | 500 | [`bkp1480-dondurma-kabi-beyaz-500-cc`](bkp1480-dondurma-kabi-beyaz-500-cc) |
| BKP1490 | Dondurma Kabı Beyaz 1000 cc | 210×100×85 | 1000 cc | PS | 500 | [`bkp1490-dondurma-kabi-beyaz-1000-cc`](bkp1490-dondurma-kabi-beyaz-1000-cc) |
| BKP1510 | Dondurma Bombe Kapağı 500-1000 cc | 210×120×40 | — | PET | 500 | [`bkp1510-dondurma-bombe-kapagi-500-1000-cc`](bkp1510-dondurma-bombe-kapagi-500-1000-cc) |
| BKP770-B | Dikdörtgen Kase Beyaz 500 cc | 130×200×55 | 500 cc | PET | 500 | [`bkp770-b-dikdortgen-kase-beyaz-500-cc`](bkp770-b-dikdortgen-kase-beyaz-500-cc) |
| BKP770 | Dikdörtgen Kase 500 cc | 205×135×55 | 500 cc | PET | 500 | [`bkp770-dikdortgen-kase-500-cc`](bkp770-dikdortgen-kase-500-cc) |
| BKP775 | Dikdörtgen Kase 750 cc | 205×135×65 | 750 cc | PET | 500 | [`bkp775-dikdortgen-kase-750-cc`](bkp775-dikdortgen-kase-750-cc) |
| BKP780 | Dikdörtgen Kase 1000 cc | 205×135×70 | 1000 cc | PET | 500 | [`bkp780-dikdortgen-kase-1000-cc`](bkp780-dikdortgen-kase-1000-cc) |
| BKP795-D | Dikdörtgen Kase Düz Kapağı | 140×210×10 | — | PET | 500 | [`bkp795-d-dikdortgen-kase-duz-kapagi`](bkp795-d-dikdortgen-kase-duz-kapagi) |
| BKP790-B | Dikdörtgen Kase Bombe Kapağı | 140×210×35 | — | PET | 500 | [`bkp790-b-dikdortgen-kase-bombe-kapagi`](bkp790-b-dikdortgen-kase-bombe-kapagi) |
| BKP1410 | Kapaklı Dondurma Kasesi 100 cc | 80×80×50 | 100 cc | PP | 2000 | [`bkp1410-kapakli-dondurma-kasesi-100-cc`](bkp1410-kapakli-dondurma-kasesi-100-cc) |
| BKP1420 | Kapaklı Dondurma Kasesi 200 cc | 95×95×55 | 200 cc | PP | 1000 | [`bkp1420-kapakli-dondurma-kasesi-200-cc`](bkp1420-kapakli-dondurma-kasesi-200-cc) |
| BKP1520 | Strafor Dondurma Kabı 500 cc | 210×130×100 | 500 cc | PS (strafor) | 60 | [`bkp1520-strafor-dondurma-kabi-500-cc`](bkp1520-strafor-dondurma-kabi-500-cc) |
| BKP1530 | Strafor Dondurma Kabı 1000 cc | 260×150×110 | 1000 cc | PS (strafor) | 60 | [`bkp1530-strafor-dondurma-kabi-1000-cc`](bkp1530-strafor-dondurma-kabi-1000-cc) |
| BKP1540 | Dondurma Küveti 5 lt | 340×150×130 | 5000 cc | PS | 120 | [`bkp1540-dondurma-kuveti-5-lt`](bkp1540-dondurma-kuveti-5-lt) |

#### Sızdırmaz Kaplar (14 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP10 | Sızdırmaz Kap 150 cc | 110×110×25 | 150 cc | PET | 1000 | [`bkp10-sizdirmaz-kap-150-cc`](bkp10-sizdirmaz-kap-150-cc) |
| BKP20 | Sızdırmaz Kap 250 cc | 110×110×40 | 250 cc | PET | 1000 | [`bkp20-sizdirmaz-kap-250-cc`](bkp20-sizdirmaz-kap-250-cc) |
| BKP30 | Sızdırmaz Kap 375 cc | 110×110×55 | 375 cc | PET | 1000 | [`bkp30-sizdirmaz-kap-375-cc`](bkp30-sizdirmaz-kap-375-cc) |
| BKP50 | Sızdırmaz Kap Düz-Yüksek 750 cc | 130×190×55-80 | 750 cc | PET | 600 | [`bkp50-sizdirmaz-kap-duz-yuksek-750-cc`](bkp50-sizdirmaz-kap-duz-yuksek-750-cc) |
| BKP40 | Sızdırmaz Kap 500 cc | 125×125×60 | 500 cc | PET | 1000 | [`bkp40-sizdirmaz-kap-500-cc`](bkp40-sizdirmaz-kap-500-cc) |
| BKP60 | Sızdırmaz Kap Düz-Yüksek 1000 cc | 130×190×70-90 | 1000 cc | PET | 600 | [`bkp60-sizdirmaz-kap-duz-yuksek-1000-cc`](bkp60-sizdirmaz-kap-duz-yuksek-1000-cc) |
| BKP735 | Sızdırmaz Yayvan Kap 1000 cc | 210×160×80 | 1000 cc | PET | 400 | [`bkp735-sizdirmaz-yayvan-kap-1000-cc`](bkp735-sizdirmaz-yayvan-kap-1000-cc) |
| BKP1160 | Kazandibi Kabı 250 cc | 100×150×40 | 250 cc | PET | 400 | [`bkp1160-kazandibi-kabi-250-cc`](bkp1160-kazandibi-kabi-250-cc) |
| BKP130 | Düz Kapaklı Peynir Kabı 500 cc | 100×150×50 | 500 cc | PET | 800 | [`bkp130-duz-kapakli-peynir-kabi-500-cc`](bkp130-duz-kapakli-peynir-kabi-500-cc) |
| BKP130-2 | Sızdırmaz Peynir Kabı 500 cc | 100×150×85 | 500 cc | PET | 800 | [`bkp130-2-sizdirmaz-peynir-kabi-500-cc`](bkp130-2-sizdirmaz-peynir-kabi-500-cc) |
| BKP150 | Üçgen Peynir Kabı 600 cc | 220×170×75 | 600 cc | PET | 300 | [`bkp150-ucgen-peynir-kabi-600-cc`](bkp150-ucgen-peynir-kabi-600-cc) |
| BKP70 | Sızdırmaz Kap Düz-Yüksek 1250 cc | 220×170×50-90 | 1250 cc | PET | 200 | [`bkp70-sizdirmaz-kap-duz-yuksek-1250-cc`](bkp70-sizdirmaz-kap-duz-yuksek-1250-cc) |
| BKP90 | Sızdırmaz Kap Düz-Yüksek 1500 cc | 220×170×70-110 | 1500 cc | PET | 200 | [`bkp90-sizdirmaz-kap-duz-yuksek-1500-cc`](bkp90-sizdirmaz-kap-duz-yuksek-1500-cc) |
| BKP110 | Sızdırmaz Kap Düz-Yüksek 2000 cc | 220×170×80-120 | 2000 cc | PET | 200 | [`bkp110-sizdirmaz-kap-duz-yuksek-2000-cc`](bkp110-sizdirmaz-kap-duz-yuksek-2000-cc) |


### Kurabiye ve Genel Gıda Kapları (40 ürün)

#### Kurabiye Kapları (20 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BK-KK200-A | Kurabiye Kabı 200 cc (A) | 115×215×35 | 200 cc | PET | 400 | [`bk-kk200-a-kurabiye-kabi-200-cc-a`](bk-kk200-a-kurabiye-kabi-200-cc-a) |
| BK-KK200-B | Kurabiye Kabı 200 cc (B) | 115×215×35 | 200 cc | PET | 400 | [`bk-kk200-b-kurabiye-kabi-200-cc-b`](bk-kk200-b-kurabiye-kabi-200-cc-b) |
| BK-KK250 | Kurabiye Kabı 250 cc | 115×215×45 | 250 cc | PET | 400 | [`bk-kk250-kurabiye-kabi-250-cc`](bk-kk250-kurabiye-kabi-250-cc) |
| BKP6950 | Kurabiye Kabı 1000 cc | 193×125×70 | 1000 cc | PET | 400 | [`bkp6950-kurabiye-kabi-1000-cc`](bkp6950-kurabiye-kabi-1000-cc) |
| BKP690 | 25x25 Kurabiye Kabı 350 cc | 202×135×50 | 350 cc | PET | 400 | [`bkp690-25x25-kurabiye-kabi-350-cc`](bkp690-25x25-kurabiye-kabi-350-cc) |
| BKP695 | 25x25 Kurabiye Kabı 400 cc | 202×135×55 | 400 cc | PET | 400 | [`bkp695-25x25-kurabiye-kabi-400-cc`](bkp695-25x25-kurabiye-kabi-400-cc) |
| BKP6920 | 35x20 Kurabiye Kabı 350 cc | 202×135×55 | 350 cc | PET | 400 | [`bkp6920-35x20-kurabiye-kabi-350-cc`](bkp6920-35x20-kurabiye-kabi-350-cc) |
| BKP6930 | 40x20 Kurabiye Kabı 400 cc | 202×135×60 | 400 cc | PET | 500 | [`bkp6930-40x20-kurabiye-kabi-400-cc`](bkp6930-40x20-kurabiye-kabi-400-cc) |
| BKP600 | Oval Sızdırmaz Kap 150 cc | 130×105×25 | 150 cc | PET | 1000 | [`bkp600-oval-sizdirmaz-kap-150-cc`](bkp600-oval-sizdirmaz-kap-150-cc) |
| BKP610 | Oval Sızdırmaz Kap 250 cc | 130×105×40 | 250 cc | PET | 1000 | [`bkp610-oval-sizdirmaz-kap-250-cc`](bkp610-oval-sizdirmaz-kap-250-cc) |
| BKP620 | Oval Sızdırmaz Kap 375 cc | 130×105×55 | 375 cc | PET | 1000 | [`bkp620-oval-sizdirmaz-kap-375-cc`](bkp620-oval-sizdirmaz-kap-375-cc) |
| BKP630 | Oval Sızdırmaz Kap 500 cc | 190×140×40 | 500 cc | PET | 800 | [`bkp630-oval-sizdirmaz-kap-500-cc`](bkp630-oval-sizdirmaz-kap-500-cc) |
| BKP640 | Oval Sızdırmaz Kap 750 cc | 190×140×60 | 750 cc | PET | 600 | [`bkp640-oval-sizdirmaz-kap-750-cc`](bkp640-oval-sizdirmaz-kap-750-cc) |
| BKP650 | Oval Sızdırmaz Kap 1000 cc | 190×140×80 | 1000 cc | PET | 600 | [`bkp650-oval-sizdirmaz-kap-1000-cc`](bkp650-oval-sizdirmaz-kap-1000-cc) |
| BKP6160-XS | Sushi Kabı XS | 170×90×45 | — | PET | 200 | [`bkp6160-xs-sushi-kabi-xs`](bkp6160-xs-sushi-kabi-xs) |
| BKP6170-S | Sushi Kabı S | 160×110×45 | — | PET | 200 | [`bkp6170-s-sushi-kabi-s`](bkp6170-s-sushi-kabi-s) |
| BKP6180-M | Sushi Kabı M | 210×85×45 | — | PET | 200 | [`bkp6180-m-sushi-kabi-m`](bkp6180-m-sushi-kabi-m) |
| BKP6190-L | Sushi Kabı L | 215×135×45 | — | PET | 200 | [`bkp6190-l-sushi-kabi-l`](bkp6190-l-sushi-kabi-l) |
| BKP6730-CP12K | Yuvarlak Bombe Kapaklı Kase 220 cc | 116×70 | 220 cc | PET | 1000 | [`bkp6730-cp12k-yuvarlak-bombe-kapakli-kase-220-cc`](bkp6730-cp12k-yuvarlak-bombe-kapakli-kase-220-cc) |
| BKP6710-6720 | Kare Kase 220 cc | 110×110×40 | 220 cc | PET | 1000 | [`bkp6710-6720-kare-kase-220-cc`](bkp6710-6720-kare-kase-220-cc) |

#### PP Köşeli Kaseler (3 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP1110 | Köşeli Kase Kapaksız 250 cc | 140×105×40 | 250 cc | PP | 1800 | [`bkp1110-koseli-kase-kapaksiz-250-cc`](bkp1110-koseli-kase-kapaksiz-250-cc) |
| BKP1120 | Köşeli Kase Kapaksız 500 cc | 200×105×40 | 500 cc | PP | 1200 | [`bkp1120-koseli-kase-kapaksiz-500-cc`](bkp1120-koseli-kase-kapaksiz-500-cc) |
| BKP1130 | Köşeli Kase Kapaksız 1000 cc | 200×105×62 | 1000 cc | PP | 1200 | [`bkp1130-koseli-kase-kapaksiz-1000-cc`](bkp1130-koseli-kase-kapaksiz-1000-cc) |

#### Kaymak Kapları (2 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP160 | Kaymak Kabı Federli | 140×100×35 | 250 cc | PET | 800 | [`bkp160-kaymak-kabi-federli`](bkp160-kaymak-kabi-federli) |
| BKP1460-2 | Kaymak Kabı Beyaz | 135×95×25 | 250 cc | PP | 1500 | [`bkp1460-2-kaymak-kabi-beyaz`](bkp1460-2-kaymak-kabi-beyaz) |

#### PP Yuvarlak Kaseler (8 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP1820 | PP Yuvarlak Vakumlu Kase 350 cc | 116×92×51 | 350 cc | PP | 1000 | [`bkp1820-pp-yuvarlak-vakumlu-kase-350-cc`](bkp1820-pp-yuvarlak-vakumlu-kase-350-cc) |
| BKP1830 | PP Yuvarlak Vakumlu Kase 500 cc | 116×84×75 | 500 cc | PP | 1000 | [`bkp1830-pp-yuvarlak-vakumlu-kase-500-cc`](bkp1830-pp-yuvarlak-vakumlu-kase-500-cc) |
| BKP1810 | PP Yuvarlak Vakumlu Kase 250 cc | 116×92×44 | 250 cc | PP | 1000 | [`bkp1810-pp-yuvarlak-vakumlu-kase-250-cc`](bkp1810-pp-yuvarlak-vakumlu-kase-250-cc) |
| BKP1840 | PP Yuvarlak Vakumlu Kase 750 cc | 116×87×105 | 750 cc | PP | 1000 | [`bkp1840-pp-yuvarlak-vakumlu-kase-750-cc`](bkp1840-pp-yuvarlak-vakumlu-kase-750-cc) |
| BKP1850 | PP Yuvarlak Vakumlu Kase 1000 cc | 116×83×138 | 1000 cc | PP | 500 | [`bkp1850-pp-yuvarlak-vakumlu-kase-1000-cc`](bkp1850-pp-yuvarlak-vakumlu-kase-1000-cc) |
| BKP1140 | Sup Kase 150 cc | 100×80×30 | 150 cc | PP | 2000 | [`bkp1140-sup-kase-150-cc`](bkp1140-sup-kase-150-cc) |
| BKP1150 | Sup Kase Beyaz 200 cc | 100×77×40 | 200 cc | PP | 2000 | [`bkp1150-sup-kase-beyaz-200-cc`](bkp1150-sup-kase-beyaz-200-cc) |
| BKP1170 | Sup Kase 250 cc | 100×77×50 | 250 cc | PP | 2000 | [`bkp1170-sup-kase-250-cc`](bkp1170-sup-kase-250-cc) |

#### Helva Kapları (3 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP885 | Helva Kabı 400 cc | 170×170×30 | 400 cc | PET | 450 | [`bkp885-helva-kabi-400-cc`](bkp885-helva-kabi-400-cc) |
| BKP886 | Helva Kabı 750 cc | 170×170×43 | 750 cc | PET | 450 | [`bkp886-helva-kabi-750-cc`](bkp886-helva-kabi-750-cc) |
| BKP887 | Helva Kabı Siyah 1000 cc | 170×170×57 | 1000 cc | PET | 450 | [`bkp887-helva-kabi-siyah-1000-cc`](bkp887-helva-kabi-siyah-1000-cc) |

#### Yumurta Viyolleri (4 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP410 | Bıldırcın Yumurta Viyolü | 100×125×40 | — | PET | 800 | [`bkp410-bildircin-yumurta-viyolu`](bkp410-bildircin-yumurta-viyolu) |
| BKP430 | 6x2 Yumurta Viyolü | 295×100×73 | — | PET | 400 | [`bkp430-6x2-yumurta-viyolu`](bkp430-6x2-yumurta-viyolu) |
| BKP420 | 10'lu Yumurta Viyolü | 240×100×73 | — | PET | 400 | [`bkp420-10-lu-yumurta-viyolu`](bkp420-10-lu-yumurta-viyolu) |
| BKP440 | 15'li Yumurta Viyolü | 245×100×73 | — | PET | 400 | [`bkp440-15-li-yumurta-viyolu`](bkp440-15-li-yumurta-viyolu) |


### İçecek Bardakları ve Şişeler (39 ürün)

#### Soğuk İçecek Bardakları (8 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP9110 | PET Bardak 8 oz | 95×60 | 250 cc | PET | 1000 | [`bkp9110-pet-bardak-8-oz`](bkp9110-pet-bardak-8-oz) |
| BKP9120 | PET Bardak 10 oz | 95×60×95 | 300 cc | PET | 1000 | [`bkp9120-pet-bardak-10-oz`](bkp9120-pet-bardak-10-oz) |
| BKP9130 | PET Bardak 12 oz | 95×60×110 | 350 cc | PET | 1000 | [`bkp9130-pet-bardak-12-oz`](bkp9130-pet-bardak-12-oz) |
| BKP9140 | PET Bardak 14 oz | 95×60×120 | 450 cc | PET | 1000 | [`bkp9140-pet-bardak-14-oz`](bkp9140-pet-bardak-14-oz) |
| BKP9150 | PET Bardak 16 oz | 95×60×130 | 550 cc | PET | 1000 | [`bkp9150-pet-bardak-16-oz`](bkp9150-pet-bardak-16-oz) |
| BKP9210 | PET Bardak Dome Kapağı | 95×95×40 | — | PET | 1000 | [`bkp9210-pet-bardak-dome-kapagi`](bkp9210-pet-bardak-dome-kapagi) |
| BKP9220 | PET Bardak Klipsli Kapak | 95×95×15 | — | PET | 1000 | [`bkp9220-pet-bardak-klipsli-kapak`](bkp9220-pet-bardak-klipsli-kapak) |
| BKP9230 | PET Bardak Artı Kesimli Kapak | 95×95×10 | — | PET | 1000 | [`bkp9230-pet-bardak-arti-kesimli-kapak`](bkp9230-pet-bardak-arti-kesimli-kapak) |

#### Plastik Şişeler (10 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP10305 | PET Şişe 200 cc | 50×50×150 | 200 cc | PET | 250 | [`bkp10305-pet-sise-200-cc`](bkp10305-pet-sise-200-cc) |
| BKP10310 | PET Şişe 250 cc | 52×52×150 | 250 cc | PET | 250 | [`bkp10310-pet-sise-250-cc`](bkp10310-pet-sise-250-cc) |
| BKP10315 | PET Şişe 330 cc | 57×57×165 | 330 cc | PET | 200 | [`bkp10315-pet-sise-330-cc`](bkp10315-pet-sise-330-cc) |
| BKP10320 | PET Şişe 400 cc | 58×58×185 | 400 cc | PET | 150 | [`bkp10320-pet-sise-400-cc`](bkp10320-pet-sise-400-cc) |
| BKP10325 | PET Şişe 500 cc | 63×63×205 | 500 cc | PET | 120 | [`bkp10325-pet-sise-500-cc`](bkp10325-pet-sise-500-cc) |
| BKP10330 | PET Şişe 1000 cc | 78×78×255 | 1000 cc | PET | 60 | [`bkp10330-pet-sise-1000-cc`](bkp10330-pet-sise-1000-cc) |
| BKP10340 | PET Kare Şişe 250 cc | Ø38 | 250 cc | PET | 250 | [`bkp10340-pet-kare-sise-250-cc`](bkp10340-pet-kare-sise-250-cc) |
| BKP10330-2 | PET Kare Şişe 300 cc | Ø38 | 300 cc | PET | 250 | [`bkp10330-2-pet-kare-sise-300-cc`](bkp10330-2-pet-kare-sise-300-cc) |
| BKP10360 | PET Kare Şişe 330 cc | Ø38 | 330 cc | PET | 200 | [`bkp10360-pet-kare-sise-330-cc`](bkp10360-pet-kare-sise-330-cc) |
| BKP10370 | PET Kare Şişe 500 cc | Ø38 | 500 cc | PET | 200 | [`bkp10370-pet-kare-sise-500-cc`](bkp10370-pet-kare-sise-500-cc) |

#### Karton Bardaklar (17 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP9505 | Baskılı Double Wall Karton Bardak 8 oz | 80×58×94 | 250 cc | Karton | 1000 | [`bkp9505-baskili-double-wall-karton-bardak-8-oz`](bkp9505-baskili-double-wall-karton-bardak-8-oz) |
| BKP9530 | Baskılı Double Wall Karton Bardak 14 oz | 90×59×110 | 400 cc | Karton | 1000 | [`bkp9530-baskili-double-wall-karton-bardak-14-oz`](bkp9530-baskili-double-wall-karton-bardak-14-oz) |
| BKP9610 | Double Wall Karton Bardak Siyah 8 oz | 80×58×94 | 250 cc | Karton | 500 | [`bkp9610-double-wall-karton-bardak-siyah-8-oz`](bkp9610-double-wall-karton-bardak-siyah-8-oz) |
| BKP9650 | Double Wall Karton Bardak Siyah 14 oz | 90×59×110 | 400 cc | Karton | 500 | [`bkp9650-double-wall-karton-bardak-siyah-14-oz`](bkp9650-double-wall-karton-bardak-siyah-14-oz) |
| BKP9605 | Double Wall Karton Bardak Kraft 8 oz | 80×58×94 | 250 cc | Karton | 500 | [`bkp9605-double-wall-karton-bardak-kraft-8-oz`](bkp9605-double-wall-karton-bardak-kraft-8-oz) |
| BKP9645 | Double Wall Karton Bardak Kraft 14 oz | 90×59×110 | 400 cc | Karton | 500 | [`bkp9645-double-wall-karton-bardak-kraft-14-oz`](bkp9645-double-wall-karton-bardak-kraft-14-oz) |
| BKP9809 | Karton Bardak 6,5 oz | 65×50×70 | 189 cc | Karton | 3000 | [`bkp9809-karton-bardak-6-5-oz`](bkp9809-karton-bardak-6-5-oz) |
| BKP9805 | Karton Bardak 4 oz | 60×45×65 | 116 cc | Karton | 3000 | [`bkp9805-karton-bardak-4-oz`](bkp9805-karton-bardak-4-oz) |
| BKP9810 | Karton Bardak 7 oz | 70×50×75 | 200 cc | Karton | 3000 | [`bkp9810-karton-bardak-7-oz`](bkp9810-karton-bardak-7-oz) |
| BKP9815 | Karton Bardak 8 oz | 85×60×90 | 232 cc | Karton | 2000 | [`bkp9815-karton-bardak-8-oz`](bkp9815-karton-bardak-8-oz) |
| BKP9830 | Karton Bardak 14 oz | 90×60×110 | 410 cc | Karton | 2000 | [`bkp9830-karton-bardak-14-oz`](bkp9830-karton-bardak-14-oz) |
| BKP9820 | Karton Bardak 12 oz | 80×50×120 | 340 cc | Karton | 2000 | [`bkp9820-karton-bardak-12-oz`](bkp9820-karton-bardak-12-oz) |
| BKP9715 | Karton Bardak Kapağı 6,5 oz | 65×65×15 | — | PP | 2000 | [`bkp9715-karton-bardak-kapagi-6-5-oz`](bkp9715-karton-bardak-kapagi-6-5-oz) |
| BKP9730 | Karton Bardak Kapağı 7 oz | 70×70×20 | — | PP | 1000 | [`bkp9730-karton-bardak-kapagi-7-oz`](bkp9730-karton-bardak-kapagi-7-oz) |
| BKP9740 | Karton Bardak Kapağı 8 oz | 80×80×20 | — | PP | 1000 | [`bkp9740-karton-bardak-kapagi-8-oz`](bkp9740-karton-bardak-kapagi-8-oz) |
| BKP9760 | Karton Bardak Kapağı 14 oz | 90×90×25 | — | PP | 1000 | [`bkp9760-karton-bardak-kapagi-14-oz`](bkp9760-karton-bardak-kapagi-14-oz) |
| BKP9240 | Bardak Kapağı 12 oz (PET) | 90×90×20 | — | PET | 1000 | [`bkp9240-bardak-kapagi-12-oz-pet`](bkp9240-bardak-kapagi-12-oz-pet) |

#### Viyoller (2 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP9900 | İkili Viyol Bardak Tutacağı | 220×100×45 | — | Karton | 480 | [`bkp9900-ikili-viyol-bardak-tutacagi`](bkp9900-ikili-viyol-bardak-tutacagi) |
| BKP9905 | Dörtlü Viyol Bardak Tutacağı | 205×215×45 | — | Karton | 220 | [`bkp9905-dortlu-viyol-bardak-tutacagi`](bkp9905-dortlu-viyol-bardak-tutacagi) |

#### Kraft Çantalar (2 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP10250 | Kraft Çanta 12x22x29 cm | 120×220×290 | — | Karton | 250 | [`bkp10250-kraft-canta-12x22x29-cm`](bkp10250-kraft-canta-12x22x29-cm) |
| BKP10260 | Kraft Çanta 16x28x29 cm | 160×280×290 | — | Karton | 250 | [`bkp10260-kraft-canta-16x28x29-cm`](bkp10260-kraft-canta-16x28x29-cm) |


### Restoran ve Paket Servis Kapları (76 ürün)

#### Mikrodalga Yemek Kapları (14 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP2210-2250 | 1 Bölmeli Mikrodalga Yemek Kabı | 240×200×40-30 | — | PP | 200 | [`bkp2210-2250-1-bolmeli-mikrodalga-yemek-kabi`](bkp2210-2250-1-bolmeli-mikrodalga-yemek-kabi) |
| BKP2220-2260 | 2 Bölmeli Mikrodalga Yemek Kabı | 240×200×40-30 | — | PP | 200 | [`bkp2220-2260-2-bolmeli-mikrodalga-yemek-kabi`](bkp2220-2260-2-bolmeli-mikrodalga-yemek-kabi) |
| BKP2230-2270 | 3 Bölmeli Mikrodalga Yemek Kabı | 240×200×40-30 | — | PP | 200 | [`bkp2230-2270-3-bolmeli-mikrodalga-yemek-kabi`](bkp2230-2270-3-bolmeli-mikrodalga-yemek-kabi) |
| BKP2240-2280 | 4 Bölmeli Mikrodalga Yemek Kabı | 240×200×40-30 | — | PP | 200 | [`bkp2240-2280-4-bolmeli-mikrodalga-yemek-kabi`](bkp2240-2280-4-bolmeli-mikrodalga-yemek-kabi) |
| BKP2570-2580 | 2 Bölmeli Hamburger Kabı | 240×200×40-30 | — | PP | 400 | [`bkp2570-2580-2-bolmeli-hamburger-kabi`](bkp2570-2580-2-bolmeli-hamburger-kabi) |
| BKP2380 | 3 Bölmeli Büyük Yemek Kabı | 285×200×45-30 | — | PP | 100 | [`bkp2380-3-bolmeli-buyuk-yemek-kabi`](bkp2380-3-bolmeli-buyuk-yemek-kabi) |
| BKP2510-2540 | Sıcak Yemek Kabı 500 cc | 190×125×55 | 500 cc | PP | 500 | [`bkp2510-2540-sicak-yemek-kabi-500-cc`](bkp2510-2540-sicak-yemek-kabi-500-cc) |
| BKP2520-2540 | Sıcak Yemek Kabı 750 cc | 190×125×75 | 750 cc | PP | 500 | [`bkp2520-2540-sicak-yemek-kabi-750-cc`](bkp2520-2540-sicak-yemek-kabi-750-cc) |
| BKP2530-2540 | Sıcak Yemek Kabı 1000 cc | 190×125×90 | 1000 cc | PP | 500 | [`bkp2530-2540-sicak-yemek-kabi-1000-cc`](bkp2530-2540-sicak-yemek-kabi-1000-cc) |
| BKP2020-2010 | Yuvarlak Sıcak Yemek Kabı 500 cc | 170×170×50 | 500 cc | PP | 280 | [`bkp2020-2010-yuvarlak-sicak-yemek-kabi-500-cc`](bkp2020-2010-yuvarlak-sicak-yemek-kabi-500-cc) |
| BKP2030-2010 | Yuvarlak Sıcak Yemek Kabı 750 cc | 170×170×60 | 750 cc | PP | 280 | [`bkp2030-2010-yuvarlak-sicak-yemek-kabi-750-cc`](bkp2030-2010-yuvarlak-sicak-yemek-kabi-750-cc) |
| BKP2040-2010 | Yuvarlak Sıcak Yemek Kabı 1000 cc | 170×170×70 | 1000 cc | PP | 280 | [`bkp2040-2010-yuvarlak-sicak-yemek-kabi-1000-cc`](bkp2040-2010-yuvarlak-sicak-yemek-kabi-1000-cc) |
| BKP2610 | 3 Bölmeli Kebap Kabı | 290×200×60 | 1500 cc | PP | 75 | [`bkp2610-3-bolmeli-kebap-kabi`](bkp2610-3-bolmeli-kebap-kabi) |
| BKP2620 | 4 Bölmeli Kebap Kabı | 290×200×60 | 1500 cc | PP | 75 | [`bkp2620-4-bolmeli-kebap-kabi`](bkp2620-4-bolmeli-kebap-kabi) |

#### Tavuk Kapları (2 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP2630 | Tavuk Kabı 150x200 | 150×200×95 | — | PET | 200 | [`bkp2630-tavuk-kabi-150x200`](bkp2630-tavuk-kabi-150x200) |
| BKP2640 | Tavuk Kabı 160x220 | 160×220×115 | — | PET | 200 | [`bkp2640-tavuk-kabi-160x220`](bkp2640-tavuk-kabi-160x220) |

#### Çok Amaçlı Kaplar (2 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP6140 | Sekizgen 5 Bölmeli Kap | 230×230×35 | — | PET | 175 | [`bkp6140-sekizgen-5-bolmeli-kap`](bkp6140-sekizgen-5-bolmeli-kap) |
| BKP6130 | Sekizgen 5 Bölmeli Kap Yüksek | 230×230×45 | — | PET | 175 | [`bkp6130-sekizgen-5-bolmeli-kap-yuksek`](bkp6130-sekizgen-5-bolmeli-kap-yuksek) |

#### Kahvaltı ve Bölmeli Kaplar (9 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP905 | 3 Bölmeli Çok Amaçlı Kap | 150×110×30 | 250 cc | PET | 500 | [`bkp905-3-bolmeli-cok-amacli-kap`](bkp905-3-bolmeli-cok-amacli-kap) |
| BKP910 | 4 Bölmeli Çok Amaçlı Kap | 150×110×30 | 250 cc | PET | 500 | [`bkp910-4-bolmeli-cok-amacli-kap`](bkp910-4-bolmeli-cok-amacli-kap) |
| BKP915 | 3 Bölmeli Oval Kap Alçak Kapak | 200×165×20 | 300 cc | PET | 250 | [`bkp915-3-bolmeli-oval-kap-alcak-kapak`](bkp915-3-bolmeli-oval-kap-alcak-kapak) |
| BKP925 | 4 Bölmeli Oval Kap Alçak Kapak | 200×165×20 | 300 cc | PET | 250 | [`bkp925-4-bolmeli-oval-kap-alcak-kapak`](bkp925-4-bolmeli-oval-kap-alcak-kapak) |
| BKP930 | 5 Bölmeli Oval Kap Alçak Kapak | 200×165×20 | 300 cc | PET | 250 | [`bkp930-5-bolmeli-oval-kap-alcak-kapak`](bkp930-5-bolmeli-oval-kap-alcak-kapak) |
| BKP935 | 5 Bölmeli Kap Yüksek Kapak | 250×180×30 | 500 cc | PET | 250 | [`bkp935-5-bolmeli-kap-yuksek-kapak`](bkp935-5-bolmeli-kap-yuksek-kapak) |
| BKP939 | 6 Bölmeli Kap Yüksek Kapak | 250×180×30 | 500 cc | PET | 200 | [`bkp939-6-bolmeli-kap-yuksek-kapak`](bkp939-6-bolmeli-kap-yuksek-kapak) |
| BKP945 | 8 Bölmeli Kap Yüksek Kapak | 280×200×30 | 750 cc | PET | 200 | [`bkp945-8-bolmeli-kap-yuksek-kapak`](bkp945-8-bolmeli-kap-yuksek-kapak) |
| BKP835 | 7 Bölmeli Kahvaltı Kabı | 280×200×30 | 750 cc | PET | 200 | [`bkp835-7-bolmeli-kahvalti-kabi`](bkp835-7-bolmeli-kahvalti-kabi) |

#### Meze Kapları (3 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP6960 | 1/5 Meze Kabı 230 cc | 133×158×25 | 230 cc | PET | 1000 | [`bkp6960-1-5-meze-kabi-230-cc`](bkp6960-1-5-meze-kabi-230-cc) |
| BKP6970 | 1/4 Meze Kabı 330 cc | 113×158×33 | 330 cc | PET | 1000 | [`bkp6970-1-4-meze-kabi-330-cc`](bkp6970-1-4-meze-kabi-330-cc) |
| BKP6980 | 1/3 Meze Kabı 450 cc | 113×158×43 | 450 cc | PET | 1000 | [`bkp6980-1-3-meze-kabi-450-cc`](bkp6980-1-3-meze-kabi-450-cc) |

#### Sandviç Kapları (1 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP6890 | Üçgen Sandviç Kabı | 375×79×87 | — | PET | 1000 | [`bkp6890-ucgen-sandvic-kabi`](bkp6890-ucgen-sandvic-kabi) |

#### Çorba Kaseleri (6 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP1930 | PP Çorba Kasesi 14 oz | 120×120×55 | 350 cc | PP | 1000 | [`bkp1930-pp-corba-kasesi-14-oz`](bkp1930-pp-corba-kasesi-14-oz) |
| BKP1940 | PP Çorba Kasesi 16 oz | 120×120×65 | 450 cc | PP | 1000 | [`bkp1940-pp-corba-kasesi-16-oz`](bkp1940-pp-corba-kasesi-16-oz) |
| BKP9850 | Karton Çorba Kasesi 14 oz | 110×110×55 | 400 cc | Karton | 500 | [`bkp9850-karton-corba-kasesi-14-oz`](bkp9850-karton-corba-kasesi-14-oz) |
| BKP9855 | Karton Çorba Kasesi 16 oz | 110×110×65 | 450 cc | Karton | 500 | [`bkp9855-karton-corba-kasesi-16-oz`](bkp9855-karton-corba-kasesi-16-oz) |
| BKP10540 | Kraft Karton Çorba Kasesi 16 oz | 110×110×65 | 450 cc | Karton | 500 | [`bkp10540-kraft-karton-corba-kasesi-16-oz`](bkp10540-kraft-karton-corba-kasesi-16-oz) |
| BKP1950 | PP Çorba Kasesi Kapağı 116 mm | 116×116×20 | — | PP | 1000 | [`bkp1950-pp-corba-kasesi-kapagi-116-mm`](bkp1950-pp-corba-kasesi-kapagi-116-mm) |

#### Sos Kapları (16 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP1560 | Yuvarlak Sos Kabı (Panda) 50 cc | 70×70×40 | 50 cc | PP | 1000 | [`bkp1560-yuvarlak-sos-kabi-panda-50-cc`](bkp1560-yuvarlak-sos-kabi-panda-50-cc) |
| BKP1570 | Yuvarlak Sos Kabı (Panda) 80 cc | 70×70×60 | 80 cc | PP | 1000 | [`bkp1570-yuvarlak-sos-kabi-panda-80-cc`](bkp1570-yuvarlak-sos-kabi-panda-80-cc) |
| BKP1575 | Yuvarlak Sos Kabı (Panda) 100 cc | 70×70×75 | 100 cc | PP | 1000 | [`bkp1575-yuvarlak-sos-kabi-panda-100-cc`](bkp1575-yuvarlak-sos-kabi-panda-100-cc) |
| BKP1610 | Kapaklı Sos Kabı 1 oz (30 ml) | 50×50×25 | 30 cc | PP | 1000 | [`bkp1610-kapakli-sos-kabi-1-oz-30-ml`](bkp1610-kapakli-sos-kabi-1-oz-30-ml) |
| BKP1620 | Kapaklı Sos Kabı 2 oz (60 ml) | 63×63×25 | 60 cc | PP | 1000 | [`bkp1620-kapakli-sos-kabi-2-oz-60-ml`](bkp1620-kapakli-sos-kabi-2-oz-60-ml) |
| BKP450 | Sos Kabı Kendinden Kapaklı 20 cc | 65×50×20 | 20 cc | PET | 2700 | [`bkp450-sos-kabi-kendinden-kapakli-20-cc`](bkp450-sos-kabi-kendinden-kapakli-20-cc) |
| BKP460 | Sos Kabı Kendinden Kapaklı 30 cc | 65×50×30 | 30 cc | PET | 2700 | [`bkp460-sos-kabi-kendinden-kapakli-30-cc`](bkp460-sos-kabi-kendinden-kapakli-30-cc) |
| BKP470 | Sos Kabı Kendinden Kapaklı 50 cc | 85×60×25 | 50 cc | PET | 1000 | [`bkp470-sos-kabi-kendinden-kapakli-50-cc`](bkp470-sos-kabi-kendinden-kapakli-50-cc) |
| BKP480 | Sos Kabı Kendinden Kapaklı 80 cc | 85×60×40 | 80 cc | PET | 1000 | [`bkp480-sos-kabi-kendinden-kapakli-80-cc`](bkp480-sos-kabi-kendinden-kapakli-80-cc) |
| BKP580 | Oval Sos Kabı Kendinden Kapaklı 80 cc | 85×60×24 | 80 cc | PET | 1000 | [`bkp580-oval-sos-kabi-kendinden-kapakli-80-cc`](bkp580-oval-sos-kabi-kendinden-kapakli-80-cc) |
| BKP590 | Oval Sos Kabı Kendinden Kapaklı 100 cc | 100×80×30 | 100 cc | PET | 1000 | [`bkp590-oval-sos-kabi-kendinden-kapakli-100-cc`](bkp590-oval-sos-kabi-kendinden-kapakli-100-cc) |
| BKP600-2 | Oval Sos Kabı Kendinden Kapaklı 150 cc | 80×60×45 | 150 cc | PET | 1000 | [`bkp600-2-oval-sos-kabi-kendinden-kapakli-150-cc`](bkp600-2-oval-sos-kabi-kendinden-kapakli-150-cc) |
| BKP510 | Kare Sos Kabı Kendinden Kapaklı 50 cc | 110×85×35 | 50 cc | PET | 1500 | [`bkp510-kare-sos-kabi-kendinden-kapakli-50-cc`](bkp510-kare-sos-kabi-kendinden-kapakli-50-cc) |
| BKP520 | Kare Sos Kabı Kendinden Kapaklı 80 cc | 110×85×40 | 80 cc | PET | 1500 | [`bkp520-kare-sos-kabi-kendinden-kapakli-80-cc`](bkp520-kare-sos-kabi-kendinden-kapakli-80-cc) |
| BKP530 | Kare Sos Kabı Kendinden Kapaklı 100 cc | 110×85×45 | 100 cc | PET | 1500 | [`bkp530-kare-sos-kabi-kendinden-kapakli-100-cc`](bkp530-kare-sos-kabi-kendinden-kapakli-100-cc) |
| BKP560 | Kare Sos Kabı Kendinden Kapaklı 125 cc | 110×85×55 | 125 cc | PET | 1500 | [`bkp560-kare-sos-kabi-kendinden-kapakli-125-cc`](bkp560-kare-sos-kabi-kendinden-kapakli-125-cc) |

#### Salata Kapları (19 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP980 | Yuvarlak Salata Kabı Siyah 500 cc | 175×175×30 | 500 cc | PET / PP | 300 | [`bkp980-yuvarlak-salata-kabi-siyah-500-cc`](bkp980-yuvarlak-salata-kabi-siyah-500-cc) |
| BKP985 | Yuvarlak Salata Kabı MF120-121 | 220×220×40 | 750-1000 cc | PET / PP | 300 | [`bkp985-yuvarlak-salata-kabi-mf120-121`](bkp985-yuvarlak-salata-kabi-mf120-121) |
| BKP654 | Yuvarlak Salata Kabı 150 cc | 120×55 | 150 cc | PET | 500 | [`bkp654-yuvarlak-salata-kabi-150-cc`](bkp654-yuvarlak-salata-kabi-150-cc) |
| BKP656 | Yuvarlak Salata Kabı 250 cc | 125×63 | 250 cc | PET | 400 | [`bkp656-yuvarlak-salata-kabi-250-cc`](bkp656-yuvarlak-salata-kabi-250-cc) |
| BKP658 | Yuvarlak Salata Kabı 375 cc | 133×133×75 | 375 cc | PET | 300 | [`bkp658-yuvarlak-salata-kabi-375-cc`](bkp658-yuvarlak-salata-kabi-375-cc) |
| BKP660 | Yuvarlak Salata Kabı 500 cc | 155×155×80 | 500 cc | PET | 300 | [`bkp660-yuvarlak-salata-kabi-500-cc`](bkp660-yuvarlak-salata-kabi-500-cc) |
| BKP670 | Yuvarlak Salata Kabı 750 cc | 170×170×87 | 750 cc | PET | 300 | [`bkp670-yuvarlak-salata-kabi-750-cc`](bkp670-yuvarlak-salata-kabi-750-cc) |
| BKP680 | Yuvarlak Salata Kabı 1000 cc | 185×185×93 | 1000 cc | PET | 300 | [`bkp680-yuvarlak-salata-kabi-1000-cc`](bkp680-yuvarlak-salata-kabi-1000-cc) |
| BKP940 | Kare Salata Kabı 250 cc Siyah | 128×128×45 | 250 cc | PET | 800 | [`bkp940-kare-salata-kabi-250-cc-siyah`](bkp940-kare-salata-kabi-250-cc-siyah) |
| BKP945-2 | Kare Salata Kabı 375 cc Siyah | 128×128×50 | 375 cc | PET | 800 | [`bkp945-2-kare-salata-kabi-375-cc-siyah`](bkp945-2-kare-salata-kabi-375-cc-siyah) |
| BKP950 | Kare Salata Kabı 500 cc Siyah | 128×128×105 | 500 cc | PET | 800 | [`bkp950-kare-salata-kabi-500-cc-siyah`](bkp950-kare-salata-kabi-500-cc-siyah) |
| BKP955 | Kare Salata Kabı 750 cc Siyah | 190×190×50 | 750 cc | PET | 300 | [`bkp955-kare-salata-kabi-750-cc-siyah`](bkp955-kare-salata-kabi-750-cc-siyah) |
| BKP956 | Kare Salata Kabı 750 cc Şeffaf | 190×190×50 | 750 cc | PET | 300 | [`bkp956-kare-salata-kabi-750-cc-seffaf`](bkp956-kare-salata-kabi-750-cc-seffaf) |
| BKP960 | Kare Salata Kabı 1000 cc Siyah | 190×190×65 | 1000 cc | PET | 300 | [`bkp960-kare-salata-kabi-1000-cc-siyah`](bkp960-kare-salata-kabi-1000-cc-siyah) |
| BKP955-Y | Kare Salata Kabı 750 cc Yeşil | 190×190×50 | 750 cc | PET | 300 | [`bkp955-y-kare-salata-kabi-750-cc-yesil`](bkp955-y-kare-salata-kabi-750-cc-yesil) |
| BKP960-Y | Kare Salata Kabı 1000 cc Yeşil | 190×190×65 | 1000 cc | PET | 300 | [`bkp960-y-kare-salata-kabi-1000-cc-yesil`](bkp960-y-kare-salata-kabi-1000-cc-yesil) |
| BKP845 | Kare Salata Kabı 750 cc | 180×180×50 | 750 cc | PET | 300 | [`bkp845-kare-salata-kabi-750-cc`](bkp845-kare-salata-kabi-750-cc) |
| BKP247 | Kare Salata Kabı 1000 cc | 180×180×70 | 1000 cc | PET | 300 | [`bkp247-kare-salata-kabi-1000-cc`](bkp247-kare-salata-kabi-1000-cc) |
| BKP849 | Kare Salata Kabı 1500 cc | 180×180×93 | 1500 cc | PET | 300 | [`bkp849-kare-salata-kabi-1500-cc`](bkp849-kare-salata-kabi-1500-cc) |

#### Kraft Kaseler (4 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP10450 | Kraft Kase 550 cc | 145×125×50 | 550 cc | Karton | 400 | [`bkp10450-kraft-kase-550-cc`](bkp10450-kraft-kase-550-cc) |
| BKP10460 | Kraft Kase 750 cc | 145×125×65 | 750 cc | Karton | 300 | [`bkp10460-kraft-kase-750-cc`](bkp10460-kraft-kase-750-cc) |
| BKP10520 | Kraft Kase 1100 cc | 190×165×50 | 1100 cc | Karton | 200 | [`bkp10520-kraft-kase-1100-cc`](bkp10520-kraft-kase-1100-cc) |
| BKP10525 | Kraft Kase 1300 cc | 190×160×70 | 1300 cc | Karton | 200 | [`bkp10525-kraft-kase-1300-cc`](bkp10525-kraft-kase-1300-cc) |


### Alüminyum Kaplar (18 ürün)

#### Alüminyum Kaplar (18 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP20050 | Alüminyum Krem Karamel Kabı | — | — | Alüminyum | — | [`bkp20050-aluminyum-krem-karamel-kabi`](bkp20050-aluminyum-krem-karamel-kabi) |
| BKP20055 | Alüminyum Sup Kase 180 cc | 96×88×32 | 180 cc | Alüminyum | 5000 | [`bkp20055-aluminyum-sup-kase-180-cc`](bkp20055-aluminyum-sup-kase-180-cc) |
| BKP20060 | Alüminyum Sütlaç Kabı 325 cc | 110×110×40 | 325 cc | Alüminyum | 3000 | [`bkp20060-aluminyum-sutlac-kabi-325-cc`](bkp20060-aluminyum-sutlac-kabi-325-cc) |
| BKP20065 | Alüminyum Küçük Künefe Kabı | 135×124×26 | 210 cc | Alüminyum | 2000 | [`bkp20065-aluminyum-kucuk-kunefe-kabi`](bkp20065-aluminyum-kucuk-kunefe-kabi) |
| BKP20070 | Alüminyum Büyük Künefe Kabı | — | — | Alüminyum | — | [`bkp20070-aluminyum-buyuk-kunefe-kabi`](bkp20070-aluminyum-buyuk-kunefe-kabi) |
| BKP20075 | Alüminyum Kap 250 g | 148×123×25 | 320 cc | Alüminyum | 2000 | [`bkp20075-aluminyum-kap-250-g`](bkp20075-aluminyum-kap-250-g) |
| BKP20080 | Alüminyum Kap 350 g | 148×123×40 | 350 cc | Alüminyum | 2000 | [`bkp20080-aluminyum-kap-350-g`](bkp20080-aluminyum-kap-350-g) |
| BKP20085 | Alüminyum Kap 500 g | 205×115×33 | 500 cc | Alüminyum | 2000 | [`bkp20085-aluminyum-kap-500-g`](bkp20085-aluminyum-kap-500-g) |
| BKP20090 | Alüminyum Kap 750 g | 219×127×33 | 750 cc | Alüminyum | 2000 | [`bkp20090-aluminyum-kap-750-g`](bkp20090-aluminyum-kap-750-g) |
| BKP20095 | Alüminyum Kap 1000 g | 220×155×38 | 1000 cc | Alüminyum | 2000 | [`bkp20095-aluminyum-kap-1000-g`](bkp20095-aluminyum-kap-1000-g) |
| BKP20110 | Alüminyum Kap 1500 g | 225×175×35 | 1500 cc | Alüminyum | — | [`bkp20110-aluminyum-kap-1500-g`](bkp20110-aluminyum-kap-1500-g) |
| BKP20115 | Alüminyum Tepsi 2,5 kg | 316×216×50 | 2500 cc | Alüminyum | — | [`bkp20115-aluminyum-tepsi-2-5-kg`](bkp20115-aluminyum-tepsi-2-5-kg) |
| BKP20120 | Alüminyum Tepsi 3,25 kg | 322×252×50 | 3250 cc | Alüminyum | 400 | [`bkp20120-aluminyum-tepsi-3-25-kg`](bkp20120-aluminyum-tepsi-3-25-kg) |
| BKP20125 | Alüminyum Tepsi 5 kg | — | 5000 cc | Alüminyum | — | [`bkp20125-aluminyum-tepsi-5-kg`](bkp20125-aluminyum-tepsi-5-kg) |
| BKP20130 | 2 Bölmeli Alüminyum Kap | 227×177×30 | — | Alüminyum | 1000 | [`bkp20130-2-bolmeli-aluminyum-kap`](bkp20130-2-bolmeli-aluminyum-kap) |
| BKP20135 | 3 Bölmeli Alüminyum Kap | 227×177×30 | — | Alüminyum | 1000 | [`bkp20135-3-bolmeli-aluminyum-kap`](bkp20135-3-bolmeli-aluminyum-kap) |
| BKP20140 | Alüminyum Oval Tepsi (Orta) | — | — | Alüminyum | — | [`bkp20140-aluminyum-oval-tepsi-orta`](bkp20140-aluminyum-oval-tepsi-orta) |
| BKP20145 | Alüminyum Oval Tepsi (Büyük) | — | — | Alüminyum | — | [`bkp20145-aluminyum-oval-tepsi-buyuk`](bkp20145-aluminyum-oval-tepsi-buyuk) |


### Üst Film Kapama Kapları (31 ürün)

#### Üst Film Kapama Yemek Kapları (15 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP1210 | Kapama Kabı 110x110 H35 Şeffaf | 110×110×35 | — | PP | 1000 | [`bkp1210-kapama-kabi-110x110-h35-seffaf`](bkp1210-kapama-kabi-110x110-h35-seffaf) |
| BKP1210-G | Kapama Kabı 110x110 H35 Gold | 110×110×35 | — | PP | 1000 | [`bkp1210-g-kapama-kabi-110x110-h35-gold`](bkp1210-g-kapama-kabi-110x110-h35-gold) |
| BKP1215 | Kapama Kabı 110x110 H45 Siyah | 110×110×45 | — | PP | 1000 | [`bkp1215-kapama-kabi-110x110-h45-siyah`](bkp1215-kapama-kabi-110x110-h45-siyah) |
| BKP1200 | Kapama Kabı 110x110 H35 Federli Şeffaf | 110×110×35 | — | PET | 1000 | [`bkp1200-kapama-kabi-110x110-h35-federli-seffaf`](bkp1200-kapama-kabi-110x110-h35-federli-seffaf) |
| BKP1310 | Kapama Oval Kap 177x117 H40 Siyah | 177×117×40 | — | PP | 880 | [`bkp1310-kapama-oval-kap-177x117-h40-siyah`](bkp1310-kapama-oval-kap-177x117-h40-siyah) |
| BKP1310-GOLD | Kapama Oval Kap 177x117 H40 Gold | 177×117×40 | — | PP | 880 | [`bkp1310-gold-kapama-oval-kap-177x117-h40-gold`](bkp1310-gold-kapama-oval-kap-177x117-h40-gold) |
| BKP1320-K | Kapama Oval Kap 177x117 H40 Siyah + Kapak | 177×117×40 | — | PP | 880 | [`bkp1320-k-kapama-oval-kap-177x117-h40-siyah-kapak`](bkp1320-k-kapama-oval-kap-177x117-h40-siyah-kapak) |
| BKP2720 | 1 Bölmeli Kapama Tepsisi | 227×178×45 | — | PP | 400 | [`bkp2720-1-bolmeli-kapama-tepsisi`](bkp2720-1-bolmeli-kapama-tepsisi) |
| BKP2730 | 2 Bölmeli Kapama Tepsisi | 227×178×45 | — | PP | 400 | [`bkp2730-2-bolmeli-kapama-tepsisi`](bkp2730-2-bolmeli-kapama-tepsisi) |
| BKP2740 | 3 Bölmeli Kapama Tepsisi | 227×178×45 | — | PP | 400 | [`bkp2740-3-bolmeli-kapama-tepsisi`](bkp2740-3-bolmeli-kapama-tepsisi) |
| BKP2710 | 3 Bölmeli Kapama Tepsisi 20 g | 227×178×45 | — | PP | 400 | [`bkp2710-3-bolmeli-kapama-tepsisi-20-g`](bkp2710-3-bolmeli-kapama-tepsisi-20-g) |
| BKP2750 | 4 Bölmeli Kapama Tepsisi | 227×178×45 | — | PP | 400 | [`bkp2750-4-bolmeli-kapama-tepsisi`](bkp2750-4-bolmeli-kapama-tepsisi) |
| BKP2760 | 6 Bölmeli Kapama Tepsisi | 227×178×45 | — | PP | 400 | [`bkp2760-6-bolmeli-kapama-tepsisi`](bkp2760-6-bolmeli-kapama-tepsisi) |
| BKP2790 | 5 Bölmeli Kapama Tepsisi | 320×255×35 | — | PP | 450 | [`bkp2790-5-bolmeli-kapama-tepsisi`](bkp2790-5-bolmeli-kapama-tepsisi) |
| BKP2770 | 7 Bölmeli Kapama Tepsisi | 325×265×55 | — | PP | 200 | [`bkp2770-7-bolmeli-kapama-tepsisi`](bkp2770-7-bolmeli-kapama-tepsisi) |

#### Üst Film Kapama Et Kapları (16 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP2910 | Kapama Et Kabı 190x144 H22 | 190×144×22 | — | PP | 600 | [`bkp2910-kapama-et-kabi-190x144-h22`](bkp2910-kapama-et-kabi-190x144-h22) |
| BKP2920 | Kapama Et Kabı 190x144 H30 | 190×144×30 | — | PP | 600 | [`bkp2920-kapama-et-kabi-190x144-h30`](bkp2920-kapama-et-kabi-190x144-h30) |
| BKP2930 | Kapama Et Kabı 190x144 H43 | 190×144×43 | — | PP | 600 | [`bkp2930-kapama-et-kabi-190x144-h43`](bkp2930-kapama-et-kabi-190x144-h43) |
| BKP2940 | Kapama Et Kabı 190x144 H50 | 190×144×50 | — | PP | 600 | [`bkp2940-kapama-et-kabi-190x144-h50`](bkp2940-kapama-et-kabi-190x144-h50) |
| BKP2950 | Kapama Et Kabı 190x144 H60 | 190×144×60 | — | PP | 600 | [`bkp2950-kapama-et-kabi-190x144-h60`](bkp2950-kapama-et-kabi-190x144-h60) |
| BKP2955 | Kapama Et Kabı 190x144 H75 | 190×144×75 | — | PP | 600 | [`bkp2955-kapama-et-kabi-190x144-h75`](bkp2955-kapama-et-kabi-190x144-h75) |
| BKP3110 | Kapama Et Kabı 227x178 H30 | 227×178×30 | — | PP | 300 | [`bkp3110-kapama-et-kabi-227x178-h30`](bkp3110-kapama-et-kabi-227x178-h30) |
| BKP3120 | Kapama Et Kabı 227x178 H40 | 227×178×40 | — | PP | 300 | [`bkp3120-kapama-et-kabi-227x178-h40`](bkp3120-kapama-et-kabi-227x178-h40) |
| BKP3130 | Kapama Et Kabı 227x178 H50 | 227×178×50 | — | PP | 300 | [`bkp3130-kapama-et-kabi-227x178-h50`](bkp3130-kapama-et-kabi-227x178-h50) |
| BKP3140 | Kapama Et Kabı 227x178 H60 | 227×178×60 | — | PP | 300 | [`bkp3140-kapama-et-kabi-227x178-h60`](bkp3140-kapama-et-kabi-227x178-h60) |
| BKP3150 | Kapama Et Kabı 227x178 H80 | 227×178×80 | — | PP | 300 | [`bkp3150-kapama-et-kabi-227x178-h80`](bkp3150-kapama-et-kabi-227x178-h80) |
| BKP3160 | Kapama Et Kabı 227x178 H100 | 227×178×100 | — | PP | 200 | [`bkp3160-kapama-et-kabi-227x178-h100`](bkp3160-kapama-et-kabi-227x178-h100) |
| BKP3410 | Kapama Et Kabı 325x260 H50 | 325×260×50 | — | PP | 80 | [`bkp3410-kapama-et-kabi-325x260-h50`](bkp3410-kapama-et-kabi-325x260-h50) |
| BKP3320 | Kapama Et Kabı 325x260 H65 | 325×260×65 | — | PP | 80 | [`bkp3320-kapama-et-kabi-325x260-h65`](bkp3320-kapama-et-kabi-325x260-h65) |
| BKP3430 | Kapama Et Kabı 325x260 H80 | 325×260×80 | — | PP | 80 | [`bkp3430-kapama-et-kabi-325x260-h80`](bkp3430-kapama-et-kabi-325x260-h80) |
| BKP3440 | Kapama Et Kabı 325x260 H100 | 325×260×100 | — | PP | 120 | [`bkp3440-kapama-et-kabi-325x260-h100`](bkp3440-kapama-et-kabi-325x260-h100) |


### Tabak ve Bardaklar (30 ürün)

#### Parti Bardak ve Tabakları (2 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP1710 | Renkli Kup Bardak 200 cc | 80×48×75 | 200 cc | PP | 500 | [`bkp1710-renkli-kup-bardak-200-cc`](bkp1710-renkli-kup-bardak-200-cc) |
| BKP1730 | Renkli Tabak 225 mm | 225×225×30 | — | PP | 500 | [`bkp1730-renkli-tabak-225-mm`](bkp1730-renkli-tabak-225-mm) |

#### İtalyan Serisi Tabak ve Bardaklar (14 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP1002 | Kahve Bardağı 80 cc | 55×35×50 | 80 cc | PP | 5000 | [`bkp1002-kahve-bardagi-80-cc`](bkp1002-kahve-bardagi-80-cc) |
| BKP1715-S2 | Renkli Bardak Sarı 200 cc | 70×45×90 | 200 cc | PP | 2500 | [`bkp1715-s2-renkli-bardak-sari-200-cc`](bkp1715-s2-renkli-bardak-sari-200-cc) |
| BKP1715-S | Renkli Bardak Siyah 200 cc | 70×45×90 | 200 cc | PP | 2500 | [`bkp1715-s-renkli-bardak-siyah-200-cc`](bkp1715-s-renkli-bardak-siyah-200-cc) |
| BKP1715-P | Renkli Bardak Pembe 200 cc | 70×45×90 | 200 cc | PP | 2500 | [`bkp1715-p-renkli-bardak-pembe-200-cc`](bkp1715-p-renkli-bardak-pembe-200-cc) |
| BKP1715-K | Renkli Bardak Kırmızı 200 cc | 70×45×90 | 200 cc | PP | 2500 | [`bkp1715-k-renkli-bardak-kirmizi-200-cc`](bkp1715-k-renkli-bardak-kirmizi-200-cc) |
| BKP1715-T | Renkli Bardak Turuncu 200 cc | 70×45×90 | 200 cc | PP | 2500 | [`bkp1715-t-renkli-bardak-turuncu-200-cc`](bkp1715-t-renkli-bardak-turuncu-200-cc) |
| BKP1715-M | Renkli Bardak Mavi 200 cc | 70×45×90 | 200 cc | PP | 2500 | [`bkp1715-m-renkli-bardak-mavi-200-cc`](bkp1715-m-renkli-bardak-mavi-200-cc) |
| BKP1715-L | Renkli Bardak Lacivert 200 cc | 70×45×90 | 200 cc | PP | 2500 | [`bkp1715-l-renkli-bardak-lacivert-200-cc`](bkp1715-l-renkli-bardak-lacivert-200-cc) |
| BKP1715-Y | Renkli Bardak Yeşil 200 cc | 70×45×90 | 200 cc | PP | 2500 | [`bkp1715-y-renkli-bardak-yesil-200-cc`](bkp1715-y-renkli-bardak-yesil-200-cc) |
| BKP1715-B | Renkli Bardak Beyaz 200 cc | 70×45×90 | 200 cc | PP | 2500 | [`bkp1715-b-renkli-bardak-beyaz-200-cc`](bkp1715-b-renkli-bardak-beyaz-200-cc) |
| BK-CP440 | Derin Tabak Düz Beyaz 220 mm 14,5 g | 220×220×40 | — | PP | 720 | [`bk-cp440-derin-tabak-duz-beyaz-220-mm-14-5-g`](bk-cp440-derin-tabak-duz-beyaz-220-mm-14-5-g) |
| BK-CP441 | Derin Tabak Desenli Beyaz 220 mm 14,5 g | 220×220×40 | — | PP | 720 | [`bk-cp441-derin-tabak-desenli-beyaz-220-mm-14-5-g`](bk-cp441-derin-tabak-desenli-beyaz-220-mm-14-5-g) |
| BK-CP442 | Düz Tabak Beyaz 220 mm 14,5 g | 220×220×40 | — | PP | 720 | [`bk-cp442-duz-tabak-beyaz-220-mm-14-5-g`](bk-cp442-duz-tabak-beyaz-220-mm-14-5-g) |
| BK-CP445 | Pizza Tabağı Beyaz 320 mm 35 g | 320×320×25 | — | PP | 300 | [`bk-cp445-pizza-tabagi-beyaz-320-mm-35-g`](bk-cp445-pizza-tabagi-beyaz-320-mm-35-g) |

#### PP Bardaklar (9 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP1005 | Otomat Bardağı 180 cc | 70×40×80 | 180 cc | PP | 3000 | [`bkp1005-otomat-bardagi-180-cc`](bkp1005-otomat-bardagi-180-cc) |
| BKP1029 | Çaycı Bardağı Kahverengi 160 cc | 70×45×75 | 160 cc | PP | 3000 | [`bkp1029-cayci-bardagi-kahverengi-160-cc`](bkp1029-cayci-bardagi-kahverengi-160-cc) |
| BKP1030 | Çaycı Bardağı Şeffaf 160 cc | 70×50×75 | 160 cc | PP | 3000 | [`bkp1030-cayci-bardagi-seffaf-160-cc`](bkp1030-cayci-bardagi-seffaf-160-cc) |
| BKP1125 | PP Bardak 330 cc (Ø80) | 80×50×110 | 330 cc | PP | 1000 | [`bkp1125-pp-bardak-330-cc-80`](bkp1125-pp-bardak-330-cc-80) |
| BKP1027 | PP Bardak 350 cc (Ø80) | 80×50×120 | 350 cc | PP | 1000 | [`bkp1027-pp-bardak-350-cc-80`](bkp1027-pp-bardak-350-cc-80) |
| BKP1029-2 | PP Bardak 400 cc (Ø98) | 98×60×115 | 400 cc | PP | 1000 | [`bkp1029-2-pp-bardak-400-cc-98`](bkp1029-2-pp-bardak-400-cc-98) |
| BKP1060 | PP Bardak 350 cc (Ø95) | 95×60×110 | 350 cc | PP | 1000 | [`bkp1060-pp-bardak-350-cc-95`](bkp1060-pp-bardak-350-cc-95) |
| BKP1070 | PP Bardak 450 cc (Ø95) | 95×60×120 | 450 cc | PP | 1000 | [`bkp1070-pp-bardak-450-cc-95`](bkp1070-pp-bardak-450-cc-95) |
| BKP1080 | PP Bardak 550 cc (Ø95) | 95×60×130 | 550 cc | PP | 1000 | [`bkp1080-pp-bardak-550-cc-95`](bkp1080-pp-bardak-550-cc-95) |

#### Standart Tabaklar (5 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP1660 | 135 mm Eko Tabak 1,9 g | 135×135×20 | — | PP | 5000 | [`bkp1660-135-mm-eko-tabak-1-9-g`](bkp1660-135-mm-eko-tabak-1-9-g) |
| BKP1670 | 170 mm Eko Tabak 3 g | 170×170×20 | — | PP | 4000 | [`bkp1670-170-mm-eko-tabak-3-g`](bkp1670-170-mm-eko-tabak-3-g) |
| BKP1680 | 190 mm Eko Tabak 4 g | 190×190×20 | — | PP | 3000 | [`bkp1680-190-mm-eko-tabak-4-g`](bkp1680-190-mm-eko-tabak-4-g) |
| BKP1690 | 205 mm Eko Tabak 5 g | 205×205×20 | — | PP | 2000 | [`bkp1690-205-mm-eko-tabak-5-g`](bkp1690-205-mm-eko-tabak-5-g) |
| BKP1670-F | 170 mm F Model Beyaz Tabak | 170×170×20 | — | PP | 800 | [`bkp1670-f-170-mm-f-model-beyaz-tabak`](bkp1670-f-170-mm-f-model-beyaz-tabak) |


### Çatal, Kaşık ve Bıçak (33 ürün)

#### Plastik Çatallar (11 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BK-CP610-B | Eko Çatal 2 g Beyaz | 160 | — | PS | 5000 | [`bk-cp610-b-eko-catal-2-g-beyaz`](bk-cp610-b-eko-catal-2-g-beyaz) |
| BK-CP610 | Eko Çatal 2 g | 160 | — | PS | 5000 | [`bk-cp610-eko-catal-2-g`](bk-cp610-eko-catal-2-g) |
| BK-CP615 | Lüks Çizgili Çatal 2,69 g | 170 | — | PS | 4000 | [`bk-cp615-luks-cizgili-catal-2-69-g`](bk-cp615-luks-cizgili-catal-2-69-g) |
| BK-CP618-S | Lüks Çatal 2,8 g Siyah | 180 | — | PS | 4000 | [`bk-cp618-s-luks-catal-2-8-g-siyah`](bk-cp618-s-luks-catal-2-8-g-siyah) |
| BK-CP618 | Lüks Çatal 2,8 g | 180 | — | PS | 4000 | [`bk-cp618-luks-catal-2-8-g`](bk-cp618-luks-catal-2-8-g) |
| BK-CP620 | Lüks Renkli Çatal 3,20 g | 175 | — | PS | 4000 | [`bk-cp620-luks-renkli-catal-3-20-g`](bk-cp620-luks-renkli-catal-3-20-g) |
| BK-CP615-2 | Lüks Düz Çatal 3,25 g | 175 | — | PS | 4000 | [`bk-cp615-2-luks-duz-catal-3-25-g`](bk-cp615-2-luks-duz-catal-3-25-g) |
| BK-CP628 | Ultra Lüks Renkli Çatal 3,85 g | 175 | — | PS | 3000 | [`bk-cp628-ultra-luks-renkli-catal-3-85-g`](bk-cp628-ultra-luks-renkli-catal-3-85-g) |
| BK-CP630 | Desenli Lüks Çatal 5,25 g | 180 | — | PS | 2000 | [`bk-cp630-desenli-luks-catal-5-25-g`](bk-cp630-desenli-luks-catal-5-25-g) |
| BK-CP635 | Cips Çatalı 0,45 g | 80 | — | PS | 10000 | [`bk-cp635-cips-catali-0-45-g`](bk-cp635-cips-catali-0-45-g) |
| BK-CP636 | Cips Çatalı 0,65 g | 80 | — | PS | 10000 | [`bk-cp636-cips-catali-0-65-g`](bk-cp636-cips-catali-0-65-g) |

#### Plastik Kaşıklar (6 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BK-CP651-S | Lüks Kaşık 2,9 g Siyah | 180 | — | PS | 3000 | [`bk-cp651-s-luks-kasik-2-9-g-siyah`](bk-cp651-s-luks-kasik-2-9-g-siyah) |
| BK-CP655 | Lüks Kaşık 3,85 g | 145 | — | PS | 4000 | [`bk-cp655-luks-kasik-3-85-g`](bk-cp655-luks-kasik-3-85-g) |
| BK-CP651 | Lüks Kaşık 2,9 g | 180 | — | PS | 3000 | [`bk-cp651-luks-kasik-2-9-g`](bk-cp651-luks-kasik-2-9-g) |
| BK-CP658 | Lüks Kaşık 4 g | 180 | — | PS | 2000 | [`bk-cp658-luks-kasik-4-g`](bk-cp658-luks-kasik-4-g) |
| BK-CP660 | Desenli Lüks Kaşık 5,6 g | 180 | — | PS | 2000 | [`bk-cp660-desenli-luks-kasik-5-6-g`](bk-cp660-desenli-luks-kasik-5-6-g) |
| BK-CP665 | Karıştırıcı 0,40 g | 110 | — | PS | 9000 | [`bk-cp665-karistirici-0-40-g`](bk-cp665-karistirici-0-40-g) |

#### Plastik Bıçaklar (6 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BK-CP680 | Eko Bıçak 2 g | 160 | — | PS | 4000 | [`bk-cp680-eko-bicak-2-g`](bk-cp680-eko-bicak-2-g) |
| BK-CP683-S | Lüks Bıçak 2,8 g Siyah | 160 | — | PS | 4000 | [`bk-cp683-s-luks-bicak-2-8-g-siyah`](bk-cp683-s-luks-bicak-2-8-g-siyah) |
| BK-CP685 | Lüks Bıçak 3,25 g | 160 | — | PS | 4000 | [`bk-cp685-luks-bicak-3-25-g`](bk-cp685-luks-bicak-3-25-g) |
| BK-CP687 | Lüks Renkli Bıçak 3,25 g | 170 | — | PS | 4000 | [`bk-cp687-luks-renkli-bicak-3-25-g`](bk-cp687-luks-renkli-bicak-3-25-g) |
| BK-CP693 | Desenli Lüks Bıçak 5,25 g | 180 | — | PS | 3000 | [`bk-cp693-desenli-luks-bicak-5-25-g`](bk-cp693-desenli-luks-bicak-5-25-g) |
| BK-CP690 | Ultra Lüks Bıçak 5 g | 185 | — | PS | 3000 | [`bk-cp690-ultra-luks-bicak-5-g`](bk-cp690-ultra-luks-bicak-5-g) |

#### Dondurma Kaşıkları (4 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BK-CP671 | Dondurma Kaşığı 8 cm (Moblen) | 80 | — | PP | 9000 | [`bk-cp671-dondurma-kasigi-8-cm-moblen`](bk-cp671-dondurma-kasigi-8-cm-moblen) |
| BK-CP672 | Dondurma Kaşığı 12,5 cm | 125 | — | PS | 2000 | [`bk-cp672-dondurma-kasigi-12-5-cm`](bk-cp672-dondurma-kasigi-12-5-cm) |
| BK-CP673 | Dondurma Kaşığı 13 cm | 130 | — | PS | 2000 | [`bk-cp673-dondurma-kasigi-13-cm`](bk-cp673-dondurma-kasigi-13-cm) |
| BK-CP674 | Panda Dondurma Kaşığı | 75 | — | PS | 14000 | [`bk-cp674-panda-dondurma-kasigi`](bk-cp674-panda-dondurma-kasigi) |

#### Hazır Yemek Setleri (6 ürün)

| Kod | Ürün | Ölçü (mm) | Hacim | Materyal | Koli içi | Klasör |
|---|---|---|---|---|---|---|
| BKP7110-S | Çatal-Kaşık 6'lı Set Siyah | — | — | — | 500 | [`bkp7110-s-catal-kasik-6-li-set-siyah`](bkp7110-s-catal-kasik-6-li-set-siyah) |
| BKP7111 | Çatal-Bıçak 6'lı Set | — | — | — | 500 | [`bkp7111-catal-bicak-6-li-set`](bkp7111-catal-bicak-6-li-set) |
| BKP7105-S | Çatal-Bıçak 6'lı Set Siyah | — | — | — | 500 | [`bkp7105-s-catal-bicak-6-li-set-siyah`](bkp7105-s-catal-bicak-6-li-set-siyah) |
| BKP7110 | Çatal-Kaşık 6'lı Set | — | — | — | 500 | [`bkp7110-catal-kasik-6-li-set`](bkp7110-catal-kasik-6-li-set) |
| BKP7130-S | Çatal-Kaşık-Bıçak 7'li Set Siyah | — | — | — | 500 | [`bkp7130-s-catal-kasik-bicak-7-li-set-siyah`](bkp7130-s-catal-kasik-bicak-7-li-set-siyah) |
| BKP7130 | Çatal-Kaşık-Bıçak 7'li Set | — | — | — | 500 | [`bkp7130-catal-kasik-bicak-7-li-set`](bkp7130-catal-kasik-bicak-7-li-set) |

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
