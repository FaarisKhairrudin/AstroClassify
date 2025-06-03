# modules/model_selection.py

import streamlit as st

def show():
    st.header("🧠 Pemilihan & Evaluasi Model")

    # Validasi: Pastikan data sudah di-preprocess
    if "processed_data" not in st.session_state or st.session_state.processed_data is None:
        st.warning("⚠️ Silakan lakukan preprocessing terlebih dahulu sebelum memilih model.")
        return

    # Daftar model
    model_options = ["Random Forest", "XGBoost", "LightGBM"]

    # Dropdown pilihan model
    selected_model = st.selectbox("🔽 Pilih model klasifikasi:", model_options)

    # Simpan pilihan model ke session_state
    st.session_state.selected_model = selected_model

    # Tombol untuk mulai training / evaluasi
    if st.button("🔍 Train / Evaluasi"):
        # Simulasi proses evaluasi, misalnya tampilkan metrik dummy
        st.success(f"✅ Evaluasi model {selected_model} selesai.")
        st.write("Berikut hasil evaluasi model:")
        
        # Dummy metrik hasil evaluasi
        dummy_metrics = {
            "Accuracy": 0.88 if selected_model == "XGBoost" else 0.85,
            "Precision": 0.83,
            "Recall": 0.81,
            "F1-score": 0.82
        }

        for key, value in dummy_metrics.items():
            st.metric(label=key, value=f"{value:.2%}")

    # Jika tidak memilih model tapi klik evaluasi → gunakan default
    if "selected_model" not in st.session_state and st.button("Gunakan Model Default"):
        default_model = "XGBoost"
        st.session_state.selected_model = default_model
        st.info(f"Model default ({default_model}) digunakan.")
