import streamlit as st

class Buah:
    def __init__(self, nama, stok, harga_jual, modal):
        self.nama = nama
        self.stok = stok
        self.harga_jual = harga_jual
        self.modal = modal
        self.keuntungan_per_kg = self.harga_jual - self.modal
        self.total_keuntungan = self.keuntungan_per_kg * self.stok

# Fungsi inisialisasi data buah
def inisialisasi_data_buah():
    if 'data_buah' not in st.session_state:
        st.session_state['data_buah'] = [
            Buah("Apel", 0, 0, 0),
            Buah("Pisang", 0, 0, 0),
            Buah("Jeruk", 0, 0, 0),
            Buah("Mangga", 0, 0, 0),
            Buah("Durian", 0, 0, 0),
        ]

# Fungsi utama untuk mengatur stok
def buat_data_buah():
    inisialisasi_data_buah()  # Pastikan state ada
    data_buah = st.session_state['data_buah']

    st.header("Manajemen Stok untuk Penjualan Buah")
    buah_options = [buah.nama for buah in data_buah]
    selected_buah = st.selectbox("Pilih buah untuk diatur", buah_options)
    buah_terpilih = next((buah for buah in data_buah if buah.nama == selected_buah), None)

    if buah_terpilih:
        st.write(f"Data Stok untuk {buah_terpilih.nama}")
        buah_terpilih.stok = st.number_input("Stok (kg)", min_value=0, step=1, value=buah_terpilih.stok)
        buah_terpilih.harga_jual = st.number_input("Harga jual (Rp/kg)", min_value=0, step=1000, value=buah_terpilih.harga_jual)
        buah_terpilih.modal = st.number_input("Modal (Rp/kg)", min_value=0, step=1000, value=buah_terpilih.modal)

        if st.button("Simpan Pengaturan Buah"):
            buah_terpilih.keuntungan_per_kg = buah_terpilih.harga_jual - buah_terpilih.modal
            buah_terpilih.total_keuntungan = buah_terpilih.keuntungan_per_kg * buah_terpilih.stok
            st.success(f"Pengaturan untuk {buah_terpilih.nama} berhasil disimpan.")

    st.write("Data Stok Buah")
    data = [
        {
            "Nama Buah": buah.nama,
            "Stok (kg)": buah.stok,
            "Harga Jual (/kg)": buah.harga_jual,
            "Modal (/kg)": buah.modal,
            "Keuntungan (/kg)": buah.keuntungan_per_kg,
        }
        for buah in data_buah
    ]
    st.table(data)

def main():
    st.title("Atur Stok Buah")
    buat_data_buah()
