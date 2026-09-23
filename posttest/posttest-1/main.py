
class JenisLayanan:
    """Merepresentasikan satu jenis layanan desain grafis yang dijual."""

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
        """Getter untuk harga dasar layanan (private)."""
        return self.__harga_dasar

    @harga_dasar.setter
    def harga_dasar(self, nilai_baru):
        """Setter dengan validasi: harga harus angka positif."""
        if not isinstance(nilai_baru, (int, float)) or nilai_baru <= 0:
            print(f"[GAGAL] Harga layanan '{self.nama_layanan}' tidak valid. "
                f"Harga harus berupa angka > 0.")
            return
        self.__harga_dasar = nilai_baru
        print(f"[OK] Harga layanan '{self.nama_layanan}' diperbarui menjadi "
            f"Rp{nilai_baru:,.0f}")

    def tampilkan_info(self):
        print(f"Layanan: {self.nama_layanan} ({self.kategori}) - "
            f"Rp{self.__harga_dasar:,.0f} - estimasi {self.estimasi_hari} hari")

    def hitung_harga_setelah_diskon(self, is_member=False):
        """Instance method: menghitung harga akhir, berdiskon jika member."""
        if is_member:
            return self.__harga_dasar * (1 - JenisLayanan.diskon_member_default)
        return self.__harga_dasar

    @classmethod
    def dari_dict(cls, data):
        """Factory method: membuat objek JenisLayanan dari dictionary."""
        return cls(data["nama_layanan"], data["kategori"],
                    data["harga_dasar"], data["estimasi_hari"])

    @classmethod
    def ubah_diskon_member(cls, diskon_baru):
        """Mengubah atribut kelas diskon_member_default untuk semua objek."""
        if 0 <= diskon_baru < 1:
            cls.diskon_member_default = diskon_baru
            print(f"[OK] Diskon member platform diubah menjadi {diskon_baru*100:.0f}%")
        else:
            print("[GAGAL] Diskon harus berupa desimal antara 0 dan 1 (misal 0.1 = 10%)")

    @staticmethod
    def validasi_kategori(kategori):
        """Static method: mengecek apakah kategori layanan terdaftar."""
        return kategori in JenisLayanan.kategori_valid


class Desainer:
    """Merepresentasikan seorang desainer grafis di Desaignkan_id."""

    nama_instansi = "Desaignkan_id"
    total_desainer = 0
    level_default = "Junior"

    def __init__(self, nama, spesialisasi, rating_awal=5.0):
        self.nama = nama                             
        self.spesialisasi = spesialisasi             
        self.level = Desainer.level_default          
        self.__rating = rating_awal                  
        self.__jumlah_pesanan_selesai = 0            
        Desainer.total_desainer += 1

    @property
    def rating(self):
        """Getter untuk rating desainer (private)."""
        return self.__rating

    @rating.setter
    def rating(self, nilai_baru):
        """Setter dengan validasi: rating harus di antara 0 sampai 5."""
        if not isinstance(nilai_baru, (int, float)) or not (0 <= nilai_baru <= 5):
            print(f"[GAGAL] Rating untuk {self.nama} harus berupa angka 0-5.")
            return
        self.__rating = nilai_baru
        print(f"[OK] Rating {self.nama} diperbarui menjadi {nilai_baru}")

    def tambah_pesanan_selesai(self):
        """Menambah hitungan pesanan yang berhasil diselesaikan desainer."""
        self.__jumlah_pesanan_selesai += 1

    def tampilkan_profil(self):
        print(f"Desainer: {self.nama} | Spesialisasi: {self.spesialisasi} | "
            f"Level: {self.level} | Rating: {self.__rating} | "
            f"Pesanan Selesai: {self.__jumlah_pesanan_selesai}")

    @classmethod
    def dari_dict(cls, data):
        """Factory method: membuat objek Desainer dari dictionary."""
        return cls(data["nama"], data["spesialisasi"], data.get("rating_awal", 5.0))

    @classmethod
    def ubah_level_default(cls, level_baru):
        """Mengubah level default yang diberikan pada desainer baru."""
        cls.level_default = level_baru
        print(f"[OK] Level default desainer baru sekarang: '{level_baru}'")

    @staticmethod
    def validasi_nama(nama):
        """Static method: mengecek nama tidak kosong."""
        return isinstance(nama, str) and len(nama.strip()) > 0


