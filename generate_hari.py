#!/usr/bin/env python3
"""
Script untuk generate index.html dengan informasi hari dan tanggal terbaru
"""

import datetime
import os

def get_hari_indonesia():
    """Mengembalikan nama hari dalam bahasa Indonesia"""
    hari_map = {
        0: "Senin",
        1: "Selasa", 
        2: "Rabu",
        3: "Kamis",
        4: "Jumat",
        5: "Sabtu",
        6: "Minggu"
    }
    return hari_map[datetime.datetime.now().weekday()]

def get_tanggal_format():
    """Mengembalikan tanggal dalam format dd-mm-yyyy"""
    now = datetime.datetime.now()
    return now.strftime("%d-%m-%Y")

def get_tahun():
    """Mengembalikan tahun saat ini"""
    return datetime.datetime.now().year

def generate_html():
    """Generate file index.html dengan data terbaru"""
    hari = get_hari_indonesia()
    tanggal = get_tanggal_format()
    tahun = get_tahun()
    
    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hari Ini - {hari}, {tanggal}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{
            background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 50%, #06b6d4 100%);
            min-height: 100vh;
        }}
        .glass {{
            background: rgba(255, 255, 255, 0.25);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }}
    </style>
</head>
<body class="flex items-center justify-center p-4">
    <div class="glass rounded-3xl p-8 md:p-12 text-center shadow-2xl max-w-md w-full">
        <h1 class="text-4xl md:text-5xl font-bold text-white mb-8 drop-shadow-lg">
            Hari Ini
        </h1>
        
        <div class="space-y-6">
            <div class="bg-white/20 rounded-2xl p-6 backdrop-blur-sm">
                <h2 class="text-2xl md:text-3xl font-semibold text-white mb-2">
                    {hari}
                </h2>
                <p class="text-white/90 text-lg">
                    {tanggal}
                </p>
            </div>
            
            <div class="bg-white/10 rounded-xl p-4 backdrop-blur-sm">
                <p class="text-white/80 text-sm">
                    Tahun {tahun}
                </p>
            </div>
        </div>
        
        <div class="mt-8 text-white/60 text-xs space-y-1">
            <p>Auto-updated daily via GitHub Actions</p>
            <p class="text-cyan-300/80 font-medium">Powered by ChatGPT 5 Engine</p>
        </div>
    </div>
</body>
</html>"""
    
    # Tulis file index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ index.html berhasil di-generate untuk {hari}, {tanggal}")

if __name__ == "__main__":
    generate_html()
