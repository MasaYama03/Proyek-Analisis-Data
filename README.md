# Analisis Data Bike Sharing 🚲

Proyek ini berisi analisis data bike sharing yang terdiri dari notebook analisis dan dashboard interaktif.

## 📊 Deskripsi Proyek

Analisis data penyewaan sepeda untuk mengidentifikasi pola dan faktor yang mempengaruhi jumlah penyewaan. Proyek ini mencakup:
1. Analisis data menggunakan Jupyter Notebook
2. Dashboard interaktif menggunakan Streamlit

## 📁 Struktur Proyek
```
Projek Analisis data Bike Sharing Data/
├── dashboard/             # Folder untuk dashboard
│   ├── dashboard.py      # File utama dashboard Streamlit
│   ├── day.csv          # Dataset harian yang sudah dibersihkan
│   └── hour.csv         # Dataset per jam yang sudah dibersihkan
├── data/                 # Dataset mentah
│   ├── day.csv          # Dataset harian original
│   └── hour.csv         # Dataset per jam original
├── notebook.ipynb        # Notebook analisis data
├── requirements.txt      # Daftar package yang diperlukan
└── README.md            # Dokumentasi proyek
```

## Instalasi

1. Clone repository ini atau download sebagai ZIP
2. Install semua package yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```

## Menjalankan Jupyter Notebook

1. Buka Command Prompt atau Terminal
2. Arahkan ke direktori proyek:
   ```bash
   cd "path/to/Projek Analisis data Bike Sharing Data"
   ```
3. Jalankan Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
4. Buka file `notebook.ipynb`

## Menjalankan Dashboard

1. Buka Command Prompt atau Terminal
2. Arahkan ke direktori dashboard:
   ```bash
   cd "path/to/Projek Analisis data Bike Sharing Data/dashboard"
   ```
3. Jalankan dashboard:
   ```bash
   streamlit run dashboard.py
   ```

## Penjelasan Package

streamlit==1.43.1 - untuk membuat dashboard interaktif
pandas==2.1.4 - untuk manipulasi dan analisis data
plotly==6.0.0 - untuk membuat visualisasi interaktif
numpy==1.25.2 - untuk operasi numerik
matplotlib==3.8.0 - untuk visualisasi data statis
seaborn==0.13.0 - untuk visualisasi data statistik
scikit-learn==1.6.1 - untuk analisis data dan model statistik
python-dateutil==2.8.2 - untuk manipulasi tanggal
pytz==2023.3 - untuk penanganan zona waktu

## Fitur Dashboard

Dashboard menyediakan visualisasi interaktif untuk:
- Tren rental sepeda harian
- Analisis dampak cuaca terhadap jumlah rental
- Pola rental per jam
- Analisis musiman (Spring, Summer, Fall, Winter)
- Perbandingan hari kerja vs akhir pekan

### Filter Interaktif:
- Rentang tanggal
- Musim
- Kondisi cuaca
- Tipe hari (hari kerja/akhir pekan)

## Hasil Analisis

Notebook analisis (`notebook.ipynb`) menjawab beberapa pertanyaan bisnis:
1. Faktor-faktor yang mempengaruhi jumlah penyewaan sepeda
2. Perbedaan pola penyewaan di hari kerja vs akhir pekan
3. Waktu puncak penyewaan sepeda dalam sehari

## Troubleshooting

### Masalah Umum:

1. **Package tidak ditemukan**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Error saat membaca file**:
   - Pastikan berada di direktori yang benar
   - Periksa struktur folder sesuai dengan yang dijelaskan di atas

3. **Streamlit tidak ditemukan**:
   ```bash
   pip uninstall streamlit
   pip install streamlit
   ```

4. **Jupyter Notebook tidak berjalan**:
   ```bash
   pip install jupyter
   ```

## Requirements

Lihat file `requirements.txt` untuk daftar lengkap package yang diperlukan. Package utama yang digunakan:
- streamlit==1.43.1 - untuk dashboard
- pandas==2.1.4 - untuk analisis data
- plotly==6.0.0 - untuk visualisasi interaktif
- matplotlib==3.8.0 - untuk visualisasi statis
- seaborn==0.13.0 - untuk visualisasi statistik

## Author

- **Nama:** Masahiro Gerarudo Yamazaki
- **Email:** masahiroymzk24@gmail.com
