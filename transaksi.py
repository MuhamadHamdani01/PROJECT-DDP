import streamlit as st
from data_penjualan import catat_transaksi
from stok import inisialisasi_data_buah

def transaksi_penjualan(data_buah):
    st.header("Transaksi Penjualan Buah")

    if not data_buah:
        st.warning("Data buah belum tersedia. Silakan masukkan data stok terlebih dahulu.")
        return

    buah_pilihan = [buah.nama for buah in data_buah]
    pilih_buah = st.selectbox("Pilih buah", buah_pilihan)
    buah_terpilih = next((buah for buah in data_buah if buah.nama == pilih_buah), None)

    if buah_terpilih:
        st.write(f"Stok saat ini: {buah_terpilih.stok} kg")
        jumlah_terjual = st.number_input("Jumlah penjualan (kg)", min_value=0, step=1)

        if st.button("Proses Penjualan"):
            if jumlah_terjual > buah_terpilih.stok:
                st.error("Stok tidak mencukupi.")
            else:
                total_harga = jumlah_terjual * buah_terpilih.harga_jual
                total_keuntungan = jumlah_terjual * buah_terpilih.keuntungan_per_kg

                # Kurangi stok buah
                buah_terpilih.stok -= jumlah_terjual

                # Catat transaksi
                catat_transaksi(buah_terpilih.nama, jumlah_terjual, total_harga, total_keuntungan)

                st.success("Penjualan berhasil diproses!")
                st.write(f"Total harga: Rp {total_harga}")
                st.write(f"Total keuntungan: Rp {total_keuntungan}")
                st.write(f"Stok tersisa: {buah_terpilih.stok} kg")

def main():
    inisialisasi_data_buah()  # Pastikan data buah ada
    data_buah = st.session_state['data_buah']
    transaksi_penjualan(data_buah)
