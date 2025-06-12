import streamlit as st
import pandas as pd
import plotly.express as px

X_features = ['alpha', 'delta', 'u', 'g', 'r', 'i', 'z', 'redshift']

def show():
    st.title("🔧 Preprocessing Data")
    st.caption("Menyiapkan data astronomi untuk model machine learning 🌌")

    if "uploaded_data" not in st.session_state or st.session_state.uploaded_data is None:
        st.warning("🚫 Silakan upload atau input data terlebih dahulu.")
        return

    df = st.session_state.uploaded_data.copy()

    with st.expander("📋 Lihat Data Asli"):
        st.dataframe(df, use_container_width=True)

    st.markdown("### ✅ Status Preprocessing")
    st.info("Preprocessing akan menangani missing value dan menyusun fitur agar siap digunakan oleh model.")

    with st.expander("🔍 Rincian Missing Value dan Langkah Preprocessing"):
        # Missing value sebelum preprocessing
        st.markdown("#### ❗ Missing Values Sebelum Preprocessing")
        missing = df[X_features].isnull().sum()
        if missing.sum() == 0:
            st.success("✅ Tidak ada nilai yang hilang.")
        else:
            fig = px.bar(
                x=missing.index,
                y=missing.values,
                labels={'x': 'Fitur', 'y': 'Jumlah Missing'},
                title="📉 Missing Value per Fitur",
                color=missing.values,
                color_continuous_scale="reds"
            )
            st.plotly_chart(fig, use_container_width=True)

        # Penjelasan proses
        st.markdown("#### 🛠️ Langkah-langkah Preprocessing")
        st.markdown("""
        - **Fitur yang digunakan:** `alpha`, `delta`, `u`, `g`, `r`, `i`, `z`, `redshift`
        - **Penanganan Missing Value:** Diisi dengan **median** dari dataset pelatihan (`star_classification.csv`)
        - **Normalisasi:** Tidak dilakukan karena model berbasis tree (XGBoost, LightGBM, Random Forest)
        """)

    # Proses preprocessing
    with st.spinner("🔄 Memproses data..."):
        df = df[X_features]
        try:
            training_df = pd.read_csv("data/star_classification.csv")
            median_values = training_df[X_features].median()
            df.fillna(median_values, inplace=True)
        except Exception as e:
            st.error("❌ Gagal memuat median dari data training. Pastikan file `data/star_classification.csv` tersedia.")
            return

    st.success("✅ Preprocessing selesai! Data siap digunakan untuk model.")

    with st.expander("📊 Lihat Data Setelah Preprocessing"):
        st.dataframe(df, use_container_width=True)

    # Simpan ke session_state
    st.session_state.processed_data = df.astype(float)
