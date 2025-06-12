import streamlit as st

def show():
    # Logo tengah
    st.markdown("""
        <div style="text-align: center;">
            <img src='https://raw.githubusercontent.com/FaarisKhairrudin/AstroClassify/main/assets/astro_logo.png' width='290'>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("## ✨ Selamat Datang di **AstroClassify**")
    st.markdown("---")

    st.markdown("""
    Bayangkan Anda sedang mengamati langit malam, penuh dengan cahaya bintang, galaksi jauh, dan objek misterius seperti quasar.  
    Tapi... bagaimana cara membedakan semua itu hanya dari angka?

    **AstroClassify** hadir sebagai jawaban.

    Dengan dukungan teknologi *machine learning*, aplikasi ini memungkinkan Anda untuk:
    - 🔬 Mengklasifikasikan objek langit hanya dari data pengamatan
    - 🚀 Menjelajahi galaksi, bintang, dan quasar dengan cara baru
    - 📊 Memahami struktur kosmos tanpa harus jadi astronom profesional

    Aplikasi ini dirancang untuk siapa saja yang ingin memahami alam semesta melalui data:
    - 🧑‍🎓 Mahasiswa yang sedang belajar astronomi atau data science
    - 🔭 Pengamat langit amatir yang penasaran terhadap objek di langit
    - 🧑‍🔬 Peneliti yang butuh klasifikasi objek secara cepat dan akurat

    ---

    ### 🌌 Sumber Data

    AstroClassify menggunakan dataset dari **Sloan Digital Sky Survey (SDSS)** —  
    survei langit terbesar dan paling komprehensif yang telah memetakan jutaan objek di alam semesta.

    Data dari SDSS menyediakan informasi penting seperti:
    - Posisi langit (`alpha`, `delta`)
    - Magnitudo cahaya pada berbagai filter (`u`, `g`, `r`, `i`, `z`)
    - Jarak relatif dalam bentuk `redshift`

    ---

    ### 🚀 Siap memulai eksplorasi kosmik Anda?
    """)

    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    if st.button("🌠 Mulai Klasifikasi Sekarang"):
        st.session_state.page = "1. Input Data"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
