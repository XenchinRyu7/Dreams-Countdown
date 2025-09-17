# Auto-Streak - Daily Hari Update

Website statis sederhana yang menampilkan informasi hari dan tanggal terbaru dengan auto-update harian menggunakan GitHub Actions.

## Fitur

- 🌐 Website statis dengan desain modern menggunakan TailwindCSS
- 🎨 Desain glassmorphism yang responsive
- 📅 Menampilkan nama hari (Senin-Minggu) dan tanggal (dd-mm-yyyy)
- 🤖 Auto-update harian menggunakan GitHub Actions
- 🐍 Script Python untuk generate HTML

## File Structure

```
├── index.html                    # Website utama (auto-generated)
├── generate_hari.py             # Script Python untuk generate HTML
├── .github/workflows/
│   └── daily-hari.yml          # GitHub Actions workflow
└── README.md                   # Dokumentasi
```

## Cara Kerja

1. **Script Python** (`generate_hari.py`) akan:
   - Mengambil tanggal dan hari saat ini
   - Generate file `index.html` dengan data terbaru
   - Menggunakan desain TailwindCSS dengan efek glassmorphism

2. **GitHub Actions** (`.github/workflows/daily-hari.yml`) akan:
   - Berjalan setiap hari pada jam 00:00 UTC (07:00 WIB)
   - Menjalankan script Python
   - Commit dan push perubahan ke repository

## Cara Menjalankan Manual

```bash
# Generate index.html dengan data hari ini
python generate_hari.py
```

## Desain

Website menggunakan:
- **TailwindCSS** untuk styling
- **Glassmorphism effect** dengan backdrop blur
- **Gradient background** yang menarik
- **Responsive design** untuk semua device
- **Clean typography** dengan hierarchy yang jelas

## GitHub Actions

Workflow akan otomatis:
- ✅ Checkout repository
- ✅ Setup Python environment
- ✅ Run generate script
- ✅ Check for changes
- ✅ Commit & push jika ada perubahan

## Setup GitHub Pages

1. **Buat Repository Public** di GitHub
2. **Push semua file** ke repository
3. **Enable GitHub Pages**:
   - Go to **Settings** → **Pages**
   - Source: **Deploy from a branch**
   - Branch: **`main`** / **`root`**
   - Folder: **`/ (root)`**
4. **Website akan live** di: `https://XenchinRyu7.github.io/Dreams-Countdown`

### ⚠️ **Catatan Penting**:
- GitHub Pages akan otomatis deploy dari branch `main`
- Tidak perlu branch `gh-pages` terpisah
- Website akan update otomatis setiap kali ada commit ke `main`

## Live Demo

Website akan otomatis terupdate setiap hari pada jam 07:00 WIB dan dapat diakses melalui GitHub Pages.

**URL**: `https://XenchinRyu7.github.io/Dreams-Countdown`

---

*Auto-generated daily via GitHub Actions* 🚀
