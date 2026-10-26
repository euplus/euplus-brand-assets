# EUPLUS Marka Logo Arşivi — Claude notları

## Bu depo nedir
EUPLUS Lojistik Ambalaj A.Ş. ve izm!r ürün markalarının resmî logoları (SVG + şeffaf PNG)
+ e-ticaret için ürün arşivi: tedarikçi katalogları (`kaynaklar/`), ürün görselleri ve
hazır ilan metinleri (`urunler/`), basılabilir ürün kataloğu (`katalog/`).
Ürünler farklı web sitelerine yüklenmek üzere hazırlanır; ana hedef kendi siteniz.
Başka bir projeyle (guzeltedarik vb.) kod olarak ilişkili DEĞİL (yalnızca Güzel Tedarik logosu burada arşivli); bağımsız, sadece lokal + GitHub.
Detaylı kullanım kuralları ve renkler `README.md` içinde; burada sadece çalışma bilgileri var.

## GitHub / yayın
- Depo: https://github.com/euplus/euplus-brand-assets (**public**)
- Remote: `origin = git@github.com:euplus/euplus-brand-assets.git`, dal `main`
- Kimlik doğrulama: SSH, `~/.ssh/id_ed25519` (GitHub kullanıcı adı `euplus`). Token yok.
  Test: `ssh -T git@github.com` → "Hi euplus!"
- `gh` CLI girişli DEĞİL. `gh` gerektiren bir işte önce `gh auth login` iste; yoksa düz `git` kullan.
- Commit kimliği (repo-local ayarlı): Kadir Güneş <suheybkadir.gunes@gmail.com>
- GitHub Pages: `main` / `/ (root)` — kökteki `index.html` yayınlanır.
  Adres: https://euplus.github.io/euplus-brand-assets/
- Ham dosya bağlantısı: `https://raw.githubusercontent.com/euplus/euplus-brand-assets/main/logos/<marka>/<dosya>`

