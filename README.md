# Proyek Analisis Data E-Commerce 🛍️

## Deskripsi
Proyek ini bertujuan untuk menganalisis data transaksi e-commerce guna menemukan pola perilaku pelanggan, jam sibuk pembelian, dan performa penjualan di wilayah tertentu. Hasil analisis ini digunakan untuk memberikan rekomendasi strategis bagi tim operasional dan pemasaran.

## Struktur Data
Dataset yang digunakan mencakup informasi mengenai:
- Pelanggan (Customers)
- Pesanan (Orders)
- Item Pesanan (Order Items)
- Pembayaran (Payments)
- Produk (Products)
- Lokasi (Geolocation)
- Penjual (Sellers)

## Tahapan Analisis
1. **Data Wrangling**: Menggabungkan dataset, menangani missing values pada kolom logistik, dan memperbaiki tipe data datetime.
2. **Exploratory Data Analysis (EDA)**: Mengeksplorasi tren penjualan bulanan, distribusi geografis pelanggan di Sao Paulo, dan pengaruh cicilan terhadap nilai transaksi.
3. **Visualization**: Membuat grafik interaktif untuk memudahkan pemahaman tren jam sibuk dan metode pembayaran favorit[cite: 2].

## Cara Menjalankan Dashboard Streamlit
Dashboard ini dapat dijalankan di lingkungan lokal Anda dengan langkah-langkah berikut:

### 1. Persiapan Environment
Pastikan Anda memiliki Python (versi 3.11 atau 3.12) terinstal di sistem Anda.
```bash
# Buat folder proyek
mkdir proyek_analisis_data
cd proyek_analisis_data

# Buat virtual environment (opsional tapi disarankan)
python -m venv venv
source venv/bin/activate  # Untuk Mac/Linux
.\venv\Scripts\activate   # Untuk Windows