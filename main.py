import streamlit as st
from modules import input_data, preprocessing, model_selection, classify_visualize, export, intro_page

# Konfigurasi halaman utama
st.set_page_config(
    page_title="AstroClassify",
    layout="wide",
    page_icon="🔭"
)

# Inisialisasi state
if "page" not in st.session_state:
    st.session_state.page = "0. Tentang Aplikasi"

# Sidebar Navigasi
with st.sidebar:
    st.image("./assets/astro_logo.png", width=120)  # Ukuran ideal di sidebar

    st.markdown("## 🚀 Navigasi")
    page_options = [
        "0. Tentang Aplikasi",
        "1. Input Data",
        "2. Preprocessing",
        "3. Model & Evaluasi",
        "4. Klasifikasi & Visualisasi",
        "5. Export Hasil"
    ]

    selected_page = st.radio("📂 Pilih Halaman", page_options, index=page_options.index(st.session_state.page))
    st.markdown("---")
    st.info("📌 Navigasi akan menyimpan progres otomatis.", icon="💾")

# Header Aplikasi
st.markdown("""
    <div style='text-align: center; padding: 10px 0;'>
        <h1 style='margin-bottom: 0;'>🔭 AstroClassify</h1>
        <h4 style='color: gray;'>Aplikasi Klasifikasi Objek Astronomi Berbasis Machine Learning</h4>
    </div>
    <hr>
""", unsafe_allow_html=True)


# Routing
st.session_state.page = selected_page

if selected_page == "1. Input Data":
    input_data.show()
elif selected_page == "2. Preprocessing":
    preprocessing.show()
elif selected_page == "3. Model & Evaluasi":
    model_selection.show()
elif selected_page == "4. Klasifikasi & Visualisasi":
    classify_visualize.show()
elif selected_page == "5. Export Hasil":
    export.show()
elif selected_page == "0. Tentang Aplikasi":
    intro_page.show()



# Tombol Navigasi ke Halaman Selanjutnya
next_index = page_options.index(st.session_state.page) + 1
if next_index < len(page_options):
    st.markdown("---")
    col1, col2 = st.columns([5, 1])
    with col2:
        if st.button(f"➡️ Lanjut ke {page_options[next_index].split('. ')[1]}"):
            st.session_state.page = page_options[next_index]
            st.rerun()
