# Sistem Manajemen Pesanan Desain Grafis — Desaignkan_id

Program Python berbasis **Object-Oriented Programming (OOP)** untuk mengelola pesanan
jasa desain grafis pada usaha kreatif fiktif **Desaignkan_id**, berdasarkan jenis layanan
(logo, banner, ilustrasi, dll).

Materi yang diterapkan:
- Modul 1 — Class & Object
- Modul 2 — Atribut (instance & kelas) dan Method (instance, class, static)
- Modul 3 — Encapsulation (public, protected, private) & Property (getter/setter)

---

## 1. Struktur Class

Program terdiri dari 3 class utama yang berdiri sendiri, namun saling berinteraksi
melalui objek (tanpa inheritance).

### a. JenisLayanan
Merepresentasikan satu jenis layanan desain grafis yang dijual.

- Atribut kelas: `nama_platform`, `total_layanan_terdaftar`, `diskon_member_default`,
  `kategori_valid`
- Atribut instance (public): `nama_layanan`, `kategori`, `estimasi_hari`
- Atribut instance (private): `__harga_dasar`
- Instance method: `tampilkan_info()`, `hitung_harga_setelah_diskon()`
- Class method: `dari_dict()` (factory), `ubah_diskon_member()`
- Static method: `validasi_kategori()`
- Property: `harga_dasar` (getter & setter, validasi harga harus > 0)

### b. Desainer
Merepresentasikan seorang desainer grafis di Desaignkan_id.

- Atribut kelas: `nama_instansi`, `total_desainer`, `level_default`
- Atribut instance (public): `nama`, `spesialisasi`, `level`
- Atribut instance (private): `__rating`, `__pesanan_selesai`
- Instance method: `tampilkan_profil()`, `tambah_pesanan_selesai()`
- Class method: `dari_dict()` (factory), `ubah_level_default()`
- Static method: `validasi_nama()`
- Property: `rating` (getter & setter, validasi nilai harus 0–5)

### c. Pesanan
Merepresentasikan satu transaksi pesanan pelanggan. Menggunakan objek `JenisLayanan`
dan `Desainer` sebagai atributnya (contoh interaksi antar objek).

- Atribut kelas: `nama_instansi`, `total_pesanan`, `ongkos_admin`, `status_valid`
- Atribut instance (public): `id_pesanan`, `nama_pelanggan`, `layanan`, `desainer`,
  `is_member`
- Atribut instance (private): `__status`, `__total_bayar`
- Instance method: `proses_pesanan()`, `selesaikan_pesanan()`, `tampilkan_struk()`
- Class method: `dari_data()` (factory), `reset_total_pesanan()`
- Static method: `validasi_id_pesanan()`
- Property: `status` (getter & setter dengan validasi), `total_bayar` (getter/read-only)

---

## 2. Konsep Encapsulation yang Diterapkan

- Public — misal `nama_layanan`, `nama`, `id_pesanan`, dapat diakses langsung dari luar
  class.
- Private — misal `__harga_dasar`, `__rating`, `__status`, `__total_bayar`, dilindungi
  dengan *name mangling* Python dan hanya bisa diubah lewat property setter yang sudah
  divalidasi.
- Getter & setter memakai `@property` dan `@nama.setter` (nama fungsi getter dan setter
  identik). Setiap setter punya validasi data; kalau data tidak valid, perubahan ditolak
  dan program mencetak pesan `[GAGAL]` tanpa menghentikan program.

---

## 3. Cara Menjalankan Program

Pastikan Python 3 sudah terpasang, lalu jalankan dari terminal:

```bash
python3 main.py
```

Tidak ada dependency eksternal, program hanya memakai Python standar.

---

## 4. Panduan Pengujian (Main Code)

Bagian `if __name__ == "__main__":` di `main.py` menjalankan demo berikut secara urut:

1. Membuat 2 objek `JenisLayanan` (satu lewat konstruktor biasa, satu lewat class
   method factory `dari_dict()`), lalu memanggil instance method, static method
   `validasi_kategori()`, dan class method `ubah_diskon_member()`.
2. Membuat 2 objek `Desainer` (satu lewat konstruktor, satu lewat factory
   `dari_dict()`), lalu memanggil instance method, static method `validasi_nama()`,
   dan class method `ubah_level_default()`.
3. Membuat 2 objek `Pesanan` yang masing-masing memakai objek `JenisLayanan` dan
   `Desainer` di atas (satu lewat konstruktor, satu lewat factory `dari_data()`), lalu
   memproses dan menyelesaikan pesanan serta menampilkan struknya.
4. Menguji getter & setter pada `harga_dasar`, `rating`, dan `status`:
   - Input valid → data berhasil diperbarui, tercetak pesan `[OK]`.
   - Input tidak valid (harga negatif, rating di luar 0–5, status tidak dikenal)
     → perubahan ditolak, tercetak pesan `[GAGAL]`, nilai lama tetap dipertahankan.
5. Memanggil class method `reset_total_pesanan()` untuk mengembalikan atribut kelas
   `Pesanan.total_pesanan` ke 0.

Untuk menguji skenario lain, ubah saja nilai pada bagian main program, misalnya coba
`layanan_logo.harga_dasar = 0` atau `desainer_bima.rating = -1` untuk memastikan
validasi tetap konsisten.

---

## 5. Struktur File

```
.
├── main.py       # Seluruh kode program (class + demo pengujian)
└── README.md     # Dokumentasi ini
```