# 🌌 AstroClassify

<img width="1856" height="1035" alt="image" src="https://github.com/user-attachments/assets/10df098b-4d34-4320-8071-0af746c2c585" />


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

