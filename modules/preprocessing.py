# modules/preprocessing.py

import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocessing_section():
    st.header("🔧 Preprocessing Data")

    if "uploaded_data" not in st.session_state or st.session_state.uploaded_data is None:
        st.warning("Silakan upload atau input data terlebih dahulu.")
        return

    df = st.session_state.uploaded_data.copy()
    st.subheader("📋 Data Asli")
    st.dataframe(df)

    # Tangani nilai hilang
    st.subheader("🧹 Penanganan Nilai Hilang")
    method = st.radio("Pilih metode penanganan:", ["Imputasi dengan rata-rata", "Hapus baris yang tidak lengkap"])

    if method == "Imputasi dengan rata-rata":
        df.fillna(df.mean(numeric_only=True), inplace=True)
        st.success("Nilai hilang diimputasi dengan rata-rata.")
    elif method == "Hapus baris yang tidak lengkap":
        df.dropna(inplace=True)
        st.success("Baris dengan nilai hilang telah dihapus.")

    st.write("Data setelah penanganan nilai hilang:")
    st.dataframe(df)

    # Normalisasi / Standarisasi
    st.subheader("⚖️ Normalisasi / Standarisasi")
    scale_method = st.radio("Pilih metode skala fitur:", ["Standarisasi (Z-score)", "Tanpa normalisasi"])

    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if scale_method == "Standarisasi (Z-score)":
        scaler = StandardScaler()
        df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
        st.success("Fitur numerik telah distandarisasi.")

    st.write("Data setelah preprocessing:")
    st.dataframe(df)

    # Simpan ke session_state untuk digunakan di modul lain
    st.session_state.processed_data = df
