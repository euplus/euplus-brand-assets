# EUPLUS · Marka Logo Arşivi

EUPLUS Lojistik Ambalaj San. Tic. A.Ş. ve **izm!r** ürün markalarına ait resmî logoların
vektörel (SVG) ve şeffaf arka planlı (PNG) hâlleri.

Logolar, orijinal kartvizit ve marka dosyalarındaki **vektörel eğrilerden** tek tek ayrıştırıldı —
yeniden çizim ya da görüntü büyütme (upscale) yapılmadı. Bu yüzden SVG'ler sonsuz büyütmeye
uygundur ve matbaa kalitesindedir.

![Tüm logolar](preview/tum-logolar.png)

## Logolar

| Logo | Klasör | Ana renkler |
|---|---|---|
| EUPLUS (`small steps, big leaps`) | [`logos/euplus`](logos/euplus) | `#878786` `#EF7C00` |
| izm!r **MENDİL** | [`logos/izmir-mendil`](logos/izmir-mendil) | `#0054A3` `#009EE3` |
| izm!r **PİPET** | [`logos/izmir-pipet`](logos/izmir-pipet) | `#EF7C00` `#009EE3` `#FFCC00` `#E5007D` |
| izm!r **ŞEKER** | [`logos/izmir-seker`](logos/izmir-seker) | `#A61380` `#009EE3` |
| izm!r **BARDAK** | [`logos/izmir-bardak`](logos/izmir-bardak) | `#FFCC00` `#EC6502` |
| izm!r **PEÇETE** | [`logos/izmir-pecete`](logos/izmir-pecete) | `#0AA537` `#00622D` `#C7D300` |
| izm!r **KAĞIT** | [`logos/izmir-kagit`](logos/izmir-kagit) | `#C3985A` `#00ADEF` |

## Dosya yapısı

Her logo kendi klasöründe, dört formatta:

```
logos/izmir-mendil/
├── izmir-mendil.svg        ← vektörel, ölçeklenebilir (web + matbaa)
├── izmir-mendil-512.png    ← şeffaf, e-posta imzası / küçük kullanım
├── izmir-mendil-1024.png   ← şeffaf, web / sunum
└── izmir-mendil-2048.png   ← şeffaf, büyük baskı / afiş
```

PNG'lerin **arka planı şeffaftır**; renkli zemin üzerinde de sorunsuz kullanılabilir.
Boyut, logonun uzun kenarını ifade eder.

## Nerede hangisini kullanmalı

- **Web sitesi, e-posta imzası, sosyal medya** → `.svg` (yoksa `-512.png` veya `-1024.png`)
- **Word / PowerPoint / PDF teklif dosyaları** → `-1024.png`
- **Matbaa, ambalaj, afiş, araç giydirme** → `.svg` (tercih edilen) veya `-2048.png`
- **Favicon / uygulama ikonu** → `.svg` üzerinden istenen boyutta dışa aktarın

## Doğrudan bağlantı (hotlink)

Bu depo public olduğu için logolar doğrudan bağlanabilir:

```html
<img src="https://raw.githubusercontent.com/KULLANICI/euplus-brand-assets/main/logos/euplus/euplus.svg"
     alt="EUPLUS" width="200">
```

> `KULLANICI` yerine GitHub kullanıcı adınızı yazın.

## Kullanım kuralları

- Logoların **en/boy oranını** koruyun; yatay veya dikey olarak esnetmeyin.
- Renkleri değiştirmeyin, gölge/kontur/efekt eklemeyin.
- Logonun etrafında, `izm!r` yazısının yüksekliği kadar **boş alan** bırakın.
- Karmaşık fotoğraf üzerine yerleştirmeyin; sade ve yeterli kontrastlı zemin kullanın.
- Minimum genişlik: ekranda **80 px**, baskıda **20 mm**.

## Telif

Bu logolar EUPLUS Lojistik Ambalaj San. Tic. A.Ş.'ye ait tescilli marka varlıklarıdır.
Depo, kurum içi ve iş ortaklarıyla paylaşım kolaylığı için herkese açıktır; ancak
logoların üçüncü taraflarca kullanımı şirketin yazılı iznine tabidir.

---

**EUPLUS Lojistik Ambalaj San. Tic. A.Ş.**
Mersinli Mah. 2829 Sokak No:3, 1. Sanayi Sitesi — 35170 İzmir / TÜRKİYE
Tel: +90 232 421 41 41 · Faks: +90 232 421 41 66 · [euplus.com.tr](https://www.euplus.com.tr)
