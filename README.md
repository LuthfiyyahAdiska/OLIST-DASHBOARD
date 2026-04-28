# 📊 Olist E-Commerce Data Analysis & Dashboard ✨

Proyek ini merupakan analisis mendalam terhadap dataset publik E-Commerce Olist untuk mengeksplorasi performa penjualan, kategori produk unggulan, serta pola perilaku transaksi pelanggan. Hasil analisis ini kemudian divisualisasikan melalui dashboard interaktif menggunakan Streamlit.

## 📁 Struktur Proyek
- `/dashboard`: Berisi file utama dashboard (`dashboard.py`) dan dataset yang telah dibersihkan (`all_data.csv`).
- `/data`: Direktori untuk menyimpan dataset mentah (CSV).
- `notebook.ipynb`: File Jupyter Notebook yang berisi proses Data Wrangling, EDA, hingga Visualisasi.
- `README.md`: Dokumentasi proyek.
- `requirements.txt`: Daftar library Python yang dibutuhkan.

## 🛠️ Setup Environment - Anaconda
Jika Anda menggunakan Anaconda, ikuti langkah berikut:
```bash
conda create --name olist-ds python=3.9
conda activate olist-ds
pip install -r requirements.txt
```

## 🛠️ Setup Environment - Shell/Terminal (venv)
Jika Anda menggunakan Python virtual environment (venv), ikuti langkah berikut:
```bash
# Membuat virtual environment
python -m venv venv

# Mengaktifkan virtual environment (Windows)
venv\Scripts\activate
# Mengaktifkan virtual environment (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Menjalankan Dashboard
Setelah environment aktif dan semua library telah terinstall, jalankan perintah berikut untuk membuka dashboard:
```bash
streamlit run dashboard/dashboard.py
```