class Pesanan:
    """Merepresentasikan satu transaksi pesanan desain dari pelanggan."""


    nama_instansi = "Desaignkan_id"
    total_pesanan = 0
    ongkos_admin = 5000
    status_valid = ["Menunggu", "Diproses", "Selesai", "Dibatalkan"]

    def __init__(self, id_pesanan, nama_pelanggan, layanan: JenisLayanan,
                desainer: Desainer, is_member=False):
        self.id_pesanan = id_pesanan          
        self.nama_pelanggan = nama_pelanggan  
        self.layanan = layanan                
        self.desainer = desainer              
        self.is_member = is_member            
        self.__status = "Menunggu"            
        self.__total_bayar = 0                

        Pesanan.total_pesanan += 1

    @property
    def status(self):
        """Getter untuk status pesanan (private)."""
        return self.__status

    @status.setter
    def status(self, status_baru):
        """Setter dengan validasi: status harus sesuai daftar status_valid."""
        if status_baru not in Pesanan.status_valid:
            print(f"[GAGAL] Status '{status_baru}' tidak valid. "
                f"Pilihan: {Pesanan.status_valid}")
            return
        self.__status = status_baru
        print(f"[OK] Status pesanan {self.id_pesanan} menjadi '{status_baru}'")

    @property
    def total_bayar(self):
        """Getter saja (read-only) untuk total bayar yang sudah dihitung sistem."""
        return self.__total_bayar

    def proses_pesanan(self):
        """Menghitung total bayar berdasarkan layanan & status member, lalu memproses."""
        harga = self.layanan.hitung_harga_setelah_diskon(self.is_member)
        self.__total_bayar = harga + Pesanan.ongkos_admin
        self.status = "Diproses"
        print(f"Pesanan {self.id_pesanan} diproses. "
            f"Total bayar: Rp{self.__total_bayar:,.0f}")

    def selesaikan_pesanan(self):
        """Menyelesaikan pesanan dan menambah statistik desainer terkait."""
        if self.__status != "Diproses":
            print(f"[GAGAL] Pesanan {self.id_pesanan} belum diproses, "
                f"tidak bisa langsung diselesaikan.")
            return
        self.status = "Selesai"
        self.desainer.tambah_pesanan_selesai()

    def tampilkan_struk(self):
        print("=== STRUK PESANAN ===")
        print(f"ID           : {self.id_pesanan}")
        print(f"Pelanggan    : {self.nama_pelanggan}")
        print(f"Layanan      : {self.layanan.nama_layanan}")
        print(f"Desainer     : {self.desainer.nama}")
        print(f"Status       : {self.__status}")
        print(f"Total Bayar  : Rp{self.__total_bayar:,.0f}")
        print("======================")

    @classmethod
    def dari_data(cls, data, layanan, desainer):
        """Factory method: membuat objek Pesanan dari dictionary + objek terkait."""
        return cls(data["id_pesanan"], data["nama_pelanggan"], layanan,
                    desainer, data.get("is_member", False))

    @classmethod
    def reset_total_pesanan(cls):
        """Mereset penghitung total_pesanan (atribut kelas) ke 0."""
        cls.total_pesanan = 0
        print("[OK] Statistik total_pesanan telah direset ke 0.")

    @staticmethod
    def validasi_id_pesanan(id_pesanan):
        """Static method: mengecek format ID pesanan harus diawali 'ORD'."""
        return isinstance(id_pesanan, str) and id_pesanan.startswith("ORD")


