
## 👥 Pembagian Tugas Tim (5 Orang)

### 1. **Input Data (modules/input_data.py)**
**Penanggung jawab:** [Nama Anggota 1]  
**Deskripsi Tugas:**
- Menyediakan fitur upload file CSV.
- Menyediakan form input manual untuk 1 data.
- Menyimpan hasil ke `st.session_state.uploaded_data`.

---

### 2. **Preprocessing (modules/preprocessing.py)**
**Penanggung jawab:** [Nama Anggota 2]  
**Deskripsi Tugas:**
- Menampilkan data asli.
- Menangani nilai hilang (imputasi/hapus).
- Melakukan normalisasi atau standardisasi.
- Menyimpan hasil ke `st.session_state.processed_data`.

---

### 3. **Model & Evaluasi (modules/model_selection.py)**
**Penanggung jawab:** [Nama Anggota 3]  
**Deskripsi Tugas:**
- Menampilkan pilihan model (`Random Forest`, `XGBoost`, `LightGBM`) via dropdown.
- Menampilkan metrik evaluasi model (.png/.csv) yang sudah ditraining sebelumnya.
- Menyimpan pilihan model ke `st.session_state.selected_model`.

---

### 4. **Klasifikasi & Visualisasi (modules/classify_visualize.py)**
**Penanggung jawab:** [Nama Anggota 4]  
**Deskripsi Tugas:**
- Memuat model terpilih dari folder `models/`.
- Melakukan prediksi terhadap `processed_data`.
- Menampilkan hasil dengan visualisasi:
  - 3D Scatter Plot (α, δ, z)
  - Histogram spektral berdasarkan kelas
- Menyimpan hasil klasifikasi ke `st.session_state.prediction`.

---

### 5. **Export Hasil (modules/export.py)**
**Penanggung jawab:** [Nama Anggota 5]  
**Deskripsi Tugas:**
- Menyediakan tombol untuk mengunduh hasil klasifikasi (.csv).
- Menyediakan tombol unduh visualisasi (.png).

---

## 🚀 Menjalankan Aplikasi

1. Clone repositori ini.
2. Install dependensi:
   ```bash
   pip install -r requirements.txt
