import streamlit as st
import random

st.title("Prediksi Nomor 4D Berdasarkan Seed")

seed_val = st.number_input("Masukkan seed (angka):", min_value=0, step=1)

if st.button("Prediksi Nomor"):
    random.seed(seed_val)

    def generate_4d_number():
        return "".join(str(random.randint(0,9)) for _ in range(4))

    nomor_list = [generate_4d_number() for _ in range(4)]

    st.write(f"Nomor 1 (keluar): {nomor_list[0]}")
    for i in range(1,4):
        st.write(f"Nomor {i+1} (prediksi): {nomor_list[i]}")