if __name__ == "__main__":

    print("#" * 60)
    print("  DEMO SISTEM MANAJEMEN PESANAN - DESAIGNKAN_ID")
    print("#" * 60)


    print("\n--- 1. Membuat objek JenisLayanan ---")
    layanan_logo = JenisLayanan("Desain Logo", "Logo", 250000, 3)
    layanan_banner = JenisLayanan.dari_dict({         
        "nama_layanan": "Desain Banner Promosi",
        "kategori": "Banner",
        "harga_dasar": 150000,
        "estimasi_hari": 2
    })

    layanan_logo.tampilkan_info()       
    layanan_banner.tampilkan_info()     

    print(f"Total layanan terdaftar (atribut kelas): "
        f"{JenisLayanan.total_layanan_terdaftar}")

    print("Validasi kategori 'Logo':", JenisLayanan.validasi_kategori("Logo"))
    print("Validasi kategori 'Fotografi':", JenisLayanan.validasi_kategori("Fotografi"))

    JenisLayanan.ubah_diskon_member(0.15)

    print("\n--- 2. Membuat objek Desainer ---")
    desainer_dea = Desainer("Dea Rahman", "Logo & Branding")
    desainer_bima = Desainer.dari_dict({             
        "nama": "Bima Saputra",
        "spesialisasi": "Ilustrasi & Banner",
        "rating_awal": 4.7
    })

    desainer_dea.tampilkan_profil()    
    desainer_bima.tampilkan_profil()   

    print(f"Total desainer terdaftar (atribut kelas): {Desainer.total_desainer}")

    print("Validasi nama 'Bima Saputra':", Desainer.validasi_nama("Bima Saputra"))
    print("Validasi nama '   ':", Desainer.validasi_nama("   "))

    Desainer.ubah_level_default("Reguler")


    print("\n--- 3. Membuat objek Pesanan ---")
    pesanan_1 = Pesanan("ORD001", "Yusuf", layanan_logo, desainer_dea, is_member=True)
    pesanan_2 = Pesanan.dari_data(                    
        {"id_pesanan": "ORD002", "nama_pelanggan": "Nadia", "is_member": False},
        layanan_banner,
        desainer_bima
    )

    pesanan_1.proses_pesanan()          
    pesanan_1.selesaikan_pesanan()      
    pesanan_1.tampilkan_struk()         

    pesanan_2.proses_pesanan()
    pesanan_2.selesaikan_pesanan()
    pesanan_2.tampilkan_struk()

    print(f"Total pesanan tercatat (atribut kelas): {Pesanan.total_pesanan}")

    
    print("Validasi ID 'ORD001':", Pesanan.validasi_id_pesanan("ORD001"))
    print("Validasi ID 'X001':", Pesanan.validasi_id_pesanan("X001"))

    print("\n--- 4. Pengujian Getter & Setter ---")

    print("\n[Harga layanan - JenisLayanan]")
    print("Harga awal logo:", layanan_logo.harga_dasar)   
    layanan_logo.harga_dasar = 300000                     
    layanan_logo.harga_dasar = -50000                     
    print("Harga akhir logo:", layanan_logo.harga_dasar)

    print("\n[Rating - Desainer]")
    print("Rating awal Bima:", desainer_bima.rating)      
    desainer_bima.rating = 4.9                            
    desainer_bima.rating = 7.5                            
    print("Rating akhir Bima:", desainer_bima.rating)

    print("\n[Status - Pesanan]")
    print("Status awal pesanan 2:", pesanan_2.status)     
    pesanan_2.status = "Dibatalkan"                       
    pesanan_2.status = "Kadaluarsa"                       
    print("Status akhir pesanan 2:", pesanan_2.status)

    print("\n--- 5. Reset statistik total_pesanan ---")
    Pesanan.reset_total_pesanan()
    print("Total pesanan setelah reset:", Pesanan.total_pesanan)