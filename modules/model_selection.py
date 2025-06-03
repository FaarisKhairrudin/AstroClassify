# modules/model_selection.py

import streamlit as st
import pandas as pd
from PIL import Image
import os

def show():
    st.header("🧠 Pemilihan & Evaluasi Model")

    if "processed_data" not in st.session_state or st.session_state.processed_data is None:
        st.warning("⚠️ Silakan lakukan preprocessing terlebih dahulu.")
        return

    # Dropdown model
    model_options = ["Random Forest", "XGBoost", "LightGBM"]
    selected_model = st.selectbox("🔽 Pilih model klasifikasi yang akan digunakan:", model_options)
    
    # Simpan ke session_state
    st.session_state.selected_model = selected_model
    st.success(f"Model yang dipilih: {selected_model}")

    # Menampilkan gambar evaluasi jika ada
    st.subheader("🖼️ Visualisasi Evaluasi (jika tersedia)")
    image_filename = {
        "Random Forest": "confusion_matrix_rf.png",
        "XGBoost": "confusion_matrix_xgb.png",      # ← tambahkan nanti jika tersedia
        "LightGBM": "confusion_matrix_lgbm.png"     # ← tambahkan nanti jika tersedia
    }.get(selected_model, None)

    image_path = os.path.join("assets", image_filename) if image_filename else None
    if image_path and os.path.exists(image_path):
        st.image(Image.open(image_path), caption=f"Confusion Matrix - {selected_model}")
    else:
        st.info("Belum ada visualisasi evaluasi untuk model ini.")

    # Menampilkan tabel metrik dari CSV
    st.subheader("📈 Metrik Evaluasi Model")
    csv_path = os.path.join("assets", "metrics_table.csv")
    if os.path.exists(csv_path):
        df_metrics = pd.read_csv(csv_path)

        # Jika ada kolom 'model', filter berdasarkan pilihan
        if 'model' in df_metrics.columns:
            filtered = df_metrics[df_metrics['model'] == selected_model]
            if not filtered.empty:
                st.dataframe(filtered)
            else:
                st.warning("Metrik untuk model ini tidak tersedia di file CSV.")
        else:
            st.dataframe(df_metrics)  # fallback jika hanya 1 model
    else:
        st.warning("File metrics_table.csv tidak ditemukan.")
