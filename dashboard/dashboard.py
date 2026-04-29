import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os

st.set_page_config(page_title="Olist E-Commerce Dashboard", layout="wide")

current_dir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(current_dir, "all_data.csv")

@st.cache_data
def load_data():
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
        return df
    return None

df_all = load_data()

if df_all is not None:
    with st.sidebar:
        st.title("Olist Dashboard 📊")
        
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

    main_df = df_all[(df_all["order_purchase_timestamp"].dt.date >= start_date) & 
                    (df_all["order_purchase_timestamp"].dt.date <= end_date)]

    st.header('Olist Sales Analysis Dashboard 🛒')

    if not main_df.empty:
        col1, col2 = st.columns(2)
        with col1:
            total_orders = main_df.order_id.nunique()
            st.metric("Total Pesanan", value=total_orders)
        with col2:
            total_revenue = main_df.price.sum()
            st.metric("Total Pendapatan", value=f"BRL {total_revenue:,.2f}")

        cat_col = 'product_category_name_english' if 'product_category_name_english' in main_df.columns else 'product_category_name'

        st.subheader("Analisis Kategori Produk")
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown("#### Top 5 Kategori (Pendapatan)")
            fig, ax = plt.subplots(figsize=(10, 5))
            top_categories = main_df.groupby(cat_col).price.sum().sort_values(ascending=False).head(5)
            sns.barplot(x=top_categories.values, y=top_categories.index, hue=top_categories.index, palette="viridis", legend=False, ax=ax)
            ax.set_xlabel("Total Pendapatan")
            st.pyplot(fig)
            
        with col4:
            st.markdown("#### Rata-rata Harga di Top 5 Kategori")
            fig_price, ax_price = plt.subplots(figsize=(10, 5))
            avg_price = main_df[main_df[cat_col].isin(top_categories.index)].groupby(cat_col).price.mean().reindex(top_categories.index)
            sns.barplot(x=avg_price.values, y=avg_price.index, hue=avg_price.index, palette="mako", legend=False, ax=ax_price)
            ax_price.set_xlabel("Rata-rata Harga")
            ax_price.set_ylabel("")
            st.pyplot(fig_price)

        st.subheader("Analisis Tren Transaksi")
        col5, col6 = st.columns(2)
        
        with col5:
            st.markdown("#### Berdasarkan Hari")
            fig_day, ax_day = plt.subplots(figsize=(10, 5))
            days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            day_data = main_df['order_purchase_timestamp'].dt.day_name().value_counts().reindex(days_order)
            sns.barplot(x=day_data.index, y=day_data.values, hue=day_data.index, palette="crest", legend=False, ax=ax_day)
            ax_day.set_xlabel("Hari")
            ax_day.set_ylabel("Jumlah Pesanan")
            ax_day.tick_params(axis='x', rotation=45)
            st.pyplot(fig_day)

        with col6:
            st.markdown("#### Tren Transaksi Per Jam")
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            hourly_data = main_df.groupby(main_df['order_purchase_timestamp'].dt.hour).order_id.nunique()
            ax2.plot(hourly_data.index, hourly_data.values, marker='o', linewidth=2, color="#ff7f0e")
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