## Klasör düzeni (buna sadık kal)
```
logos/<marka-slug>/          marka logoları (SVG + 512/1024/2048 şeffaf PNG)
gelen/                       İŞLENMEMİŞ kutu — kullanıcı buraya katalog/foto bırakır
                             (.gitignore'da; README.md hariç commit edilmez)
kaynaklar/<tedarikci-slug>/  orijinal katalog PDF + tedarikci.json (iletişim, izin, kod öneki)
urunler/<kod>-<urun-adi>/    <slug>.jpg (1200×1200 beyaz) + <slug>.png (şeffaf)
                             + urun.json (yapısal veri) + ilan.md (kopyala-yapıştır metin)
urunler/urunler.csv          toplu içe aktarma (Excel/pazaryeri, UTF-8 BOM)
urunler/urunler.json         toplu veri (API/otomasyon)
katalog/urunler.json         katalog kaynak verisi — ürün metinlerinin TEK doğru kaynağı
                             (bolumler[n].katalog = "seffaf" | "servis" | "fastfood" | "gida", .tedarikci = slug)
katalog/gorseller/           ürün görselleri: cp*.png şeffaf; pc-*.png şeffaf, pc-*.jpg opak tanıtım fotoğrafı
katalog/build_katalog.py     PDF katalog üretici, 3×3 kart formatı: `python3 katalog/build_katalog.py [seffaf|gida]`
                             seffaf → EUPLUS-Urun-Katalogu-2026.pdf, gida → EUPLUS-Gida-Ambalaj-Katalogu-2026.pdf;
                             katalog başına metinler betikteki CONFIGS'te (kapak, giriş, öne çıkanlar, 6. kart satırı)
katalog/build_katalog_servis.py  PDF katalog üretici — paket servis (katalog="servis"), bölüm başına tek sayfa
katalog/build_katalog_fastfood.py  PDF katalog üretici — fast food (katalog="fastfood"), genel tablo motoru:
                             bölümün `sutunlar`/`tablolar` tanımına göre çizer, uzun tablolar sayfaya taşar; 2 geçişli sayfa no
katalog/build_urunler.py     urunler/ altındaki her şeyi üreten betik
katalog/upscale.py           seçilen ürün görsellerini Real-ESRGAN ile büyütür (--liste adaylar, --geri-al, --derle);
                             orijinaller katalog/gorseller/orijinal/ altında, motor ~/.euplus-tools/realesrgan/
preview/tum-logolar.png      logo önizlemesi
index.html                   Pages sayfası · README.md kullanım kılavuzu
```
Mevcut markalar: euplus, izmir-mendil, izmir-pipet, izmir-seker, izmir-bardak, izmir-pecete, izmir-kagit, guzel-tedarik.
`guzel-tedarik` istisna: SVG yok, sadece 300×158 PNG (kaynak: guzeltedarik sitesindeki `public/logo.png`).
Vektör aslı bulunursa SVG'yi koyup 512/1024/2048 PNG'leri ondan üret, 300'lük PNG'leri kaldır.
Mevcut tedarikçiler: crystal-pack (93 ürün, kod öneki `CP`, katalog "seffaf"),
promocup (72 ürün, kod öneki `PC`, katalog "servis"; tedarikçi kodu olanlarda `PC-<kod>`, diğerlerinde
`PC-<tip><ölçü>` türetildi, bkz. `kaynaklar/promocup/tedarikci.json` → `kod_notu`).
helmex (79 ürün / 256 ölçü satırı, kod öneki `HX`, katalog "fastfood"; İngilizce 2023 kataloğu, 64 sayfa raster).
Helmex ürünlerinde ölçü tablosu olanlar tek ürün + `varyantlar[]` (her varyant bölümün sütun anahtarlarını taşır);
bölümler `grup` (1 karton, 2 kağıt, 3 tamamlayıcı) ile katalogda ayırıcı sayfaya bölünür.
bukap (342 ürün, kod öneki `BKP`, katalog "gida", bölüm 43–50; Crystal Pack ile aynı adres/kardeş firma). Katalogdaki CP kodları
`BK-CP…` olarak alındı (Crystal Pack ile çakışmasın); katalogda aynı kodu paylaşan ikinci ürünler `-2` aldı, ayrıntı `kod_notu`'nda.
Bukap ürünlerinde ek alanlar: alt_grup (sayfa alt başlığı), agirlik_g, tedarikci_kodu, kaynak_sayfa, not.
Ürüne `"katalogda": false` verilirse PDF katalogdan çıkar ama ürün arşivinde (urunler/, CSV) kalır (kullanıcı kararı 2026-10-26:
Bukap karton bardak + kapakları, kraft çanta, çorba kaseleri — 24 ürün).
Ayrıca eski iki ürün: bardak-kilifi-siyah, bardak-kilifi-kraft (elle yazılmış, betik üretmez).

## Yeni katalog/görsel geldiğinde (ana iş akışı)
Kullanıcı `gelen/` klasörüne dosya bırakır ya da sohbete gönderir. Sırayla:
1. **Tedarikçiyi belirle.** `kaynaklar/<slug>/` yoksa aç; `tedarikci.json` yaz
   (ad, iletişim, kod öneki, `gorsel_izni`). Katalogun son sayfasında genelde iletişim olur.
2. **Katalogu arşivle:** `kaynaklar/<slug>/<slug>-katalog-<yil>.pdf`. Orijinali DEĞİŞTİRME.
3. **Ürünleri çıkar.** PyMuPDF (`fitz`) ile sayfaları 300 dpi render et; ürün görseli +
   etiket bloğu çiftlerini bul. Yöntem: sayfayı ~100 dpi'da maskeleyip bağlı bileşen
   çıkar, satır-doluluk oranı yüksek olan = ürün fotoğrafı, düşük olan = etiket metni.
   Etiketi hemen üstündeki fotoğrafla eşleştir. Kontrol sayfası üretip GÖZLE doğrula.
4. **Veriyi `katalog/urunler.json`'a ekle** (kod, ad, ölçü, hacim, materyal, koli, palet, bölüm).
   Promocup şeması ek alanlar taşır: agiz_capi, dip_capi, yukseklik, agirlik_g, fisek_ici, net_kg,
   koli_secenekleri[] (aynı ürünün farklı koli adetleri), tedarikci_kodu, not. Yeni bir tedarikçi
   farklı tabloyla gelirse bölüme `tablo` tipi (bardak/kapak/kart/canta) ver ve her iki build betiğini uyarla.
