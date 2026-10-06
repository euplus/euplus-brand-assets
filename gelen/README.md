# Gelen kutusu

İşlenmemiş katalog ve ürün görsellerini buraya bırakın. Claude bu klasörü okur,
içeriği işler ve kalıcı yerine taşır; işlendikten sonra klasör boşaltılır.

## Nasıl bırakılır

Dosyaları doğrudan bu klasöre kopyalayın. Tedarikçi adını dosya adına yazarsanız
eşleştirme kendiliğinden olur:

```
gelen/
├── polat-ambalaj-katalog-2026.pdf        ← katalog
├── ozkan-plastik/                         ← ya da tedarikçi adıyla klasör
│   ├── katalog.pdf
│   └── fotograflar/
│       ├── IMG_4821.jpg
│       └── IMG_4822.jpg
└── notlar.txt                             ← varsa fiyat, iletişim, açıklama
```

Dosya adı tedarikçiyi belli etmiyorsa sorun değil, sohbette söylemeniz yeterli.

## İşlendikten sonra nereye gider

| Gelen | Gittiği yer |
|---|---|
| Katalog PDF | `kaynaklar/<tedarikci>/<tedarikci>-katalog-<yil>.pdf` |
| Ürün görselleri | `urunler/<kod>-<ad>/` içine JPG + PNG olarak |
| Tedarikçi bilgisi | `kaynaklar/<tedarikci>/tedarikci.json` |
| Ürün verisi | `urunler/<kod>-<ad>/urun.json` + `ilan.md` |

## Neyi belirtmek faydalı

Zorunlu değil, ama varsa işi hızlandırır:

- **Tedarikçi adı** ve iletişim bilgisi
- **Ürün kodu öneki** (Crystal Pack için `CP` gibi) — yoksa ben öneririm
- **Hangi ürünler alınacak** — katalogdaki her şey mi, bir bölüm mü
- **Görsel kullanım izni** var mı — public depoda yayımlanacağı için önemli
