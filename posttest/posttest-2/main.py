class JenisLayanan:
    """Satu jenis layanan desain grafis yang dijual."""

    nama_platform = "Desaignkan_id"
    total_layanan_terdaftar = 0
    diskon_member_default = 0.1
    kategori_valid = ["Logo", "Banner", "Ilustrasi", "UI/UX", "Konten Sosmed"]

    def __init__(self, nama_layanan, kategori, harga_dasar, estimasi_hari):
        self.nama_layanan = nama_layanan
        self.kategori = kategori
        self.estimasi_hari = estimasi_hari
        self.__harga_dasar = harga_dasar
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
    """SUPERCLASS: seorang desainer grafis di Desaignkan_id.

    - Protected (_nama, _spesialisasi, _level): boleh dipakai langsung oleh subclass.
    - Private (__rating, __pesanan_selesai): rahasia superclass, hanya bisa
    diubah lewat property / method milik Desainer.
    """
    nama_instansi = "Desaignkan_id"
    total_desainer = 0
    level_default = "Junior"

    def __init__(self, nama, spesialisasi, rating_awal=5.0):
        self._nama = nama
        self._spesialisasi = spesialisasi
        self._level = Desainer.level_default
        self.__rating = rating_awal
        self.__pesanan_selesai = 0
        Desainer.total_desainer += 1

    @property
    def nama(self):
        return self._nama

    @property
    def spesialisasi(self):
        return self._spesialisasi

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or not (0 <= nilai_baru <= 5):
            print(f"[GAGAL] Rating {self._nama} harus angka 0-5.")
            return
        self.__rating = nilai_baru
        print(f"[OK] Rating {self._nama} diperbarui jadi {nilai_baru}")

    @property
    def pesanan_selesai(self):
        return self.__pesanan_selesai

    def tambah_pesanan_selesai(self):
        self.__pesanan_selesai += 1

    def hitung_biaya_tambahan(self, harga_layanan):
        """Biaya tambahan khusus desainer. Default: tidak ada (di-override subclass)."""
        return 0

    def tampilkan_profil(self):
        print(f"Desainer: {self._nama} | Spesialisasi: {self._spesialisasi} | "
              f"Level: {self._level} | Rating: {self.__rating} | "
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


class DesainerLogo(Desainer):
    """SUBCLASS 1: spesialis logo & branding.
    Atribut unik: jumlah_konsep (konsep logo yang dikerjakan per pesanan)."""
    KONSEP_GRATIS = 3
    BIAYA_PER_KONSEP = 25000

    def __init__(self, nama, rating_awal=5.0, jumlah_konsep=3):
        super().__init__(nama, "Logo & Branding", rating_awal)
        self.jumlah_konsep = jumlah_konsep

    def hitung_biaya_tambahan(self, harga_layanan):
        konsep_ekstra = max(0, self.jumlah_konsep - DesainerLogo.KONSEP_GRATIS)
        return konsep_ekstra * DesainerLogo.BIAYA_PER_KONSEP

    def tampilkan_profil(self):
        super().tampilkan_profil()
        print(f"   -> [Logo] Jumlah konsep per pesanan: {self.jumlah_konsep}")


class DesainerIlustrator(Desainer):
    """SUBCLASS 2: spesialis ilustrasi & banner.
    Atribut unik: gaya_ilustrasi."""
    PERSEN_KOMPLEKSITAS = 0.10

    def __init__(self, nama, gaya_ilustrasi, rating_awal=5.0):
        super().__init__(nama, "Ilustrasi & Banner", rating_awal)
        self.gaya_ilustrasi = gaya_ilustrasi

    def hitung_biaya_tambahan(self, harga_layanan):
        return harga_layanan * DesainerIlustrator.PERSEN_KOMPLEKSITAS

    def tampilkan_profil(self):
        super().tampilkan_profil()
        print(f"   -> [Ilustrator] Gaya ilustrasi: {self.gaya_ilustrasi}")

    @classmethod
    def dari_dict(cls, data):
        """Override factory: subclass ini butuh field 'gaya_ilustrasi'."""
        return cls(data["nama"], data["gaya_ilustrasi"], data.get("rating_awal", 5.0))


class DesainerUIUX(Desainer):
    """SUBCLASS 3: spesialis UI/UX.
    Atribut unik: tools (daftar software yang dikuasai)."""
    BIAYA_PROTOTYPE = 50000

    def __init__(self, nama, tools, rating_awal=5.0):
        super().__init__(nama, "UI/UX", rating_awal)
        self.tools = tools

    def hitung_biaya_tambahan(self, harga_layanan):
        return DesainerUIUX.BIAYA_PROTOTYPE

    def tampilkan_profil(self):
        super().tampilkan_profil()
        print(f"   -> [UI/UX] Tools: {', '.join(self.tools)}")

    def sapa_tim(self):
        """Contoh subclass mengakses atribut protected milik superclass."""
        print(f"Halo, saya {self._nama}, spesialis {self._spesialisasi} "
            f"(level {self._level}).")



class Pelanggan:
    """Pelanggan jasa desain. Berelasi ASOSIASI dengan Pesanan."""
    total_pelanggan = 0

    def __init__(self, nama, is_member=False):
        self.nama = nama
        self.is_member = is_member
        Pelanggan.total_pelanggan += 1

    def tampilkan_info(self):
        tipe = "Member" if self.is_member else "Non-member"
        print(f"Pelanggan: {self.nama} ({tipe})")


class TimDesain:
    """AGREGASI: TimDesain 'memiliki' banyak Desainer, tetapi Desainer
    dibuat di luar & tetap hidup meskipun tim dibubarkan."""

    def __init__(self, nama_tim):
        self.nama_tim = nama_tim
        self.__anggota = []

    @property
    def anggota(self):
        return list(self.__anggota)

    def tambah_anggota(self, desainer):
        if not isinstance(desainer, Desainer):
            print("[GAGAL] Anggota harus objek Desainer.")
            return
        if desainer in self.__anggota:
            print(f"[GAGAL] {desainer.nama} sudah ada di {self.nama_tim}.")
            return
        self.__anggota.append(desainer)
        print(f"[OK] {desainer.nama} bergabung ke {self.nama_tim}")

    def keluarkan_anggota(self, desainer):
        if desainer in self.__anggota:
            self.__anggota.remove(desainer)
            print(f"[OK] {desainer.nama} keluar dari {self.nama_tim}")

    def rata_rata_rating(self):
        if not self.__anggota:
            return 0
        return sum(d.rating for d in self.__anggota) / len(self.__anggota)

    def tampilkan_tim(self):
        print(f"=== {self.nama_tim} ({len(self.__anggota)} anggota, "
            f"rata-rata rating {self.rata_rata_rating():.2f}) ===")
        for d in self.__anggota:
            d.tampilkan_profil()

    def bubarkan(self):
        """Tim bubar -> daftar anggota dikosongkan, objek Desainer TETAP ADA."""
        self.__anggota.clear()
        print(f"[OK] {self.nama_tim} dibubarkan.")


class RincianBiaya:
    """KOMPOSISI (bagian dari Pesanan): dibuat di dalam Pesanan,
    tidak punya arti & tidak ada tanpa Pesanan."""

    def __init__(self):
        self.harga_layanan = 0
        self.potongan_member = 0
        self.biaya_desainer = 0
        self.ongkos_admin = 0

    @property
    def total(self):
        return (self.harga_layanan - self.potongan_member
                + self.biaya_desainer + self.ongkos_admin)

    def hitung(self, harga_layanan, potongan_member, biaya_desainer, ongkos_admin):
        self.harga_layanan = harga_layanan
        self.potongan_member = potongan_member
        self.biaya_desainer = biaya_desainer
        self.ongkos_admin = ongkos_admin

    def tampilkan(self):
        print(f"  Harga layanan   : Rp{self.harga_layanan:,.0f}")
        print(f"  Potongan member : -Rp{self.potongan_member:,.0f}")
        print(f"  Biaya desainer  : Rp{self.biaya_desainer:,.0f}")
        print(f"  Ongkos admin    : Rp{self.ongkos_admin:,.0f}")


class Revisi:
    """KOMPOSISI (bagian dari Pesanan): hanya dibuat lewat Pesanan.tambah_revisi()."""

    def __init__(self, nomor, catatan):
        self.nomor = nomor
        self.catatan = catatan


class Pesanan:
    """Satu transaksi pesanan desain.

    ASOSIASI : Pesanan -> Pelanggan, JenisLayanan, Desainer
            (objek dibuat di luar, hanya direferensikan)
    KOMPOSISI: Pesanan *-- RincianBiaya, Pesanan *-- Revisi
            (dibuat & dimiliki penuh oleh Pesanan)
    """
    nama_instansi = "Desaignkan_id"
    total_pesanan = 0
    ongkos_admin = 5000
    status_valid = ["Menunggu", "Diproses", "Selesai", "Dibatalkan"]

    def __init__(self, id_pesanan, pelanggan, layanan, desainer):
        self.id_pesanan = id_pesanan
        self.pelanggan = pelanggan
        self.layanan = layanan
        self.desainer = desainer
        self.__rincian = RincianBiaya()
        self.__daftar_revisi = []
        self.__status = "Menunggu"
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
        return self.__rincian.total

    @property
    def jumlah_revisi(self):
        return len(self.__daftar_revisi)

    def tambah_revisi(self, catatan):
        if self.__status in ("Selesai", "Dibatalkan"):
            print(f"[GAGAL] Pesanan {self.id_pesanan} sudah {self.__status}, revisi ditolak.")
            return
        revisi = Revisi(len(self.__daftar_revisi) + 1, catatan)
        self.__daftar_revisi.append(revisi)
        print(f"[OK] Revisi #{revisi.nomor} untuk {self.id_pesanan}: {catatan}")

    def proses_pesanan(self):
        harga_setelah = self.layanan.hitung_harga_setelah_diskon(self.pelanggan.is_member)
        potongan = self.layanan.harga_dasar - harga_setelah
        biaya_desainer = self.desainer.hitung_biaya_tambahan(harga_setelah)
        self.__rincian.hitung(self.layanan.harga_dasar, potongan,
                            biaya_desainer, Pesanan.ongkos_admin)
        self.status = "Diproses"
        print(f"Pesanan {self.id_pesanan} diproses. Total: Rp{self.total_bayar:,.0f}")

    def selesaikan_pesanan(self):
        if self.__status != "Diproses":
            print(f"[GAGAL] Pesanan {self.id_pesanan} belum diproses.")
            return
        self.status = "Selesai"
        self.desainer.tambah_pesanan_selesai()

    def tampilkan_struk(self):
        print("=== STRUK PESANAN ===")
        print(f"ID          : {self.id_pesanan}")
        print(f"Pelanggan   : {self.pelanggan.nama}")
        print(f"Layanan     : {self.layanan.nama_layanan}")
        print(f"Desainer    : {self.desainer.nama} ({type(self.desainer).__name__})")
        print(f"Status      : {self.__status}")
        print(f"Revisi      : {self.jumlah_revisi}x")
        self.__rincian.tampilkan()
        print(f"Total Bayar : Rp{self.total_bayar:,.0f}")

    @classmethod
    def dari_data(cls, data, pelanggan, layanan, desainer):
        """Factory method: buat objek dari dictionary + objek terkait."""
        return cls(data["id_pesanan"], pelanggan, layanan, desainer)

    @classmethod
    def reset_total_pesanan(cls):
        cls.total_pesanan = 0
        print("[OK] total_pesanan direset ke 0.")

    @staticmethod
    def validasi_id_pesanan(id_pesanan):
        return isinstance(id_pesanan, str) and id_pesanan.startswith("ORD")


if __name__ == "__main__":
    print("=== DEMO SISTEM MANAJEMEN PESANAN - DESAIGNKAN_ID ===")

    print("\n--- JenisLayanan ---")
    layanan_logo = JenisLayanan("Desain Logo", "Logo", 250000, 3)
    layanan_banner = JenisLayanan.dari_dict({
        "nama_layanan": "Desain Banner Promosi", "kategori": "Banner",
        "harga_dasar": 150000, "estimasi_hari": 2
    })
    layanan_uiux = JenisLayanan("Desain UI/UX Aplikasi", "UI/UX", 500000, 7)
    for l in (layanan_logo, layanan_banner, layanan_uiux):
        l.tampilkan_info()
    print("Total layanan terdaftar:", JenisLayanan.total_layanan_terdaftar)
    print("Validasi kategori 'Logo':", JenisLayanan.validasi_kategori("Logo"))
    print("Validasi kategori 'Fotografi':", JenisLayanan.validasi_kategori("Fotografi"))
    JenisLayanan.ubah_diskon_member(0.15)

    print("\n--- INHERITANCE: Superclass Desainer & 3 Subclass ---")
    desainer_dea = DesainerLogo("Dea Rahman", jumlah_konsep=5)
    desainer_bima = DesainerIlustrator.dari_dict({
        "nama": "Bima Saputra", "gaya_ilustrasi": "Flat Vector", "rating_awal": 4.7
    })
    desainer_citra = DesainerUIUX("Citra Lestari", ["Figma", "Adobe XD"], 4.8)
    semua_desainer = [desainer_dea, desainer_bima, desainer_citra]

    print("Total desainer terdaftar:", Desainer.total_desainer)
    print("Validasi nama 'Bima Saputra':", Desainer.validasi_nama("Bima Saputra"))
    print("Validasi nama '   ':", Desainer.validasi_nama("   "))
    Desainer.ubah_level_default("Reguler")

    print("\n[Method Overriding: tampilkan_profil() di tiap subclass]")
    for d in semua_desainer:
        d.tampilkan_profil()

    print("\n[Method Overriding + Polymorphism: hitung_biaya_tambahan(harga=200000)]")
    for d in semua_desainer:
        print(f"{type(d).__name__:<18}: Rp{d.hitung_biaya_tambahan(200000):,.0f}")

    print("\n[Atribut Protected: diakses langsung dari dalam subclass]")
    desainer_citra.sapa_tim()
    print("Protected dari luar (boleh secara konvensi, tidak disarankan):", desainer_dea._nama)

    print("\n[Atribut Private: tidak bisa diakses langsung]")
    try:
        print(desainer_dea.__rating)
    except AttributeError:
        print("[GAGAL] __rating bersifat private, harus lewat property .rating =",
            desainer_dea.rating)

    print("\n[isinstance & issubclass]")
    print("DesainerLogo subclass dari Desainer?", issubclass(DesainerLogo, Desainer))
    print("desainer_bima instance dari Desainer?", isinstance(desainer_bima, Desainer))

    print("\n--- AGREGASI: TimDesain o-- Desainer ---")
    tim = TimDesain("Tim Kreatif Alpha")
    for d in semua_desainer:
        tim.tambah_anggota(d)
    tim.tambah_anggota(desainer_dea)
    tim.tambah_anggota("bukan desainer")
    tim.tampilkan_tim()
    tim.keluarkan_anggota(desainer_bima)
    tim.bubarkan()
    print("Anggota tim setelah bubar:", len(tim.anggota))
    print("Desainer tetap ada setelah tim bubar:")
    desainer_dea.tampilkan_profil()

    print("\n--- ASOSIASI: Pesanan -> Pelanggan, JenisLayanan, Desainer ---")
    yusuf = Pelanggan("Yusuf", is_member=True)
    nadia = Pelanggan("Nadia")
    raka = Pelanggan("Raka", is_member=True)
    yusuf.tampilkan_info()
    nadia.tampilkan_info()

    pesanan_1 = Pesanan("ORD001", yusuf, layanan_logo, desainer_dea)
    pesanan_2 = Pesanan.dari_data({"id_pesanan": "ORD002"}, nadia,
                                layanan_banner, desainer_bima)
    pesanan_3 = Pesanan("ORD003", raka, layanan_uiux, desainer_citra)

    print("\n--- KOMPOSISI: Pesanan *-- RincianBiaya & Revisi ---")
    pesanan_1.tambah_revisi("Warna logo dibuat lebih gelap")
    pesanan_1.tambah_revisi("Ganti font nama brand")
    for p in (pesanan_1, pesanan_2, pesanan_3):
        p.proses_pesanan()
        p.selesaikan_pesanan()
        p.tampilkan_struk()
        print()
    pesanan_1.tambah_revisi("Revisi setelah selesai")
    print("Total pesanan tercatat:", Pesanan.total_pesanan)
    print("Total pelanggan terdaftar:", Pelanggan.total_pelanggan)
    print("Validasi ID 'ORD001':", Pesanan.validasi_id_pesanan("ORD001"))
    print("Validasi ID 'X001':", Pesanan.validasi_id_pesanan("X001"))

    del pesanan_3
    print("\nSetelah pesanan_3 dihapus, pelanggan & desainer tetap ada:")
    raka.tampilkan_info()
    desainer_citra.tampilkan_profil()

    print("\n--- Pengujian Getter & Setter ---")
    print("Harga awal logo:", layanan_logo.harga_dasar)
    layanan_logo.harga_dasar = 300000
    layanan_logo.harga_dasar = -50000
    print("Harga akhir logo:", layanan_logo.harga_dasar)

    print("Rating awal Bima:", desainer_bima.rating)
    desainer_bima.rating = 4.9
    desainer_bima.rating = 7.5
    print("Rating akhir Bima:", desainer_bima.rating)

    print("Status awal pesanan 2:", pesanan_2.status)
    pesanan_2.status = "Dibatalkan"
    pesanan_2.status = "Kadaluarsa"
    print("Status akhir pesanan 2:", pesanan_2.status)

    print("\n--- Reset Statistik ---")
    Pesanan.reset_total_pesanan()
    print("Total pesanan setelah reset:", Pesanan.total_pesanan)