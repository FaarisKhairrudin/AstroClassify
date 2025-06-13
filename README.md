# 🌌 AstroClassify

Bayangkan Anda sedang mengamati langit malam, penuh dengan cahaya bintang, galaksi jauh, dan objek misterius seperti quasar.  
Tapi... bagaimana cara membedakan semua itu hanya dari angka?

**AstroClassify** hadir sebagai jawabannya.

Dengan dukungan teknologi *machine learning*, aplikasi ini memungkinkan Anda untuk:

- 🔬 Mengklasifikasikan objek langit hanya dari data pengamatan
- 🚀 Menjelajahi galaksi, bintang, dan quasar dengan cara baru
- 📊 Memahami struktur kosmos tanpa harus jadi astronom profesional

---

## ✨ Siapa yang Cocok Menggunakan AstroClassify?

- 🧑‍🎓 Mahasiswa yang sedang belajar astronomi atau data science  
- 🔭 Pengamat langit amatir yang penasaran terhadap objek di langit  
- 🧑‍🔬 Peneliti yang butuh klasifikasi objek secara cepat dan akurat  

---

## 🛠️ Fitur Utama

- Upload data pengamatan bintang dalam format CSV
- Preprocessing otomatis
- Pemilihan model klasifikasi terbaik (Random Forest, XGBoost, LightGBM)
- Visualisasi hasil klasifikasi
- Ekspor hasil prediksi

---

## 📁 Struktur Proyek
```
astroclassify/
├── assets/
│   ├── astro_logo.png
├── data/
│   └── star_classification.csv
├── evaluation/
│   ├── lgb_classification_report.txt
│   ├── lgb_confusion_matrix.png
│   ├── rf_classification_report.txt
│   ├── rf_confusion_matrix.png
│   ├── xgb_classification_report.txt
│   └── xgb_confusion_matrix.png
├── models/
│   ├── best_model_params.json
│   ├── lgb_model.pkl
│   ├── rf_model.pkl
│   └── xgb_model.pkl
├── modules/
│   ├── classify_visualize.py
│   ├── export.py
│   ├── input_data.py
│   ├── intro_page.py
│   ├── model_selection.py
│   └── preprocessing.py
├── training/
│   └── train_models.ipynb
├── utils/
│   └── helpers.py
├── main.py
├── README.md
└── requirements.txt 
```

## 🚀 Cara Menjalankan Aplikasi

1. **Clone repository ini:**
   ```
   git clone https://github.com/FaarisKhairrudin/AstroClassify.git
   cd AstroClassify
   ```
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Jalankan aplikasi:**
   ```
   streamlit run main.py
   ```

## 📚 Dataset
Dataset yang digunakan berasal dari observasi spektrum cahaya bintang yang berisi fitur numerik dan label klasifikasi objek langit (GALAXY, STAR, QSO). Disimpan di dalam folder data/.

## 📃 Lisensi
Proyek ini bersifat open-source untuk tujuan pembelajaran dan pengembangan.
Lisensi mengikuti standar MIT License.

   
## 👥 Pembagian Tugas Tim (5 Orang)

### 1. **Input Data (modules/input_data.py)**
**Penanggung jawab:** Kevin Jonathan  
**Deskripsi Tugas:**
- Menyediakan fitur upload file CSV.
- Menyediakan form input manual untuk 1 data.
- Menyimpan hasil ke `st.session_state.uploaded_data`.

---

### 2. **Preprocessing & Modeling (modules/preprocessing.py)**
**Penanggung jawab:** Faaris Khairrudin  
**Deskripsi Tugas:**
- membuat model (`Random Forest`, `XGBoost`, `LightGBM`) dalam bentuk .pkl
- Menampilkan data asli.
- Menangani nilai hilang (imputasi/hapus).
- Melakukan normalisasi atau standardisasi.
- Menyimpan hasil ke `st.session_state.processed_data`.

---

### 3. **Model & prediction (modules/model_selection.py)**
**Penanggung jawab:** Farrell Faruqh Efendi.  
**Deskripsi Tugas:**
- Menampilkan pilihan model (`Random Forest`, `XGBoost`, `LightGBM`) via dropdown.
- Menampilkan metrik evaluasi model (.png(confussion matrix) dan .txt(classification report)) yang sudah ditraining sebelumnya pada folder evaluation.
- klasifikasi menggunakan selected model yang ada pada folder `models/`
- Menyimpan hasil klasifikasi ke `st.session_state.prediction`.
---

### 4. ** Visualisasi (modules/classify_visualize.py)**
**Penanggung jawab:** Fauzan Ahsanudin Alfikri.  
**Deskripsi Tugas:**
- Menampilkan hasil dengan visualisasi dari hasil prediksi:
  - Hasil Prediksi (jika 1 baris, muncul tulisan hasil klasifikasi nya saja, kalau df tampilkan keseluruhan)
  - 3D Scatter Plot (α, δ, z)
  - Histogram spektral berdasarkan kelas
- Menyimpan hasil visualisasi ke `st.session_state.visualisasi`.

---

### 5. **Export Hasil (modules/export.py)**
**Penanggung jawab:** Muhammad Fikri Hanif  
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

