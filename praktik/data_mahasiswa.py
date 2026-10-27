def cari_mahasiswa(data, nim):
    return data.get(nim)


def rata_rata_nilai(data):
    if len(data) == 0:
        return 0

    total = 0
    for info in data.values():
        total += info["nilai"]

    return total / len(data)


data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}

nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)

print("=== PENCARIAN DATA MAHASISWA ===")
if hasil is not None:
    print(f"NIM   : {nim_cari}")
    print(f"Nama  : {hasil['nama']}")
    print(f"Kelas : {hasil['kelas']}")
    print(f"Nilai : {hasil['nilai']}")
else:
    print("Data tidak ditemukan")


print("\n=== PENCARIAN NIM TIDAK TERSEDIA ===")
nim_cari = "A999"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)

if hasil is not None:
    print(f"Data ditemukan: {hasil}")
else:
    print(f"Data mahasiswa dengan NIM {nim_cari} tidak ditemukan")


data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}

print("\n=== PENAMBAHAN DATA MAHASISWA ===")
print("Mahasiswa A006 berhasil ditambahkan")


data_mahasiswa["A002"]["nilai"] = 82

print("\n=== PEMBARUAN NILAI ===")
print(f"Nilai Budi setelah diperbarui: {data_mahasiswa['A002']['nilai']}")


print("\n=== SELURUH DATA MAHASISWA ===")
for nim, info in data_mahasiswa.items():
    print(
        f"NIM: {nim} | "
        f"Nama: {info['nama']} | "
        f"Kelas: {info['kelas']} | "
        f"Nilai: {info['nilai']}"
    )


print("\n=== RATA-RATA NILAI ===")
print(f"Rata-rata nilai mahasiswa: {rata_rata_nilai(data_mahasiswa):.2f}")