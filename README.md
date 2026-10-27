
# Pertemuan 11 - Dictionary/Map

Nama: **Salsabila Thahira**
NIM: **2225250214**
Kelas: **3B**

## Tujuan
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data
Data mahasiswa disimpan menggunakan dictionary. NIM digunakan sebagai key utama untuk membedakan setiap mahasiswa, sedangkan value berupa dictionary yang berisi nama, kelas, dan nilai mahasiswa.

<table>
  <thead>
    <tr>
      <th>Key</th>
      <th>Value</th>
      <th>Keterangan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A001, A002, A003, A004, A005</td>
      <td>Dictionary mahasiswa</td>
      <td>NIM sebagai key utama untuk mencari data mahasiswa.</td>
    </tr>
    <tr>
      <td>nama</td>
      <td>Ayu, Budi, Citra, Deni, Eka, Fajar</td>
      <td>Menyimpan nama mahasiswa.</td>
    </tr>
    <tr>
      <td>kelas</td>
      <td>A atau B</td>
      <td>Menyimpan kelas mahasiswa.</td>
    </tr>
    <tr>
      <td>nilai</td>
      <td>Angka nilai mahasiswa</td>
      <td>Menyimpan nilai setiap mahasiswa.</td>
    </tr>
    <tr>
      <td>A006</td>
      <td>{"nama": "Fajar", "kelas": "B", "nilai": 80}</td>
      <td>Key baru yang ditambahkan ke dictionary.</td>
    </tr>
  </tbody>
</table>

## Cara Menjalankan
python3 praktik/data_mahasiswa.py

## Test Case

<table>
  <thead>
    <tr>
      <th>No.</th>
      <th>Input/Aksi</th>
      <th>Hasil yang Diharapkan</th>
      <th>Hasil Aktual</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Mencari NIM A003</td>
      <td>Data Citra, kelas B, nilai 92 ditampilkan.</td>
      <td>Data Citra, kelas B, nilai 92 ditampilkan.</td>
      <td>Berhasil</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Mencari NIM A999</td>
      <td>Menampilkan pesan Data tidak ditemukan.</td>
      <td>Data tidak ditemukan.</td>
      <td>Berhasil</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Menambahkan NIM A006</td>
      <td>Data Fajar tersimpan di dictionary.</td>
      <td>Data Fajar berhasil ditambahkan.</td>
      <td>Berhasil</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Mengubah nilai A002 menjadi 82</td>
      <td>Nilai Budi berubah menjadi 82.</td>
      <td>Nilai A002 berhasil diubah menjadi 82.</td>
      <td>Berhasil</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Menampilkan data dengan items()</td>
      <td>Seluruh data enam mahasiswa ditampilkan.</td>
      <td>Enam data mahasiswa ditampilkan.</td>
      <td>Berhasil</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Menghitung rata-rata nilai</td>
      <td>Rata-rata nilai seluruh mahasiswa adalah 83.17.</td>
      <td>Rata-rata nilai: 83.17.</td>
      <td>Berhasil</td>
    </tr>
  </tbody>
</table>

## Refleksi
Satu kesalahan akses key yang dapat terjadi adalah menggunakan data_mahasiswa["A999"] secara langsung ketika NIM tersebut tidak tersedia. Kesalahan ini menyebabkan KeyError. Cara memperbaikinya adalah menggunakan method get() melalui fungsi cari_mahasiswa(), kemudian memeriksa hasilnya dengan kondisi if agar program menampilkan pesan "Data tidak ditemukan" tanpa mengalami error.
