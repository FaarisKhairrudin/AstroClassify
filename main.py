import streamlit as st
from modules import input_data, preprocessing, model_selection, classify_visualize, export

# Set konfigurasi halaman
st.set_page_config(
    page_title="AstroClassify",
    layout="wide",
    page_icon="🔭"
)

# Inisialisasi session_state page jika belum ada
if "page" not in st.session_state:
    st.session_state.page = "1. Input Data"

# Sidebar - Navigasi
st.sidebar.markdown("## 🚀 Navigasi")
page_options = [
    "1. Input Data",
    "2. Preprocessing",
    "3. Model & Evaluasi",
    "4. Klasifikasi & Visualisasi",
    "5. Export Hasil"
]
page = st.sidebar.radio("Pilih Halaman", page_options, index=page_options.index(st.session_state.page))

# Judul Utama
st.markdown("""
<h1 style='text-align: center;'>🔭 AstroClassify</h1>
<h4 style='text-align: center; color: gray;'>Aplikasi Klasifikasi Objek Astronomi Berbasis Machine Learning</h4>
<hr style='margin-top: 0;'>
""", unsafe_allow_html=True)

# Tampilkan halaman sesuai navigasi
if page == "1. Input Data":
    st.session_state.page = page
    input_data.show()

elif page == "2. Preprocessing":
    st.session_state.page = page
    preprocessing.show()

elif page == "3. Model & Evaluasi":
    st.session_state.page = page
    model_selection.show()

elif page == "4. Klasifikasi & Visualisasi":
    st.session_state.page = page
    classify_visualize.show()

elif page == "5. Export Hasil":
    st.session_state.page = page
    export.show()

# Tombol "Next" di bawah untuk berpindah halaman (jika belum di akhir)
next_index = page_options.index(st.session_state.page) + 1
if next_index < len(page_options):
    st.markdown("---")
    col1, col2 = st.columns([5, 1])
    with col2:
        if st.button("➡️ Lanjut ke " + page_options[next_index].split(". ")[1]):
            st.session_state.page = page_options[next_index]
            st.rerun()
