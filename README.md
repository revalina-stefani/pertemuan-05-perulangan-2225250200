Pertemuan 05 Perulangan Python

Nama: [Revalina Stefani]
NIM: 2225250200
Kelas: [3B]

Tujuan

Menggunakan perulangan for dan while.

Menggunakan range().

Menggunakan seleksi if.

Menggunakan akumulasi dan pencacahan.

Melakukan validasi input.

Cara Menjalankan
py latihan/01_tabel_perkalian.py
py latihan/02_jumlah_bilangan.py
py latihan/03_validasi_input.py
py latihan/04_hitung_genap.py
py kuis/kuis2_deret_aritmetika.py

Algoritma Kuis 2
# Input
* Suku pertama a
* Beda d
* Banyak suku n

# Proses
* Validasi n menggunakan while
* Menghasilkan n suku menggunakan for
* Menghitung setiap suku
* Menjumlahkan semua suku

# Kondisi berhenti
* Perulangan for selesai setelah n suku
* Perulangan while berhenti ketika n > 0

# Output
* Nomor setiap suku
* Nilai setiap suku
* Jumlah seluruh suku

Hasil Pengujian
# Latihan 1 - Tabel Perkalian

* n = 4
  Hasil: 4 x 1 sampai 4 x 10

* n = -3
  Hasil: -3 x 1 sampai -3 x 10


# Latihan 2 - Jumlah Bilangan

* n = 1
  Hasil: Jumlah = 1

* n = 5
  Hasil: Jumlah = 15

* n = 10
  Hasil: Jumlah = 55


# Latihan 3 - Validasi Input

* Input: 120
  Hasil: Tidak valid

* Input: -5
  Hasil: Tidak valid

* Input: 75
  Hasil: Nilai diterima


# Latihan 4 - Menghitung Bilangan Genap

* n = 1
  Hasil: 0

* n = 2
  Hasil: 1

* n = 5
  Hasil: 2

* n = 10
  Hasil: 5


# Kuis 2 - Deret Aritmetika

* a = 2, d = 3, n = 5
  Hasil: 2, 5, 8, 11, 14
  Jumlah: 40

* a = 10, d = -2, n = 4
  Hasil: 10, 8, 6, 4
  Jumlah: 28

* a = 1.5, d = 0.5, n = 3
  Hasil: 1.5, 2.0, 2.5
  Jumlah: 6

* n = 0
  Hasil: Ditolak sampai n lebih dari 0

Refleksi
# Kesalahan yang ditemukan

* Saya sebelumnya menjalankan file Python secara langsung di terminal.
* Perintah yang benar adalah menggunakan py.

Contoh:

py latihan/01_tabel_perkalian.py

# Pemahaman

* range(1, 11) menghasilkan angka 1 sampai 10.
* Batas akhir range tidak ikut dihitung.
* while digunakan untuk validasi input.
* for digunakan ketika jumlah perulangan sudah diketahui.

Refleksi Teknis
# Bagian mana yang menentukan jumlah iterasi?

* Pada for, jumlah iterasi ditentukan oleh range().
* Pada Kuis 2, range(n) berjalan sebanyak n kali.

# Mengapa total harus diinisialisasi sebelum loop?

* Karena total digunakan sebagai akumulator.
* Nilai total harus disiapkan sebelum proses penjumlahan dimulai.

# Apa akibatnya jika total = 0 berada di dalam loop?

* Total akan kembali menjadi 0 setiap iterasi.
* Hasil penjumlahan sebelumnya akan hilang.

# Mengapa validasi n menggunakan while?

* Karena jumlah percobaan input tidak diketahui.
* Program terus meminta input sampai n > 0.

# Bagaimana membuktikan loop berhenti?

* for berhenti setelah n iterasi selesai.
* while berhenti ketika kondisi n <= 0 menjadi False.

Status
Latihan 1  : Selesai
Latihan 2  : Selesai
Latihan 3  : Selesai
Latihan 4  : Selesai
Kuis 2     : Selesai
README     : Selesai