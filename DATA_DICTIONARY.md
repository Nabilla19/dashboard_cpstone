# Data Dictionary - MindEase Mental Health Dataset

Dokumen ini menjelaskan struktur data yang digunakan dalam proyek **MindEase Student Mental Health Dashboard**. Dataset ini berisi informasi mengenai kesehatan mental mahasiswa berdasarkan faktor akademik, gaya hidup, dan sosial.

| Nama Kolom | Deskripsi | Tipe Data | Contoh/Range |
| :--- | :--- | :--- | :--- |
| `age` | Usia mahasiswa | Integer | 18 - 30 |
| `gender` | Jenis kelamin mahasiswa | String | Male, Female, Other |
| `academic_year` | Tahun akademik (semester/tahun ke-n) | Integer | 1, 2, 3, 4 |
| `study_hours_per_day` | Rata-rata jam belajar per hari | Float | 0 - 12 |
| `exam_pressure` | Tingkat tekanan ujian (skala 0-10) | Float | 0 - 10 |
| `academic_performance` | Skor performa akademik | Float | 0 - 100 |
| `stress_level` | Skor tingkat stres (skala 0-10) | Float | 0 - 10 |
| `anxiety_score` | Skor tingkat kecemasan | Float | 0 - 10 |
| `depression_score` | Skor tingkat depresi | Float | 0 - 10 |
| `sleep_hours` | Rata-rata jam tidur per malam | Float | 0 - 10 |
| `physical_activity` | Frekuensi aktivitas fisik | Float | 0 - 10 |
| `social_support` | Skor dukungan sosial yang dirasakan | Float | 0 - 10 |
| `screen_time` | Durasi waktu layar per hari (jam) | Float | 0 - 24 |
| `internet_usage` | Durasi penggunaan internet per hari (jam) | Float | 0 - 24 |
| `financial_stress` | Skor tingkat stres finansial | Float | 0 - 10 |
| `family_expectation` | Skor tekanan ekspektasi keluarga | Float | 0 - 10 |
| `burnout_score` | Skor tingkat kejenuhan mental (burnout) | Float | 0 - 10 |
| `mental_health_index` | Indeks kesehatan mental keseluruhan | Float | 0 - 10 |
| `risk_level` | **Target Variable**: Klasifikasi risiko | Categorical | Low, Medium, High |
| `dropout_risk` | Prediksi risiko putus kuliah | Float | 0 - 10 |

---

## Langkah Kesiapan Model (Model Readiness)
Untuk memastikan data siap diproses oleh model Machine Learning, langkah-langkah berikut disarankan:

1. **Feature Encoding**: Mengubah kolom kategorikal (`gender`, `risk_level`) menjadi numerik menggunakan *One-Hot Encoding* atau *Label Encoding*.
2. **Scaling/Normalization**: Karena variabel seperti `academic_performance` (skala 100) dan `stress_level` (skala 10) memiliki rentang yang berbeda, disarankan menggunakan *StandardScaler* atau *MinMaxScaler*.
3. **Handling Class Imbalance**: Jika distribusi `risk_level` tidak seimbang (misalnya kategori High sangat sedikit), pertimbangkan teknik *SMOTE* atau *Oversampling*.
4. **Feature Selection**: Berdasarkan EDA, variabel `stress_level`, `anxiety_score`, dan `sleep_hours` adalah fitur yang paling berpengaruh.
