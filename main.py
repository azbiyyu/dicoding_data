import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io

# === WRANGLING DATA ===
# MEMBACA DATA
df = pd.read_csv('products_dataset.csv')

# TITLE
st.title('Product_Sales Analysis')

# Data Exploration Section
st.header('Data Exploration')
st.write("### Rangkuman Statistics")
st.write(df.describe())
st.write("### Data Awal 5 Rows")
st.write(df.head())
st.write("### Data AKhir 5 Rows")
st.write(df.tail())
st.write("### Data Info")
# st.write(df.info())
buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()
st.text(info_str)


# Data Cleaning Section
st.header('Data Cleaning')

# Check for duplicates
duplicate_count = df.duplicated().sum()
st.write(f"Number of Duplicates: {duplicate_count}")

# Check for missing values
missing_values = df.isna().sum()
st.write("Missing Values:")
st.write(missing_values)

# Fill missing values
df['product_category_name'].fillna(value='cama_mesa_banho', inplace=True)
df['product_name_lenght'].fillna(value=df['product_name_lenght'].median(), inplace=True)
df['product_description_lenght'].fillna(value=df['product_description_lenght'].mean(), inplace=True)
df['product_photos_qty'].fillna(value=df['product_photos_qty'].mean(), inplace=True)
df['product_weight_g'].fillna(value=df['product_weight_g'].mean(), inplace=True)
df['product_length_cm'].fillna(value=df['product_length_cm'].mean(), inplace=True)
df['product_height_cm'].fillna(value=df['product_height_cm'].mean(), inplace=True)
df['product_width_cm'].fillna(value=df['product_width_cm'].mean(), inplace=True)

# Data Visualization Section
st.header('Data Visualization')

# ==== PERTANYAAN ====
# APA KATEGORI PRODUK PENJUALAN TERPOPULER ?
kategori_penjualan = df.groupby('product_category_name')['product_id'].count().reset_index()
kategori_penjualan.columns = ['product_category_name', 'jumlah_produk_terjual']

st.write("### Angka Penjualan Product/Kategori")
st.bar_chart(kategori_penjualan.set_index('product_category_name'))

kategori_terlaris = kategori_penjualan[kategori_penjualan['jumlah_produk_terjual'] == kategori_penjualan['jumlah_produk_terjual'].max()]
st.write("### Kategori Penjualan Terbanyak")
st.write(kategori_terlaris)

# 2. APA HUBUNGAN ANTARA PENJULAN PRODUK DAN JUMLAH FOTO ?
foto_produk_terjual = df.groupby('product_photos_qty')['product_id'].count().reset_index()
foto_produk_terjual.columns = ['product_photos_qty', 'jumlah_produk_terjual']

st.write("### Hubungan Angka Penjualan Dengan Jumlah Foto ")
st.bar_chart(foto_produk_terjual.set_index('product_photos_qty'))

st.write("### Jumlah Produk Terjual untuk Setiap Kuantitas Foto")
st.dataframe(foto_produk_terjual)

if __name__ == '__main__':
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.set_option('deprecation.showfileUploaderEncoding', False)
