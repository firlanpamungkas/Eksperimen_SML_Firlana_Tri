# Titanic Dataset Preprocessing Automation

## Deskripsi Proyek

Repository ini dibuat untuk memenuhi Kriteria 1 pada Submission Proyek Akhir Membangun Sistem Machine Learning (MSML) Dicoding.

Proyek menggunakan dataset Titanic untuk melakukan proses Exploratory Data Analysis (EDA) dan Data Preprocessing secara otomatis menggunakan Python dan GitHub Actions.

## Dataset

Dataset yang digunakan adalah Titanic Dataset yang berisi informasi penumpang kapal Titanic dan status keselamatan mereka.

Target prediksi:

* `Survived = 0` : Tidak Selamat
* `Survived = 1` : Selamat

## Tahapan Eksperimen

### 1. Data Loading

Memuat dataset Titanic menggunakan Pandas.

### 2. Exploratory Data Analysis (EDA)

Analisis dilakukan untuk:

* Memeriksa struktur dataset
* Memeriksa missing values
* Menganalisis distribusi target
* Menganalisis hubungan fitur dengan target
* Visualisasi data menggunakan Matplotlib dan Seaborn

### 3. Data Preprocessing

Tahapan preprocessing yang dilakukan:

* Menghapus kolom:

  * PassengerId
  * Name
  * Ticket
  * Cabin
* Menangani missing value:

  * Age → Median Imputation
  * Embarked → Mode Imputation
* Encoding fitur kategorikal:

  * Sex
  * Embarked
* Menyimpan hasil preprocessing ke file CSV baru

## Struktur Repository

```text
.
├── .github/
│   └── workflows/
│       └── preprocessing.yml
│
├── preprocessing/
│   ├── automate_firlana.py
│   ├── Eksperimen_firlana.ipynb
│   └── titanic_preprocessing.csv
│
├── titanic.csv
├── requirements.txt
└── README.md
```

## Automasi Preprocessing

Proses preprocessing dapat dijalankan secara otomatis menggunakan:

```bash
python preprocessing/automate_firlana.py
```

Output:

```text
Preprocessing selesai
Shape: (891, 8)
```

## GitHub Actions

Repository ini menggunakan GitHub Actions untuk menjalankan proses preprocessing secara otomatis setiap kali terdapat perubahan pada branch `main`.

Workflow:

```text
.github/workflows/preprocessing.yml
```

## Environment

* Python 3.12.7
* pandas
* numpy
* scikit-learn
* matplotlib
* seaborn
* mlflow 2.19.0

## Author

Firlan
Submission Proyek Akhir Membangun Sistem Machine Learning - Dicoding

![Python](https://img.shields.io/badge/Python-3.12-blue)
![MLflow](https://img.shields.io/badge/MLflow-2.19.0-orange)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-success)