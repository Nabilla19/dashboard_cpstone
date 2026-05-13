# Data Dictionary - MindEase Mental Health Dataset

Dokumen ini adalah panduan teknis yang menjelaskan setiap variabel dalam dataset MindEase. Kamus data ini digunakan untuk memastikan konsistensi interpretasi data selama tahap analisis dan pengembangan model Machine Learning.

---

## Bagaimana Data Ini Dikumpulkan?

Dalam aplikasi MindEase, pengguna **tidak menginput angka secara langsung**. Mereka menjawab **kuesioner Smart Assessment** berupa pertanyaan pilihan/skala. Sistem kemudian mengubah jawaban tersebut menjadi nilai numerik untuk setiap variabel di bawah ini.

Contoh alur:
- User menjawab: *"Seberapa sering kamu merasa tertekan karena ujian? (1-10)"* → Sistem simpan sebagai `exam_pressure = 8`
- User menjawab: *"Berapa jam kamu tidur tadi malam?"* → Sistem simpan sebagai `sleep_hours = 5`
- Setelah semua dijawab → **Model AI memprediksi** → `risk_level = "High"`

---

## Tabel Variabel

### 🟦 Fitur Input (Dihasilkan dari Jawaban Kuesioner User)

| Nama Kolom | Deskripsi | Tipe Data | Keterangan & Range Nilai |
| :--- | :--- | :--- | :--- |
| `age` | Usia responden pada saat pengambilan data. | Integer | Rentang **18 - 30** tahun. |
| `gender` | Identitas gender responden. | String | Kategori: **Male, Female, Other**. |
| `academic_year` | Tingkat tahun studi mahasiswa di universitas. | Integer | Tahun ke **1, 2, 3, atau 4**. |
| `study_hours_per_day` | Rata-rata waktu belajar mandiri dalam satu hari. | Float | Satuan **Jam** (0 - 12 jam). |
| `exam_pressure` | Tingkat tekanan yang dirasakan akibat ujian dan tugas akademik. | Float | Skala **0 - 10** (10 = Tekanan sangat ekstrem). |
| `academic_performance` | Nilai rata-rata atau skor performa akademik mahasiswa. | Float | Skala **0 - 100** (Persentase pencapaian). |
| `stress_level` | Tingkat stres emosional yang dirasakan secara keseluruhan. | Float | Skala **0 - 10** (10 = Stres sangat tinggi). |
| `anxiety_score` | Skor tingkat kecemasan berdasarkan asesmen psikologis. | Float | Skala **0 - 10** (10 = Kecemasan klinis tinggi). |
| `depression_score` | Skor indikator gejala depresi berdasarkan asesmen psikologis. | Float | Skala **0 - 10** (10 = Gejala depresi berat). |
| `sleep_hours` | Rata-rata durasi tidur efektif setiap malam. | Float | Satuan **Jam** (0 - 10 jam). |
| `physical_activity` | Intensitas keterlibatan dalam aktivitas fisik/olahraga. | Float | Skala **0 - 10** (10 = Sangat aktif berolahraga). |
| `social_support` | Kualitas dukungan dari teman, keluarga, atau lingkungan sekitar. | Float | Skala **0 - 10** (10 = Dukungan sangat kuat). |
| `screen_time` | Total waktu yang dihabiskan di depan layar perangkat digital per hari. | Float | Satuan **Jam** (0 - 24 jam). |
| `internet_usage` | Total waktu penggunaan internet untuk aktivitas non-studi per hari. | Float | Satuan **Jam** (0 - 24 jam). |
| `financial_stress` | Tingkat kekhawatiran terkait kondisi keuangan pribadi/keluarga. | Float | Skala **0 - 10** (10 = Kesulitan finansial berat). |
| `family_expectation` | Tekanan yang dirasakan akibat ekspektasi dari keluarga. | Float | Skala **0 - 10** (10 = Ekspektasi sangat membebani). |
| `burnout_score` | Tingkat kelelahan fisik dan mental akibat aktivitas yang berkepanjangan. | Float | Skala **0 - 10** (10 = Kejenuhan/burnout total). |
| `mental_health_index` | Skor komposit yang merepresentasikan indeks kesehatan mental secara umum. | Float | Skala **0 - 10** (10 = Kondisi mental sangat sehat). |
| `dropout_risk` | Estimasi risiko mahasiswa untuk berhenti kuliah berdasarkan faktor yang ada. | Float | Skala **0 - 10** (10 = Risiko dropout sangat tinggi). |

---

### 🟥 Output Model (Hasil Prediksi AI — Tidak Diinput oleh User)

| Nama Kolom | Deskripsi | Tipe Data | Keterangan |
| :--- | :--- | :--- | :--- |
| `risk_level` | Klasifikasi tingkat risiko kesehatan mental yang **diprediksi oleh model AI** berdasarkan seluruh fitur input di atas. | Categorical | **Low** (Risiko Rendah), **Medium** (Risiko Sedang), **High** (Risiko Tinggi — perlu perhatian segera). |

---

## Catatan Kesiapan Data untuk Model

Berdasarkan kamus data di atas, data sudah siap untuk diproses karena:
1. **Struktur Konsisten**: Semua fitur numerik berada pada skala yang jelas (mayoritas 0-10).
2. **Target Jelas**: Variabel `risk_level` sudah terdefinisi sebagai **output/target klasifikasi**.
3. **Data Bersih**: Tidak ada nilai kosong (*missing values*) yang tersisa dalam dataset.
