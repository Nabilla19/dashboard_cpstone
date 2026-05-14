# Data Dictionary - MindEase Mental Health Dataset (Advanced Version)

Dokumen ini menjelaskan struktur data untuk dataset **mental_health_featured.csv**. Dataset ini berisi 25 kolom, yang terdiri dari 20 kolom original dan 5 kolom hasil **Feature Engineering** untuk meningkatkan akurasi analisis dan model.

---

## 🟦 Fitur Input Original (20 Kolom)

| Nama Kolom | Deskripsi | Tipe Data | Keterangan & Range Nilai |
| :--- | :--- | :--- | :--- |
| `age` | Usia responden pada saat pengambilan data. | Integer | 18 - 30 tahun. |
| `gender` | Identitas gender responden. | String | Male, Female, Other. |
| `academic_year` | Tahun studi mahasiswa di universitas. | Integer | Tahun ke 1, 2, 3, atau 4. |
| `study_hours_per_day` | Rata-rata waktu belajar mandiri per hari. | Float | Satuan Jam (0 - 12). |
| `exam_pressure` | Tingkat tekanan akibat ujian/tugas akademik. | Float | Skala 0 - 10 (10 = Ekstrem). |
| `academic_performance` | Skor performa akademik mahasiswa. | Float | Skala 0 - 100. |
| `stress_level` | Skor stres emosional secara keseluruhan. | Float | Skala 0 - 10. |
| `anxiety_score` | Skor tingkat kecemasan psikologis. | Float | Skala 0 - 10. |
| `depression_score` | Skor gejala depresi psikologis. | Float | Skala 0 - 10. |
| `sleep_hours` | Rata-rata durasi tidur per malam. | Float | Satuan Jam (0 - 10). |
| `physical_activity` | Intensitas aktivitas fisik/olahraga. | Float | Skala 0 - 10. |
| `social_support` | Kualitas dukungan dari lingkungan sekitar. | Float | Skala 0 - 10. |
| `screen_time` | Total waktu di depan layar digital per hari. | Float | Satuan Jam (0 - 24). |
| `internet_usage` | Penggunaan internet non-studi per hari. | Float | Satuan Jam (0 - 24). |
| `financial_stress` | Tingkat kekhawatiran kondisi keuangan. | Float | Skala 0 - 10. |
| `family_expectation` | Tekanan akibat ekspektasi keluarga. | Float | Skala 0 - 10. |
| `burnout_score` | Tingkat kelelahan fisik dan mental. | Float | Skala 0 - 10. |
| `mental_health_index` | Indeks kesehatan mental secara umum. | Float | Skala 0 - 10 (10 = Sehat). |
| `dropout_risk` | Estimasi risiko berhenti kuliah. | Float | Skala 0 - 10. |

---

## 🟧 Fitur Baru - Feature Engineering (5 Kolom Tambahan)

Kolom-kolom di bawah ini dibuat secara manual (*Engineered*) untuk membantu model memahami pola data dengan lebih tajam.

| Nama Kolom | Deskripsi | Tipe Data | Keterangan / Logika |
| :--- | :--- | :--- | :--- |
| `sleep_category` | Pengelompokan kualitas tidur berdasarkan jam tidur. | String | **Kurang** (<6 jam), **Cukup** (6-8 jam), **Baik** (>8 jam). |
| `screen_time_category` | Pengelompokan penggunaan gadget per hari. | String | **Normal** (<=6 jam), **Berlebih** (>6 jam). |
| `stress_category` | Kategorisasi tingkat stres berdasarkan skor stres. | String | **Low** (0-3), **Medium** (4-7), **High** (>7). |
| `mental_risk_score` | Skor risiko gabungan dari stres, kecemasan, dan depresi. | Float | Hasil kalkulasi rata-rata tertimbang fitur-fitur risiko. |
| `support_category` | Pengelompokan tingkat dukungan sosial. | String | **Low Support** (0-4), **High Support** (5-10). |

---

## 🟥 Output Model (Target Prediksi)

| Nama Kolom | Deskripsi | Tipe Data | Keterangan |
| :--- | :--- | :--- | :--- |
| `risk_level` | Klasifikasi tingkat risiko kesehatan mental akhir. | String | **Low, Medium, High** (Target Prediksi AI). |

---

## Kesimpulan Kesiapan Data
Dataset **featured** ini jauh lebih siap untuk model Machine Learning karena:
1.  **Kategorisasi**: Data numerik yang sudah dikelompokkan membantu algoritma menangani variasi data yang kecil.
2.  **Korelasi Baru**: Fitur seperti `mental_risk_score` memberikan perspektif gabungan yang lebih kuat dibanding fitur tunggal.
