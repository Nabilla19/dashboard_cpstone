# Data Dictionary - MindEase Mental Health Dataset

Dokumen ini adalah panduan teknis yang menjelaskan setiap variabel dalam dataset **MindEase**. Kamus data ini digunakan untuk memastikan konsistensi interpretasi data selama tahap analisis dan pengembangan model Machine Learning.

| Nama Kolom | Deskripsi | Tipe Data | Keterangan & Range Nilai |
| :--- | :--- | :--- | :--- |
| `age` | Usia responden pada saat pengambilan data. | Integer | Rentang **18 - 30** tahun. |
| `gender` | Identitas gender responden. | String | Kategori: **Male, Female, Other**. |
| `academic_year` | Tingkat tahun studi atau semester mahasiswa di universitas. | Integer | Tahun ke **1, 2, 3, atau 4**. |
| `study_hours_per_day` | Rata-rata waktu yang dihabiskan untuk belajar secara mandiri dalam satu hari. | Float | Satuan **Jam** (0 - 12 jam). |
| `exam_pressure` | Tingkat tekanan atau beban yang dirasakan akibat ujian atau tugas akademik. | Float | Skala **0 - 10** (10 = Tekanan sangat ekstrem). |
| `academic_performance` | Nilai rata-rata kumulatif atau skor performa akademik mahasiswa. | Float | Skala **0 - 100** (Persentase pencapaian). |
| `stress_level` | Indikator tingkat stres emosional yang dirasakan secara keseluruhan. | Float | Skala **0 - 10** (10 = Stres sangat tinggi). |
| `anxiety_score` | Skor hasil asesmen psikologis untuk mengukur tingkat kecemasan. | Float | Skala **0 - 10** (10 = Kecemasan klinis tinggi). |
| `depression_score` | Skor hasil asesmen psikologis untuk mengukur indikator gejala depresi. | Float | Skala **0 - 10** (10 = Gejala depresi berat). |
| `sleep_hours` | Rata-rata durasi tidur efektif yang didapatkan responden setiap malam. | Float | Satuan **Jam** (0 - 10 jam). |
| `physical_activity` | Frekuensi atau intensitas keterlibatan dalam aktivitas fisik/olahraga. | Float | Skala **0 - 10** (10 = Sangat aktif berolahraga). |
| `social_support` | Ketersediaan dan kualitas dukungan dari teman, keluarga, atau lingkungan. | Float | Skala **0 - 10** (10 = Dukungan sangat kuat). |
| `screen_time` | Total waktu yang dihabiskan di depan layar perangkat digital per hari. | Float | Satuan **Jam** (0 - 24 jam). |
| `internet_usage` | Total waktu penggunaan koneksi internet untuk aktivitas non-studi per hari. | Float | Satuan **Jam** (0 - 24 jam). |
| `financial_stress` | Tingkat kekhawatiran atau kesulitan terkait kondisi keuangan pribadi/keluarga. | Float | Skala **0 - 10** (10 = Kesulitan finansial berat). |
| `family_expectation` | Besarnya tekanan yang dirasakan responden akibat ekspektasi dari keluarga. | Float | Skala **0 - 10** (10 = Ekspektasi sangat membebani). |
| `burnout_score` | Tingkat kelelahan fisik dan mental akibat aktivitas berkepanjangan. | Float | Skala **0 - 10** (10 = Kejenuhan/burnout total). |
| `mental_health_index` | Skor komposit yang mewakili indeks kesehatan mental secara umum. | Float | Skala **0 - 10** (10 = Kondisi mental sangat sehat). |
| `risk_level` | **Target Utama**: Klasifikasi tingkat risiko kesehatan mental mahasiswa. | Categorical | **Low** (Rendah), **Medium** (Sedang), **High** (Tinggi). |
| `dropout_risk` | Estimasi kemungkinan mahasiswa untuk berhenti kuliah berdasarkan faktor terkait. | Float | Skala **0 - 10** (10 = Risiko dropout sangat tinggi). |

---

## Catatan Tambahan untuk Kesiapan Model
Berdasarkan Kamus Data di atas, data sudah siap untuk diproses lebih lanjut karena:
1. **Struktur Konsisten**: Semua fitur numerik berada pada skala yang jelas (mayoritas 0-10).
2. **Target Jelas**: Variabel `risk_level` sudah terdefinisi sebagai target klasifikasi.
3. **Data Bersih**: Tidak ada nilai kosong (*missing values*) yang tersisa dalam dataset ini.
