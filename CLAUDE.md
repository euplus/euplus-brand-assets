# EUPLUS Marka Logo Arşivi — Claude notları

## Bu depo nedir
EUPLUS Lojistik Ambalaj A.Ş. ve izm!r ürün markalarının resmî logoları (SVG + şeffaf PNG).
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
logos/<marka-slug>/
  <marka-slug>.svg          vektörel kaynak
  <marka-slug>-512.png      şeffaf PNG, uzun kenar 512
  <marka-slug>-1024.png
  <marka-slug>-2048.png
preview/tum-logolar.png     tüm logoların toplu önizlemesi
index.html                  Pages sayfası (logo galerisi)
README.md                   kullanım kılavuzu + renk tablosu
```
Mevcut markalar: euplus, izmir-mendil, izmir-pipet, izmir-seker, izmir-bardak, izmir-pecete, izmir-kagit.

## Yeni logo eklerken
1. `logos/<yeni-slug>/` klasörü aç; slug küçük harf, Türkçe karaktersiz, tire ile (`izmir-poset` gibi).
2. SVG'yi koy; PNG'leri SVG'den üret (upscale/yeniden çizim yok):
   `rsvg-convert -w 2048 x.svg -o x-2048.png` veya `inkscape`/`magick` — şeffaf arka plan şart.
3. `README.md` logo tablosuna satır ekle (klasör + ana renkler).
4. `index.html` galerisine kart ekle.
5. `preview/tum-logolar.png` güncellenmeli (mümkünse).
6. Commit + `git push origin main` — Pages otomatik güncellenir.

## Kurallar
- Logo dosyalarını değiştirme/optimize etme (SVG minify vb.) — kullanıcı istemedikçe.
- Renk kodlarını README'deki tablodan al; uydurma.
- Push öncesi `git status` temiz olsun; PNG'ler `.gitattributes` ile binary işaretli.
