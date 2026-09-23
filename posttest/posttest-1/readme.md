# Sistem Manajemen Pesanan Desain Grafis — Desaignkan_id

Program Python berbasis **Object-Oriented Programming (OOP)** untuk mengelola pesanan
jasa desain grafis pada usaha kreatif fiktif **Desaignkan_id**, berdasarkan jenis layanan
(logo, banner, ilustrasi, dll).

Materi yang diterapkan:
- **Modul 1** — Class & Object
- **Modul 2** — Atribut (instance & kelas) dan Method (instance, class, static)
- **Modul 3** — Encapsulation (public, protected, private) & Property (getter/setter)

---

## 1. Struktur Class

Program terdiri dari **3 class utama** yang berdiri sendiri, namun saling berinteraksi
melalui objek (tanpa inheritance):

### a. `JenisLayanan`
Merepresentasikan satu jenis layanan desain grafis yang dijual Desaignkan_id.

| Jenis | Nama | Keterangan |
|---|---|---|
| Atribut Kelas | `nama_platform`, `total_layanan_terdaftar`, `diskon_member_default`, `kategori_valid` | Data dipakai bersama semua objek |
| Atribut Instance | `nama_layanan`, `kategori`, `estimasi_hari` (public), `__harga_dasar` (private) | Unik tiap objek |
| Instance Method | `tampilkan_info()`, `hitung_harga_setelah_diskon()` | Menampilkan & mengolah data objek |
| Class Method | `dari_dict()` (factory), `ubah_diskon_member()` | Membuat objek dari dict / ubah atribut kelas |
| Static Method | `validasi_kategori()` | Cek kategori layanan valid |
| Property | `harga_dasar` (getter & setter dengan validasi harga > 0) | |

### b. `Desainer`
Merepresentasikan seorang desainer grafis di Desaignkan_id.

| Jenis | Nama | Keterangan |
|---|---|---|
| Atribut Kelas | `nama_instansi`, `total_desainer`, `level_default` | Data dipakai bersama semua objek |
| Atribut Instance | `nama`, `spesialisasi`, `level` (public), `__rating`, `__jumlah_pesanan_selesai` (private) | Unik tiap objek |
| Instance Method | `tampilkan_profil()`, `tambah_pesanan_selesai()` | Menampilkan & mengubah data objek |
| Class Method | `dari_dict()` (factory), `ubah_level_default()` | Membuat objek dari dict / ubah atribut kelas |
| Static Method | `validasi_nama()` | Cek nama tidak kosong |
| Property | `rating` (getter & setter dengan validasi 0–5) | |

### c. `Pesanan`
Merepresentasikan satu transaksi pesanan pelanggan. Menggunakan **objek `JenisLayanan`
dan `Desainer`** sebagai atributnya (interaksi antar objek).

| Jenis | Nama | Keterangan |
|---|---|---|
| Atribut Kelas | `nama_instansi`, `total_pesanan`, `ongkos_admin`, `status_valid` | Data dipakai bersama semua objek |
| Atribut Instance | `id_pesanan`, `nama_pelanggan`, `layanan`, `desainer`, `is_member` (public), `__status`, `__total_bayar` (private) | Unik tiap objek |
| Instance Method | `proses_pesanan()`, `selesaikan_pesanan()`, `tampilkan_struk()` | Mengolah & menampilkan data objek |
| Class Method | `dari_data()` (factory), `reset_total_pesanan()` | Membuat objek / reset atribut kelas |
| Static Method | `validasi_id_pesanan()` | Cek format ID pesanan diawali "ORD" |
| Property | `status` (getter & setter dengan validasi status), `total_bayar` (getter/read-only) | |

---

## 2. Konsep Encapsulation yang Diterapkan

- **Public** — misal `nama_layanan`, `nama`, `id_pesanan`, dapat diakses langsung dari luar class.
- **Private** — misal `__harga_dasar`, `__rating`, `__status`, `__total_bayar`, dilindungi
  dengan *name mangling* Python dan hanya bisa diubah lewat method/`@property` setter
  yang sudah divalidasi.
- **Getter & Setter idiomatis** — menggunakan `@property` dan `@nama.setter` (nama fungsi
  getter dan setter identik), setiap setter memiliki validasi data. Jika data tidak valid,
  perubahan ditolak dan program mencetak pesan peringatan (bukan menghentikan program).

---

## 3. Cara Menjalankan Program

Pastikan Python 3 sudah terpasang, lalu jalankan dari terminal:

```bash
python3 main.py
```

Tidak ada dependency eksternal — program hanya memakai Python standar.

---

## 4. Panduan Pengujian (Main Code)

Bagian `if __name__ == "__main__":` di `main.py` melakukan demonstrasi berikut,
urut sesuai output di terminal:

1. **Pembuatan objek `JenisLayanan`** — 2 objek (`layanan_logo` dibuat langsung via
   konstruktor, `layanan_banner` dibuat via class method factory `dari_dict()`).
   Memanggil instance method (`tampilkan_info`), static method (`validasi_kategori`),
   dan class method (`ubah_diskon_member`).
2. **Pembuatan objek `Desainer`** — 2 objek (`desainer_dea` via konstruktor,
   `desainer_bima` via factory `dari_dict()`). Memanggil instance, static, dan class method.
3. **Pembuatan objek `Pesanan`** — 2 objek yang masing-masing menggunakan objek
   `JenisLayanan` & `Desainer` di atas (`pesanan_1` via konstruktor,
   `pesanan_2` via factory `dari_data()`). Memanggil `proses_pesanan()`,
   `selesaikan_pesanan()`, dan `tampilkan_struk()`.
4. **Pengujian getter & setter** — untuk `harga_dasar`, `rating`, dan `status`:
   - Input **valid** → data berhasil diperbarui, tercetak pesan `[OK]`.
   - Input **tidak valid** (harga negatif, rating di luar 0–5, status tidak dikenal)
     → perubahan **ditolak**, tercetak pesan `[GAGAL]`, dan nilai lama tetap dipertahankan.
5. **Class method tambahan** — `reset_total_pesanan()` untuk mengubah atribut kelas
   `Pesanan.total_pesanan` kembali ke 0.

Untuk menguji skenario lain, Anda dapat mengubah nilai pada bagian main program,
misalnya mencoba `layanan_logo.harga_dasar = 0` atau `desainer_bima.rating = -1`
untuk memastikan validasi tetap konsisten.

---

## 5. Struktur File

```
.
├── main.py       # Seluruh kode program (class + demo pengujian)
└── README.md     # Dokumentasi ini
```