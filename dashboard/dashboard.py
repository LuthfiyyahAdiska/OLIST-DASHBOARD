import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="E-Commerce Analysis Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    return df

all_df = load_data()

with st.sidebar:
    st.title("Filter Analisis")
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=all_df["order_purchase_timestamp"].min(),
        max_value=all_df["order_purchase_timestamp"].max(),
        value=[all_df["order_purchase_timestamp"].min(), all_df["order_purchase_timestamp"].max()]
    )

main_df = all_df[(all_df["order_purchase_timestamp"] >= str(start_date)) & 
                 (all_df["order_purchase_timestamp"] <= str(end_date))]

st.title("🛍️ E-Commerce Business Dashboard")
st.markdown("Dashboard ini menampilkan performa bisnis berdasarkan hasil data cleaning dan analisis mendalam.")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Pesanan", value=main_df.order_id.nunique())
with col2:
    total_revenue = main_df.payment_value.sum()
    st.metric("Total Pendapatan", value=f"R$ {total_revenue:,.2f}")
with col3:
    avg_payment = main_df.payment_value.mean()
    st.metric("Rata-rata Transaksi", value=f"R$ {avg_payment:,.2f}")

st.divider()


col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Pola Jam Sibuk Pembelian")
    main_df['hour'] = main_df['order_purchase_timestamp'].dt.hour
    hourly_data = main_df.groupby('hour').order_id.nunique().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=hourly_data, x='hour', y='order_id', marker='o', color='#2E86C1')
    ax.set_xlabel("Jam (00-23)")
    ax.set_ylabel("Jumlah Pesanan")
    st.pyplot(fig)

with col_right:
    st.subheader("Metode Pembayaran Terfavorit")
    payment_data = main_df['payment_type'].value_counts().reset_index()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=payment_data, x='count', y='payment_type', palette='viridis')
    ax.set_xlabel("Jumlah Penggunaan")
    ax.set_ylabel(None)
    st.pyplot(fig)

st.divider()
st.subheader("💡 Rekomendasi Strategis")
st.info("""
1. **Targeting Jam Sibuk**: Berdasarkan grafik, lakukan flash sale 1 jam sebelum puncak pesanan.
2. **Optimasi Pembayaran**: Karena metode kartu kredit mendominasi, berikan promo cicilan 0% untuk meningkatkan nilai transaksi.
3. **Fokus Wilayah**: Pastikan stok di gudang wilayah Sao Paulo selalu aman untuk menjaga kecepatan pengiriman.
""")