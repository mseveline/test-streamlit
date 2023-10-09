import streamlit as st

st.title('Kalkulator Sederhana')

# Input field untuk memasukkan angka pertama
angka1 = st.number_input('Masukkan Angka Pertama', format="%f")

# Input field untuk memasukkan angka kedua
angka2 = st.number_input('Masukkan Angka Kedua', format="%f")

# Tombol untuk menghitung hasil pertambahan
if st.button('Hitung'):
    hasil = int(angka1 + angka2)  # Mengonversi hasil ke bilangan bulat
    st.write(f'Hasil Pertambahan: {hasil}')
