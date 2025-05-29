import streamlit as st
import pandas as pd

# Tempat penyimpanan state data
if 'uploaded_data' not in st.session_state:
    st.session_state.uploaded_data = None

def show():
    st.header("🪐 Input Data Astronomi")

    st.subheader("🔼 Upload Dataset (CSV)")
    uploaded_file = st.file_uploader("Unggah file CSV berisi data objek astronomi", type=["csv"])
    
    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state.uploaded_data = df
            st.success("Dataset berhasil diunggah!")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Terjadi kesalahan saat membaca file: {e}")

    st.markdown("---")
    st.subheader("✍️ Input Manual Data (Opsional)")
    with st.form(key="manual_input_form"):
        alpha = st.number_input("Right Ascension (α)", format="%.6f")
        delta = st.number_input("Declination (δ)", format="%.6f")
        u = st.number_input("Magnitudo (u)")
        g = st.number_input("Magnitudo (g)")
        r = st.number_input("Magnitudo (r)")
        i = st.number_input("Magnitudo (i)")
        z = st.number_input("Magnitudo (z)")
        submit = st.form_submit_button("Tambah ke Dataset")

    if submit:
        new_row = pd.DataFrame([{
            "alpha": alpha,
            "delta": delta,
            "u": u,
            "g": g,
            "r": r,
            "i": i,
            "z": z
        }])

        if st.session_state.uploaded_data is not None:
            st.session_state.uploaded_data = pd.concat([st.session_state.uploaded_data, new_row], ignore_index=True)
        else:
            st.session_state.uploaded_data = new_row

        st.success("Data berhasil ditambahkan!")
        st.dataframe(st.session_state.uploaded_data)
