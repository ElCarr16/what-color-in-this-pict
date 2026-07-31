# What Color in This Pict? (Screenshot Color Picker CLI)

![Python Version](https://img.shields.io/badge/python-3.14+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Sebuah aplikasi Command Line Interface (CLI) berbasis Python yang dapat mendeteksi warna-warna paling dominan langsung dari *clipboard* (hasil screenshot `Win + Shift + S` atau *Copy Image*) tanpa perlu menyimpan file gambar terlebih dahulu. Aplikasi ini juga dilengkapi dengan *live preview* kotak warna asli langsung di dalam terminal menggunakan kode warna ANSI.

---

## 🚀 Deskripsi Proyek

Aplikasi ini dibuat untuk mempermudah developer, desainer, atau pencari warna dalam mengambil kode warna (HEX) dari area layar mana pun secara instan. Menggunakan algoritma *Machine Learning*, sistem akan membedah jutaan piksel gambar hasil *screenshot* yang ada di memori *clipboard*, mengelompokkannya, dan mengekstrak 5 warna utama yang paling dominan.

---

## 🛠️ Tech Stack & Pustaka

Aplikasi ini memanfaatkan ekosistem Python modern dan beberapa pustaka pihak ketiga:

* **Python 3.14+**: Versi bahasa pemrograman utama yang digunakan.
* **Pillow (PIL - ImageGrab)**: Bertugas untuk mengambil dan membaca data gambar secara langsung dari *clipboard* sistem operasi tanpa perantara file fisik.
* **NumPy**: Digunakan untuk mengubah struktur data gambar dari Pillow menjadi matriks angka (array 3D) agar pikselnya bisa diolah secara matematis.
* **Scikit-Learn (K-Means Clustering)**: Algoritma *Machine Learning* yang digunakan untuk mengelompokkan jutaan variasi warna piksel yang mirip menjadi beberapa kelompok warna utama (default: 5 warna dominan).
* **ANSI Escape Codes (True Color 24-bit)**: Digunakan untuk merender kotak warna visual sebagai latar belakang spasi di terminal, memberikan representasi warna asli tepat di sebelah kode HEX.

---

## 💻 Instalasi & Persiapan

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di komputer lokal Anda:

### 1. Kloning Repositori
Buka terminal atau Command Prompt (CMD), lalu kloning repositori ini:
* `git clone https://github.com/ElCarr16/what-color-in-this-pict.git`
* `cd what-color-in-this-pict`

### 2. Buat & Aktifkan Virtual Environment (Disarankan)
Agar pustaka proyek terisolasi dengan rapi dan tidak mengganggu global environment, buatlah *virtual environment*:
* **Windows (PowerShell)**:
  * `python -m venv venv`
  * `.\venv\Scripts\Activate.ps1`
* **Windows (CMD)**:
  * `python -m venv venv`
  * `.\venv\Scripts\activate.bat`
* **Linux/Mac**:
  * `python3 -m venv venv`
  * `source venv/bin/activate`

### 3. Instal Dependencies
Instal semua pustaka yang dibutuhkan menggunakan perintah pip lewat terminal Anda:
* `pip install pillow scikit-learn numpy`

---

## 🎯 Cara Penggunaan

1. Cari gambar, aset UI, atau objek apa saja yang ingin Anda ambil warnanya di layar monitor.
2. Lakukan *screenshot* pada area tersebut menggunakan kombinasi tombol **`Windows + Shift + S`** (atau klik kanan gambar di browser lalu pilih **Copy Image**).
3. Jalankan aplikasi melalui terminal Anda:
   * `python app.py`
4. Kembali ke terminal, lalu tekan **[ENTER]** jika gambar sudah siap di *clipboard*.
5. Sistem akan otomatis menganalisis piksel dan menampilkan hasilnya berupa daftar warna dominan beserta kode HEX dan visual warnanya di terminal.
6. **Fitur Perulangan:** Setelah output muncul, sistem akan bertanya `Pick color again? (y/n) [default: y]:`. 
   * Tekan **Enter** atau ketik **`y`** untuk mengambil screenshot warna baru lagi.
   * Ketik **`n`** untuk menghentikan program secara rapi.

---

## 📝 Catatan Penting untuk Windows User
Aplikasi ini menggunakan modul `os.system('')` di awal kode untuk mengaktifkan dukungan *ANSI Virtual Terminal Sequences* pada Windows Command Prompt (CMD) versi lama. Fitur kotak warna akan langsung berjalan optimal di terminal modern seperti **VS Code Terminal**, **Windows Terminal**, maupun CMD bawaan Windows 10/11 terbaru.
