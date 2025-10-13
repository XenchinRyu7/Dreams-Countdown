# Daily Info - Hari & Tanggal Terkini

Website statis sederhana yang menampilkan informasi hari dan tanggal dengan update otomatis.

## Fitur

- 🌐 Website statis dengan desain modern menggunakan TailwindCSS
- 🎨 Desain glassmorphism yang responsive
- 📅 Menampilkan nama hari (Senin-Minggu) dan tanggal (dd-mm-yyyy)
- 🔄 Update otomatis setiap hari
- 🐍 Script Python untuk generate HTML

## File Structure

```
├── index.html                    # Website utama (auto-generated)
├── generate_hari.py             # Script Python untuk generate HTML
├── .github/workflows/
│   └── daily-hari.yml          # Automation workflow
└── README.md                   # Dokumentasi
```

## Cara Kerja

1. **Script Python** (`generate_hari.py`) akan:
   - Mengambil tanggal dan hari saat ini
   - Generate file `index.html` dengan data terbaru
   - Menggunakan desain TailwindCSS dengan efek glassmorphism

2. **Automation** akan:
   - Berjalan setiap hari
   - Menjalankan script Python
   - Update konten website secara otomatis

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

## Setup GitHub Pages

1. **Buat Repository Public** di GitHub
2. **Push semua file** ke repository
3. **Enable GitHub Pages**:
   - Go to **Settings** → **Pages**
   - Source: **Deploy from a branch**
   - Branch: **`main`** / **`root`**
   - Folder: **`/ (root)`**
4. **Website akan live** di: `https://username.github.io/repo-name`

### ⚠️ **Catatan**:
- GitHub Pages akan otomatis deploy dari branch `main`
- Website akan update setiap kali ada commit baru

## Live Demo

Website dapat diakses melalui GitHub Pages dan akan menampilkan informasi hari dan tanggal terkini.

---

*Simple daily info website* ✨
