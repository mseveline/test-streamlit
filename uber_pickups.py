import streamlit as st

st.title('Kalkulator Sederhana')

# Input field untuk memasukkan angka pertama
angka1 = st.number_input('Masukkan Angka Pertama')

# Input field untuk memasukkan angka kedua
angka2 = st.number_input('Masukkan Angka Kedua')

# Tombol untuk menghitung hasil pertambahan
if st.button('Hitung'):
    hasil = angka1 + angka2
    st.write(f'Hasil Pertambahan: {hasil}')
