# 🌌 AstroClassify

AstroClassify adalah aplikasi klasifikasi objek astronomi berbasis **Streamlit** yang menggunakan **model machine learning terlatih (.pkl)** untuk mengklasifikasikan objek langit seperti **Bintang**, **Galaksi**, dan **Quasar** berdasarkan data spektral.

## 📁 Struktur Proyek

```
astroclassify/
├── main.py
├── models/
│ └── model_random_forest.pkl
│ └── model_xgboost.pkl
│ └── model_lightgbm.pkl
├── data/
│ └── example_input.csv
├── modules/
│ ├── input_data.py
│ ├── preprocessing.py
│ ├── model_selection.py
│ ├── classify_visualize.py
│ └── export.py
├── assets/
│ └── confusion_matrix_rf.png
│ └── metrics_table.csv
├── requirements.txt
└── README.md
```

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

## Panduan Kerja Tim Proyek AstroClassify di GitHub

Dokumen ini berisi panduan langkah demi langkah bagi anggota tim untuk berkolaborasi dalam proyek AstroClassify menggunakan GitHub.

### 1. Clone Repository

Setelah repository dibuat dan diunggah ke GitHub oleh ketua tim (leader), setiap anggota tim perlu melakukan *clone* repository ke komputer lokal masing-masing. Buka terminal atau command prompt Anda dan jalankan perintah berikut, ganti `<URL_REPOSITORY>` dengan URL repository AstroClassify dari GitHub:

```bash
git clone <URL_REPOSITORY>
cd astroclassify
```

Contoh:
```
git clone [https://github.com/faariskhairrudin/astroclassify.git](https://github.com/faariskhairrudin/astroclassify.git)
cd astroclassify
```
### 2. Buat Branch Masing-Masing

Setiap anggota tim wajib membuat branch baru untuk setiap fitur atau tugas yang dikerjakan. Ini bertujuan untuk mengisolasi perubahan dan mencegah konflik langsung pada branch utama (main).

Gunakan perintah berikut untuk membuat dan berpindah ke branch baru, ganti <nama-branch> dengan nama branch sesuai dengan fitur yang Anda kerjakan:
```
git checkout -b <nama-branch>
```
Contoh Penamaan Branch:
```
Nama Anggota	Nama Branch	Fitur
Anggota 1	data-input	Upload/Input Data
Anggota 2	preprocessing	Preprocessing
Anggota 3	model-selection	Pemilihan Model
Anggota 4	visualization	Visualisasi Hasil
Anggota 5	export-result	Ekspor Hasil
```
Pastikan nama branch deskriptif dan mudah dipahami.

### 3. Kerjakan Fitur di Branch Masing-Masing

Setelah berada di branch Anda, kerjakan file atau modul yang telah ditugaskan. Penting untuk tidak mengubah file utama (main.py) secara langsung di branch Anda. Fokuslah pada file-file yang relevan dengan fitur yang sedang Anda kembangkan.

### 4. Commit Perubahan

Setelah Anda menyelesaikan sebagian atau seluruh fitur yang dikerjakan di branch Anda, simpan perubahan Anda ke local repository menggunakan perintah git commit.

Pertama, tambahkan file-file yang telah Anda ubah atau buat ke staging area:
```
git add .
```
Atau, jika Anda ingin menambahkan file tertentu saja:
```
git add <nama_file>
```
Kemudian, lakukan commit dengan pesan yang jelas dan informatif mengenai perubahan yang Anda lakukan:
```
git commit -m "<pesan commit yang deskriptif>"
```

Contoh Pesan Commit yang Baik:

    Implement fitur upload data dengan validasi format file.
    Menambahkan fungsi untuk melakukan preprocessing data numerik.
    Memperbarui script untuk pemilihan model dengan opsi Random Forest dan SVM.
    Membuat visualisasi scatter plot untuk hasil klasifikasi.
    Menambahkan fungsionalitas ekspor hasil ke format CSV.

### 5. Push Branch ke GitHub

Setelah Anda melakukan commit perubahan di local repository, langkah selanjutnya adalah mengunggah branch Anda ke remote repository di GitHub. Gunakan perintah berikut, ganti <nama-branch> dengan nama branch Anda:
```
git push origin <nama-branch>
```
Contoh:
```
git push origin data-input
```

### 6. Buat Pull Request (PR)

Setelah fitur Anda selesai dan branch Anda telah di-push ke GitHub, langkah terakhir adalah membuat Pull Request (PR).

- Buka halaman repository AstroClassify di GitHub melalui web browser
-  Anda akan melihat notifikasi tentang branch Anda yang baru saja di-push. Klik tombol "Compare & pull request".
-  Pada halaman pembuatan Pull Request:
   -  Pastikan base repository adalah faariskhairrudin/astroclassify dan base adalah main.
   -  Pastikan compare repository adalah faariskhairrudin/astroclassify dan compare adalah branch Anda (misalnya, data-input).
   -  Berikan judul Pull Request yang jelas dan ringkas mengenai fitur yang Anda kerjakan.
   -  Tulis deskripsi yang detail mengenai perubahan yang Anda lakukan, alasan perubahan tersebut, dan hal-hal lain yang perlu diketahui oleh leader
-  Klik tombol "Create pull request".

Setelah Pull Request dibuat, ketua tim (leader) akan menerima notifikasi dan akan melakukan review terhadap kode Anda. Jika ada perubahan yang perlu diperbaiki, leader akan memberikan feedback pada Pull Request. Lakukan perbaikan yang diminta dengan melakukan commit dan push lagi ke branch Anda. Perubahan ini akan otomatis terupdate di Pull Request.

Setelah review selesai dan disetujui, leader akan melakukan merge (menggabungkan) branch Anda ke branch main. Setelah di-merge, fitur Anda akan menjadi bagian dari proyek utama.


---

## 🚀 Menjalankan Aplikasi

1. Clone repositori ini.
2. Install dependensi:
   ```bash
   pip install -r requirements.txt
