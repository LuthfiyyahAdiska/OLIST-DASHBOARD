import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Olist E-Commerce Dashboard", layout="wide")

# 2. Pengaturan Path Otomatis
# Mencari file all_data.csv di folder yang sama dengan script ini
current_dir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(current_dir, "all_data.csv")

# 3. Fungsi Load Data
@st.cache_data
def load_data():
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        # Pastikan kolom waktu dikonversi ke datetime
        # Jika ada error nama kolom, pastikan di CSV namanya sudah benar
        df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
        return df
    return None

df_all = load_data()

# 4. Validasi Jika Data Berhasil Dimuat
if df_all is not None:
    # --- SIDEBAR ---
    with st.sidebar:
        st.title("Olist Dashboard 📊")
        
        # Filter Rentang Waktu
        min_date = df_all["order_purchase_timestamp"].min()
        max_date = df_all["order_purchase_timestamp"].max()
        
        try:
            start_date, end_date = st.date_input(
                label='Pilih Rentang Waktu',
                min_value=min_date.date(),
                max_value=max_date.date(),
                value=[min_date.date(), max_date.date()]
            )
        except Exception:
            st.error("Silakan pilih rentang tanggal mulai dan selesai.")
            st.stop()

    # Filter Data Berdasarkan Tanggal
    main_df = df_all[(df_all["order_purchase_timestamp"].dt.date >= start_date) & 
                    (df_all["order_purchase_timestamp"].dt.date <= end_date)]

    # --- MAIN PAGE ---
    st.header('Olist Sales Analysis Dashboard 🛒')

    if not main_df.empty:
        # Metrics Utama (KPI)
        col1, col2 = st.columns(2)
        with col1:
            total_orders = main_df.order_id.nunique()
            st.metric("Total Pesanan", value=total_orders)
        with col2:
            total_revenue = main_df.price.sum()
            st.metric("Total Pendapatan", value=f"BRL {total_revenue:,.2f}")

        # Visualisasi 1: Top Kategori
        st.subheader("Top 5 Kategori Produk Berdasarkan Pendapatan")
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Cek kolom kategori (sesuaikan jika namanya berbeda di CSV Anda)
        cat_col = 'product_category_name_english' if 'product_category_name_english' in main_df.columns else 'product_category_name'
        
        top_categories = main_df.groupby(cat_col).price.sum().sort_values(ascending=False).head(5)
        sns.barplot(x=top_categories.values, y=top_categories.index, palette="viridis", ax=ax)
        ax.set_xlabel("Total Pendapatan")
        st.pyplot(fig)

        # Visualisasi 2: Tren Jam Sibuk
        st.subheader("Tren Transaksi Per Jam")
        fig2, ax2 = plt.subplots(figsize=(12, 5))
        hourly_data = main_df.groupby(main_df['order_purchase_timestamp'].dt.hour).order_id.nunique()
        ax2.plot(hourly_data.index, hourly_data.values, marker='o', linewidth=2)
        ax2.set_xticks(range(0, 24))
        ax2.set_xlabel("Jam (24-Hour Format)")
        ax2.set_ylabel("Jumlah Pesanan")
        ax2.grid(True, linestyle='--', alpha=0.6)
        st.pyplot(fig2)

    else:
        st.warning("Data tidak ditemukan untuk rentang waktu tersebut.")
else:
    st.error(f"File 'all_data.csv' tidak ditemukan!")
    st.info(f"Pastikan file all_data.csv berada di folder yang sama dengan dashboard.py. Lokasi yang dicari: {csv_path}")
