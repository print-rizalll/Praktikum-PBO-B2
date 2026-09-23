class JenisLayanan:
    """Satu jenis layanan desain grafis yang dijual."""

    nama_platform = "Desaignkan_id"
    total_layanan_terdaftar = 0
    diskon_member_default = 0.1
    kategori_valid = ["Logo", "Banner", "Ilustrasi", "UI/UX", "Konten Sosmed"]

    def __init__(self, nama_layanan, kategori, harga_dasar, estimasi_hari):
        self.nama_layanan = nama_layanan   # public
        self.kategori = kategori           # public
        self.estimasi_hari = estimasi_hari  # public
        self.__harga_dasar = harga_dasar   # private
        JenisLayanan.total_layanan_terdaftar += 1

    @property
    def harga_dasar(self):
        return self.__harga_dasar

    @harga_dasar.setter
    def harga_dasar(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru <= 0:
            print(f"[GAGAL] Harga '{self.nama_layanan}' harus angka > 0.")
            return
        self.__harga_dasar = nilai_baru
        print(f"[OK] Harga '{self.nama_layanan}' diperbarui jadi Rp{nilai_baru:,.0f}")

    def tampilkan_info(self):
        print(f"Layanan: {self.nama_layanan} ({self.kategori}) - "
            f"Rp{self.__harga_dasar:,.0f} - estimasi {self.estimasi_hari} hari")

    def hitung_harga_setelah_diskon(self, is_member=False):
        if is_member:
            return self.__harga_dasar * (1 - JenisLayanan.diskon_member_default)
        return self.__harga_dasar

    @classmethod
    def dari_dict(cls, data):
        """Factory method: buat objek dari dictionary."""
        return cls(data["nama_layanan"], data["kategori"],
                    data["harga_dasar"], data["estimasi_hari"])

    @classmethod
    def ubah_diskon_member(cls, diskon_baru):
        if 0 <= diskon_baru < 1:
            cls.diskon_member_default = diskon_baru
            print(f"[OK] Diskon member jadi {diskon_baru*100:.0f}%")
        else:
            print("[GAGAL] Diskon harus desimal 0-1 (misal 0.1 = 10%)")

    @staticmethod
    def validasi_kategori(kategori):
        return kategori in JenisLayanan.kategori_valid


class Desainer:
    """Seorang desainer grafis di Desaignkan_id."""

    # Atribut kelas
    nama_instansi = "Desaignkan_id"
    total_desainer = 0
    level_default = "Junior"

    def __init__(self, nama, spesialisasi, rating_awal=5.0):
        self.nama = nama                     # public
        self.spesialisasi = spesialisasi     # public
        self.level = Desainer.level_default  # public
        self.__rating = rating_awal          # private
        self.__pesanan_selesai = 0           # private
        Desainer.total_desainer += 1

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or not (0 <= nilai_baru <= 5):
            print(f"[GAGAL] Rating {self.nama} harus angka 0-5.")
            return
        self.__rating = nilai_baru
        print(f"[OK] Rating {self.nama} diperbarui jadi {nilai_baru}")

    def tambah_pesanan_selesai(self):
        self.__pesanan_selesai += 1

    def tampilkan_profil(self):
        print(f"Desainer: {self.nama} | Spesialisasi: {self.spesialisasi} | "
            f"Level: {self.level} | Rating: {self.__rating} | "
            f"Selesai: {self.__pesanan_selesai}")

    @classmethod
    def dari_dict(cls, data):
        """Factory method: buat objek dari dictionary."""
        return cls(data["nama"], data["spesialisasi"], data.get("rating_awal", 5.0))

    @classmethod
    def ubah_level_default(cls, level_baru):
        cls.level_default = level_baru
        print(f"[OK] Level default desainer baru: '{level_baru}'")

    @staticmethod
    def validasi_nama(nama):
        return isinstance(nama, str) and len(nama.strip()) > 0


class Pesanan:
    """Satu transaksi pesanan desain dari pelanggan (memakai objek
    JenisLayanan & Desainer)."""
    nama_instansi = "Desaignkan_id"
    total_pesanan = 0
    ongkos_admin = 5000
    status_valid = ["Menunggu", "Diproses", "Selesai", "Dibatalkan"]

    def __init__(self, id_pesanan, nama_pelanggan, layanan, desainer, is_member=False):
        self.id_pesanan = id_pesanan          # public
        self.nama_pelanggan = nama_pelanggan  # public
        self.layanan = layanan                # public, objek JenisLayanan
        self.desainer = desainer              # public, objek Desainer
        self.is_member = is_member            # public
        self.__status = "Menunggu"            # private
        self.__total_bayar = 0                # private
        Pesanan.total_pesanan += 1

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        if status_baru not in Pesanan.status_valid:
            print(f"[GAGAL] Status '{status_baru}' tidak valid. Pilihan: {Pesanan.status_valid}")
            return
        self.__status = status_baru
        print(f"[OK] Status {self.id_pesanan} jadi '{status_baru}'")

    @property
    def total_bayar(self):
        return self.__total_bayar

    def proses_pesanan(self):
        harga = self.layanan.hitung_harga_setelah_diskon(self.is_member)
        self.__total_bayar = harga + Pesanan.ongkos_admin
        self.status = "Diproses"
        print(f"Pesanan {self.id_pesanan} diproses. Total: Rp{self.__total_bayar:,.0f}")

    def selesaikan_pesanan(self):
        if self.__status != "Diproses":
            print(f"[GAGAL] Pesanan {self.id_pesanan} belum diproses.")
            return
        self.status = "Selesai"
        self.desainer.tambah_pesanan_selesai()

    def tampilkan_struk(self):
        print("=== STRUK PESANAN ===")
        print(f"ID          : {self.id_pesanan}")
        print(f"Pelanggan   : {self.nama_pelanggan}")
        print(f"Layanan     : {self.layanan.nama_layanan}")
        print(f"Desainer    : {self.desainer.nama}")
        print(f"Status      : {self.__status}")
        print(f"Total Bayar : Rp{self.__total_bayar:,.0f}")

    @classmethod
    def dari_data(cls, data, layanan, desainer):
        """Factory method: buat objek dari dictionary + objek terkait."""
        return cls(data["id_pesanan"], data["nama_pelanggan"], layanan,
                    desainer, data.get("is_member", False))

    @classmethod
    def reset_total_pesanan(cls):
        cls.total_pesanan = 0
        print("[OK] total_pesanan direset ke 0.")

    @staticmethod
    def validasi_id_pesanan(id_pesanan):
        return isinstance(id_pesanan, str) and id_pesanan.startswith("ORD")


# ============================ MAIN PROGRAM ============================
if __name__ == "__main__":
    print("=== DEMO SISTEM MANAJEMEN PESANAN - DESAIGNKAN_ID ===")

    print("\n--- JenisLayanan ---")
    layanan_logo = JenisLayanan("Desain Logo", "Logo", 250000, 3)
    layanan_banner = JenisLayanan.dari_dict({
        "nama_layanan": "Desain Banner Promosi", "kategori": "Banner",
        "harga_dasar": 150000, "estimasi_hari": 2
    })
    layanan_logo.tampilkan_info()
    layanan_banner.tampilkan_info()
    print("Total layanan terdaftar:", JenisLayanan.total_layanan_terdaftar)
    print("Validasi kategori 'Logo':", JenisLayanan.validasi_kategori("Logo"))
    print("Validasi kategori 'Fotografi':", JenisLayanan.validasi_kategori("Fotografi"))
    JenisLayanan.ubah_diskon_member(0.15)

    print("\n--- Desainer ---")
    desainer_dea = Desainer("Dea Rahman", "Logo & Branding")
    desainer_bima = Desainer.dari_dict({
        "nama": "Bima Saputra", "spesialisasi": "Ilustrasi & Banner", "rating_awal": 4.7
    })
    desainer_dea.tampilkan_profil()
    desainer_bima.tampilkan_profil()
    print("Total desainer terdaftar:", Desainer.total_desainer)
    print("Validasi nama 'Bima Saputra':", Desainer.validasi_nama("Bima Saputra"))
    print("Validasi nama '   ':", Desainer.validasi_nama("   "))
    Desainer.ubah_level_default("Reguler")

    print("\n--- Pesanan ---")
    pesanan_1 = Pesanan("ORD001", "Yusuf", layanan_logo, desainer_dea, is_member=True)
    pesanan_2 = Pesanan.dari_data(
        {"id_pesanan": "ORD002", "nama_pelanggan": "Nadia", "is_member": False},
        layanan_banner, desainer_bima
    )
    for p in (pesanan_1, pesanan_2):
        p.proses_pesanan()
        p.selesaikan_pesanan()
        p.tampilkan_struk()
    print("Total pesanan tercatat:", Pesanan.total_pesanan)
    print("Validasi ID 'ORD001':", Pesanan.validasi_id_pesanan("ORD001"))
    print("Validasi ID 'X001':", Pesanan.validasi_id_pesanan("X001"))

    print("\n--- Pengujian Getter & Setter ---")
    print("Harga awal logo:", layanan_logo.harga_dasar)
    layanan_logo.harga_dasar = 300000   # valid
    layanan_logo.harga_dasar = -50000   # tidak valid
    print("Harga akhir logo:", layanan_logo.harga_dasar)

    print("Rating awal Bima:", desainer_bima.rating)
    desainer_bima.rating = 4.9   # valid
    desainer_bima.rating = 7.5   # tidak valid
    print("Rating akhir Bima:", desainer_bima.rating)

    print("Status awal pesanan 2:", pesanan_2.status)
    pesanan_2.status = "Dibatalkan"  # valid
    pesanan_2.status = "Kadaluarsa"  # tidak valid
    print("Status akhir pesanan 2:", pesanan_2.status)

    print("\n--- Reset Statistik ---")
    Pesanan.reset_total_pesanan()
    print("Total pesanan setelah reset:", Pesanan.total_pesanan)