class Bank:
    def __init__(self, nama_bank, kode):
        self.nama_bank = nama_bank
        self.kode = kode
        self.karyawan = []

    def tambah_karyawan(self, nama, nip, posisi):
        karyawan_baru = Karyawan(nama, nip, posisi)
        self.karyawan.append(Karyawan)

class Karyawan:
    def __init__(self, nama, nip, posisi):
        self.nama = nama
        self.nip = nip
        self.posisi = posisi

bank = Bank("BCA", "12345")
bank.tambah_karyawan("Dapa", "001", "Manager")

del bank
