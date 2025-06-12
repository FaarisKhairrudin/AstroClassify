import streamlit as st
import os
import joblib
import random

def show():
    st.header("🧠 Pemilihan & Evaluasi Model")

    # Validasi: Pastikan data sudah di-preprocess
    if "processed_data" not in st.session_state or st.session_state.processed_data is None:
        st.warning("⚠️ Silakan lakukan preprocessing terlebih dahulu sebelum memilih model.")
        return

    # Daftar model
    model_map = {
        "Random Forest": "rf",
        "XGBoost": "xgb",
        "LightGBM": "lgb"
    }

    model_options = list(model_map.keys())
    selected_model_name = st.selectbox("🔽 Pilih model klasifikasi:", model_options)
    model_prefix = model_map[selected_model_name]

    st.session_state.selected_model = model_prefix

    # === Ganti bagian ini dengan expander ===
    with st.expander("📊 Tampilkan Evaluasi Model"):
        st.markdown("💡 <i>Lihat performa modelmu sebelum melangkah lebih jauh!</i>", unsafe_allow_html=True)

        cm_path = os.path.join("evaluation", f"{model_prefix}_confusion_matrix.png")
        report_path = os.path.join("evaluation", f"{model_prefix}_classification_report.txt")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📉 Confusion Matrix")
            if os.path.exists(cm_path):
                st.image(cm_path, caption="Confusion Matrix", use_container_width=True)
            else:
                st.warning("❌ File confusion matrix tidak ditemukan.")

        with col2:
            st.subheader("📄 Classification Report")
            if os.path.exists(report_path):
                with open(report_path, "r") as f:
                    report = f.read()
                st.text_area("Hasil Evaluasi", report, height=300, label_visibility="collapsed")
            else:
                st.warning("❌ File classification report tidak ditemukan.")
    # === Selesai ganti tombol evaluasi ===

    # === Ganti bagian tombol prediksi jadi expander ===
    with st.expander("🔮 Prediksi Data"):
        st.markdown("📌 <i>Prediksi bukan sekadar angka — ini tentang mengungkap misteri kosmos 🌌</i>", unsafe_allow_html=True)

        model_path = os.path.join("models", f"{model_prefix}_model.pkl")

        if os.path.exists(model_path):
            # Lakukan prediksi
            st.session_state.predicted = st.session_state.processed_data.copy()
            model = joblib.load(model_path)

            # Mapping dan prediksi
            label_map = {0: 'GALAXY', 1: 'QSO', 2: 'STAR'}
            predicted_labels = model.predict(st.session_state.processed_data)
            st.session_state.predicted = st.session_state.processed_data.copy()
            st.session_state.predicted["class"] = predicted_labels

            # Tampilkan hasil
            st.subheader("📋 Hasil Prediksi")

            # Narasi menarik jika hanya 1 data
            if len(st.session_state.predicted) == 1:
                kelas = label_map[predicted_labels[0]]

                st.markdown(f"### 🧾 HASIL PREDIKSI: **{kelas}**")

                if kelas == "GALAXY":
                    st.info("🌌 **Fun Fact:** Galaksi terbesar yang diketahui, IC 1101, memiliki diameter lebih dari 400.000 tahun cahaya! Itu sekitar 4 kali lebih besar dari Bima Sakti. 😮")
                elif kelas == "QSO":
                    st.info("✨ **Fun Fact:** QSO (Quasar) bersinar lebih terang dari seluruh galaksi, meskipun ukurannya jauh lebih kecil. Dipicu oleh lubang hitam supermasif! 🔭")
                elif kelas == "STAR":
                    st.info("⭐ **Fun Fact:** Bintang paling terang di langit malam adalah Sirius. Tapi ada bintang yang lebih besar dari matahari kita hingga 2.000 kali! 🔥")

            else:
                # Narasi tambahan untuk banyak data
                st.success("📈 Data berhasil diprediksi! Yuk cek kelas objek astronominya di bawah ini ⬇️")

                # Daftar fun fact acak
                fun_facts = [
                    "🔭 Beberapa bintang bisa meledak dalam ledakan supernova yang melepaskan lebih banyak energi daripada matahari selama jutaan tahun.",
                    "🌠 Ada lebih banyak bintang di alam semesta daripada butiran pasir di semua pantai di Bumi!",
                    "🌌 Galaksi Andromeda sedang menuju ke galaksi kita dan akan bertabrakan dalam sekitar 4 miliar tahun.",
                    "🌟 Cahaya dari bintang terjauh yang bisa kita lihat butuh miliaran tahun untuk sampai ke Bumi.",
                    "🛰️ Teleskop luar angkasa seperti Hubble telah mengubah cara kita memahami alam semesta."
                ]
                st.info(random.choice(fun_facts))

            # Tampilkan tabel
            st.dataframe(st.session_state.predicted)

        else:
            st.error(f"❌ Model {selected_model_name} tidak ditemukan di {model_path}.")
    # === Selesai ganti tombol prediksi ===
