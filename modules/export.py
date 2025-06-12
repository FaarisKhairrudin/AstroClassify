import streamlit as st
import pandas as pd
import io
import os

def to_excel(df: pd.DataFrame):
    """
    Mengonversi DataFrame ke format Excel (in-memory).
    """
    output = io.BytesIO()
    # Menggunakan 'with' memastikan writer ditutup dengan benar
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Hasil Prediksi')
    processed_data = output.getvalue()
    return processed_data

def show():
    """
    Menampilkan halaman untuk mengekspor hasil prediksi dan visualisasi.
    """
    st.header("🚀 Ekspor Hasil")

    st.markdown("---")
    st.subheader("📦 Unduh Hasil Prediksi")

    # Skenario 4: Cek apakah data hasil klasifikasi kosong/tidak valid
    if "predicted" not in st.session_state or st.session_state.predicted.empty:
        st.error("❌ Data hasil klasifikasi kosong/tidak valid untuk diunduh.")
        st.warning("ℹ️ Silakan lakukan prediksi pada halaman '🧠 Pemilihan & Evaluasi Model' terlebih dahulu.")
    else:
        df = st.session_state.predicted
        st.success("✅ Data hasil prediksi siap untuk diunduh.")
        st.dataframe(df.head(), use_container_width=True) # Menampilkan pratinjau data

        col1, col2, col3 = st.columns(3)

        # Skenario 1: Tombol unduh hasil klasifikasi sebagai CSV
        with col1:
            st.download_button(
                label="📥 Unduh CSV",
                data=df.to_csv(index=False, encoding='utf-8'),
                file_name='hasil_klasifikasi.csv',
                mime='text/csv',
                help="Unduh hasil klasifikasi dalam format CSV."
            )

        # Skenario 2: Tombol unduh hasil klasifikasi sebagai XLSX
        with col2:
            excel_data = to_excel(df)
            st.download_button(
                label="📥 Unduh XLSX",
                data=excel_data,
                file_name='hasil_klasifikasi.xlsx',
                mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                help="Unduh hasil klasifikasi dalam format Excel."
            )

        # Skenario 3: Tombol unduh hasil klasifikasi sebagai JSON
        with col3:
            st.download_button(
                label="📥 Unduh JSON",
                data=df.to_json(orient='records', indent=4, force_ascii=False).encode('utf-8'),
                file_name='hasil_klasifikasi.json',
                mime='application/json',
                help="Unduh hasil klasifikasi dalam format JSON."
            )

    st.markdown("---")
    st.subheader("🖼️ Unduh Visualisasi")

    # Asumsi: Modul visualisasi akan menyimpan plot sebagai bytes di session_state
    # dengan nama 'plot_2d_bytes' dan 'plot_3d_bytes'.
    
    col_vis1, col_vis2 = st.columns(2)

    with col_vis1:
        if "path_histogram_2d" not in st.session_state or not os.path.exists(st.session_state["path_histogram_2d"]):
            st.error("❌ Grafik visualisasi 2D tidak tersedia, unduhan tidak dapat dilakukan.")
        else:
            with open(st.session_state["path_histogram_2d"], "rb") as f:
                st.download_button(
                    label="📥 Unduh Plot 2D (PNG)",
                    data=f.read(),
                    file_name="plot_klasifikasi_2d.png",
                    mime="image/png"
                )

    with col_vis2:
        if "path_scatter_3d" not in st.session_state or not os.path.exists(st.session_state["path_scatter_3d"]):
            st.error("❌ Grafik visualisasi 3D tidak tersedia, unduhan tidak dapat dilakukan.")
        else:
            with open(st.session_state["path_scatter_3d"], "rb") as f:
                st.download_button(
                    label="📥 Unduh Plot 3D (PNG)",
                    data=f.read(),
                    file_name="plot_klasifikasi_3d.png",
                    mime="image/png"
                )