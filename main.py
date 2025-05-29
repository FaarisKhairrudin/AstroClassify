import streamlit as st
from modules import input_data, preprocessing, model_selection, classify_visualize, export

st.set_page_config(page_title="AstroClassify", layout="wide")
st.title("🔭 AstroClassify - Aplikasi Klasifikasi Objek Astronomi")

# Sidebar Navigation
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", [
    "1. Input Data",
    "2. Preprocessing",
    "3. Model & Evaluasi",
    "4. Klasifikasi & Visualisasi",
    "5. Export Hasil"
])

# Routing to each module
if page == "1. Input Data":
    input_data.show()

elif page == "2. Preprocessing":
    preprocessing.show()

elif page == "3. Model & Evaluasi":
    model_selection.show()

elif page == "4. Klasifikasi & Visualisasi":
    classify_visualize.show()

elif page == "5. Export Hasil":
    export.show()