5. **Görselleri `katalog/gorseller/<kod>.png`** olarak kaydet: 300 dpi kırp, beyaz zemini
   şeffafa çevir (köşelerden floodfill), uzun kenar ≤900 px.
6. `python3 katalog/build_urunler.py` → urunler/ altındaki her şey üretilir.
7. `python3 katalog/build_katalog.py` (şeffaf) ve/veya `python3 katalog/build_katalog_servis.py` (paket servis)
   → PDF katalog güncellenir. Sayfaları PNG'ye render edip GÖZLE kontrol et (tablo sütun çakışması, kırpılan foto).
8. README tablolarını güncelle, `gelen/` içini boşalt, commit + push.

### Görsel çıkarmada dikkat (acı tecrübe)
- Kaynak kataloglarda ürün kodu yazısı genelde fotoğrafın ALT kenarına basılı. Yazıyı
  silmek için kırparken ürünün altını kesme; kesme noktasını gözle doğrula.
- "Geniş ve koyu satırı sil" gibi otomatik temizlik, siyah kapaklı ya da koyu renkli
  ürünlerin üstünü keser. Otomatik kırpmadan sonra MUTLAKA kontrol sayfası üret ve bak.
- Komşu ürünün etiket yazısı kadraja girebilir; beyazla, ama ürüne dokunma.
- Canva/raster kataloglarda (Promocup gibi) metin katmanı yoktur; gömülü sayfa görselini (150 dpi)
  doğrudan çıkar, tabloları gözle okuyup elle yaz. Ürün başına değil kategori başına fotoğraf varsa
  kategori fotoğrafını opak JPEG olarak sakla, ürünler onu paylaşsın; şeffaflaştırmaya çalışma.
- Renkli düz zemin (pembe panel) → floodfill eşiği ~22 + 400 px altı adacıkları sil; gölgedeki zemin
  tonunu "pembelik" (r − (g+b)/2 > 8) ile yakalayıp griye çevir. Beyaz ürünlerde zemine yakın renkleri
  global olarak silme — kutunun gri gölgelenmesini deler; yalnız köşelerden bağlı bölgeyi sil.
- Tedarikçi logosu basılı mockup'lar (Helmex): OpenCV Telea inpainting. Çok renkli amblemi doygunluk +
  renk çeşitliliğiyle bul, soluna yazı için ROI aç, ROI'de yerel zeminden farklı pikselleri maskele (eşik 55,
  sonra 26 ile ikinci geçiş). Perspektifli / büyük logolarda otomatik ROI yetmez; grid çizip elle ROI ver.
  Gri yazı ve yarı saydam logo düşük eşik (20–35) ister. Kıvrımlı yüzeyde büyük logo (kova, bardak kılıfı)
  inpainting ile kurtulmaz → o mockup'ı kullanma, kategori fotoğrafını kullan.
- Turuncu gibi doygun zemin → kroma uzayında (rgb/toplam) renk anahtarı; paneli kenarından 10 px
  içeriden kırp (anti-alias saçak), alfayı 2 px aşındır. Degrade zeminde şeffaf ürün (PET kapak) → opak bırak.
- Sıkıştırılmış (iLovePDF) ama ürün fotoğrafları ayrı gömülü görsel olan kataloglarda (Bukap): sayfayı render edip kırpma;
  gömülü görseli SMask'ıyla birlikte doğrudan çıkar (kalite kaybı yok). Yerleşim matrisine bak — ters yerleştirilmiş
  (a<0) görseller aynalanmalı. Aynı xref sayfada iki kez yerleşebilir; eşleştirmeyi xref değil yerleşim bazında yap.
- Raster etiketler: macOS Vision OCR (Swift, `VNRecognizeTextRequest`, tr-TR) etiketi 600 dpi kırpınca çok iyi okur;
  Kiril harf karışmasını (В→B) normalize et, kod altındaki kesikli çizgi "—==" çöpü üretir. Sonuçları kırpıntı sayfasıyla gözle doğrula.
