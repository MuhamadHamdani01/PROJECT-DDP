import streamlit as st
from halaman_utama import tampilkan_halaman_utama
from stok import main as atur_stok
from transaksi import main as tampilkan_transaksi
from data_penjualan import tampilkan_data_penjualan

st.sidebar.title("Navisagi")
menu = st.sidebar.radio(
    "Pilih Halaman", 
    ["Halaman Utama", "Atur Stok", "Penjualan", "Data Penjualan"]
)

if menu == "Halaman Utama":
    tampilkan_halaman_utama()
elif menu == "Atur Stok":
    atur_stok()
elif menu == "Penjualan":
    tampilkan_transaksi()
elif menu == "Data Penjualan":
    tampilkan_data_penjualan()
