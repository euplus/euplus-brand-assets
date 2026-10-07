# Kaynaklar · Tedarikçi arşivi

Ürünlerin geldiği kataloglar ve tedarikçi bilgileri. Her tedarikçi kendi klasöründe:

```
kaynaklar/<tedarikci-slug>/
├── tedarikci.json                        ← iletişim, katalog listesi, kod öneki
├── <tedarikci>-katalog-<yil>.pdf         ← orijinal katalog (değiştirilmez)
└── notlar.md                             ← varsa fiyat, koşul, yazışma notu
```

Ürünlerin hangi tedarikçiden geldiği `urunler/<kod>-<ad>/urun.json` içindeki
`kaynak` alanında tutulur; katalog dosyasına kadar izlenebilir.

## Tedarikçiler

| Tedarikçi | Ürün | Katalog | Kod öneki |
|---|---|---|---|
| [Crystal Pack](crystal-pack) | 93 | [2026](crystal-pack/crystal-pack-katalog-2026.pdf) | `CP` |
| [Promocup](promocup) | 72 | [2026](promocup/promocup-katalog-2026.pdf) | `PC` |
| [Helmex](helmex) | 79 | [2023](helmex/helmex-katalog-2023.pdf) | `HX` |

## Telif ve izin

Kataloglar ve içindeki görseller tedarikçilere aittir. Bu depo **public** olduğu için
görselleri yayımlamadan önce kullanım izninin alınmış olması gerekir. İzin durumu
her tedarikçinin `tedarikci.json` dosyasındaki `gorsel_izni` alanında tutulur.
