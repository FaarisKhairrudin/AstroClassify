import streamlit as st
import pandas as pd

# Fitur yang digunakan dalam model
X_features = ['alpha','delta','u','g','r','i','z','redshift']

def show():
    st.header("🔧 Preprocessing Data")

    if "uploaded_data" not in st.session_state or st.session_state.uploaded_data is None:
        st.warning("Silakan upload atau input data terlebih dahulu.")
        return

    # Ambil data yang diupload
    df = st.session_state.uploaded_data.copy()
    
    st.subheader("📋 Data Asli")
    st.dataframe(df)

    with st.expander("ℹ️ Penjelasan Preprocessing", expanded=False):
        st.markdown("""
        - Hanya fitur berikut yang digunakan: `alpha`, `delta`, `u`, `g`, `r`, `i`, `z`, dan `redshift`.
        - Nilai hilang akan diisi menggunakan median dari dataset training (`star_classification.csv`).
        - Tidak dilakukan normalisasi karena model yang digunakan adalah tree-based.
        """)

    # Mulai preprocessing
    with st.spinner("🔄 Sedang memproses data..."):
        # Ambil hanya kolom yang digunakan di model
        df = df[X_features]

        # Load median dari data training
        try:
            training_df = pd.read_csv("data/star_classification.csv")
            median_values = training_df[X_features].median()
            df.fillna(median_values, inplace=True)
        except Exception as e:
            st.error("Gagal memuat median dari data training. Pastikan file 'star_classification.csv' tersedia.")
            return

    st.success("✅ Preprocessing selesai.")
    st.subheader("📊 Data Setelah Preprocessing")
    st.dataframe(df)

    # Simpan hasil ke session_state
    st.session_state.processed_data = df