- PyMuPDF 1.26 `rewrite_images` alfa maskeli büyük belgelerde rastgele segfault verebiliyor (gıda kataloğu);
  build_katalog.py "gida" için kendi JPEG dönüşümünü (`jpeg_images`) kullanır.
- Düşük çözünürlüklü ürün görseli (Bukap ~300 px) → `python3 katalog/upscale.py KOD ...`; şeffaf PNG'de RGB ve alfa ayrı
  büyütülüp beyaz zemin etkisi geri alınır. Sonra build_urunler + build_katalog gida. Real-ESRGAN binary'si dışarıdan
  indirilen koddur; ilk çalıştırma (xattr/chmod) kullanıcıdan istenir.
- Beyaz zemin → şeffaf çevirirken floodfill eşiği 14 iyi çalışır; açık renkli/şeffaf
  ürünlerde (ör. cam gibi tabaklar) içeri sızarsa 6'ya düşür.

## Ürün metinleri
`katalog/build_urunler.py` üretir; `urunler/` altındaki dosyaları ELLE DÜZENLEME.
Metin veya etiket şablonu değişecekse betiği düzenle, sonra yeniden çalıştır.
Açıklama 5 paragraf: ne olduğu + kullanım, teknik özellik, şeffaflık/gıda uygunluğu,
sıcaklık aralığı (−10 °C / +60 °C), koli-palet ve toptan satış koşulu.
Etiketler ürün tipinden (kase/kutu/kavanoz/bardak/tabak/kapak/separatör/kasa/kaşık/şişe)
ve bölümden türetilir, ürün başına 13-14 adet.

## Yeni logo eklerken
1. `logos/<yeni-slug>/` klasörü aç; slug küçük harf, Türkçe karaktersiz, tire ile (`izmir-poset` gibi).
2. SVG'yi koy; PNG'leri SVG'den üret (upscale/yeniden çizim yok):
   `rsvg-convert -w 2048 x.svg -o x-2048.png` veya `inkscape`/`magick` — şeffaf arka plan şart.
3. `README.md` logo tablosuna satır ekle (klasör + ana renkler).
4. `index.html` galerisine kart ekle.
5. `preview/tum-logolar.png` güncellenmeli (mümkünse).
6. Commit + `git push origin main` — Pages otomatik güncellenir.

## Yeni ürün eklerken
1. `urunler/<yeni-slug>/` aç; slug kuralı logolarla aynı. Fotoğraf `<slug>.jpg` (beyaz zemin, en az 800 px).
2. `urunler/README.md`'ye tablo satırı + açıklama + etiketler ekle.
3. Kök `README.md` "Ürün görselleri" tablosuna ve `index.html` "Ürün görselleri" bölümüne kart ekle.
4. Commit + push.

## Kurallar
- Logo dosyalarını değiştirme/optimize etme (SVG minify vb.) — kullanıcı istemedikçe.
- Kaynak katalog PDF'lerine dokunma; `kaynaklar/` salt arşivdir.
- Depo **public**: tedarikçi görsellerini yayımlamadan önce izin durumunu hatırlat.
- PDF katalogda logo PNG değil, `euplus.svg`'den vektör gömülür (sıkıştırma bulanıklaştırır).
- Renk kodlarını README'deki tablodan al; uydurma.
- Push öncesi `git status` temiz olsun; PNG'ler `.gitattributes` ile binary işaretli.
- `Claude outputs/` (müşteri teklif PDF'leri vb.) `.gitignore`'da; public depoya girmez.
- Tedarikçi mockup'larındaki tedarikçi logosu kaldırılır (kullanıcı kararı); kaynak PDF'e dokunulmaz.
- EUPLUS kataloglarında GIDA ÜRÜNÜ yer almaz (kullanıcı kararı, 2026-10-07): tedarikçi kataloğundaki yağ, sos,
  içecek vb. ürünler alınmaz; yalnızca ambalaj ve servis ekipmanı.
