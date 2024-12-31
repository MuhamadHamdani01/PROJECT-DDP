import streamlit as st
import pandas as pd

# Pastikan inisialisasi dilakukan dengan aman
def inisialisasi_data_penjualan():
    if "data_penjualan" not in st.session_state:
        st.session_state["data_penjualan"] = pd.DataFrame(columns=[
            "Nama Buah", "Jumlah Terjual (kg)", "Total Harga (Rp)", "Total Keuntungan (Rp)"
        ])

# Fungsi mencatat transaksi
def catat_transaksi(nama_buah, jumlah_terjual, total_harga, total_keuntungan):
    inisialisasi_data_penjualan()  # Pastikan state ada
    transaksi_baru = pd.DataFrame({
        "Nama Buah": [nama_buah],
        "Jumlah Terjual (kg)": [jumlah_terjual],
        "Total Harga (Rp)": [total_harga],
        "Total Keuntungan (Rp)": [total_keuntungan],
    })
    st.session_state["data_penjualan"] = pd.concat(
        [st.session_state["data_penjualan"], transaksi_baru], ignore_index=True
    )

# Fungsi menampilkan data penjualan
def tampilkan_data_penjualan():
    inisialisasi_data_penjualan()  # Pastikan state ada
    st.title("Data Penjualan Buah")
    data_penjualan = st.session_state["data_penjualan"]

    if data_penjualan.empty:
        st.info("Belum ada transaksi yang dicatat.")
    else:
        st.write("Data transaksi penjualan:")
        st.dataframe(data_penjualan)
