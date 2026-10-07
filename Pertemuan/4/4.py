class Animal:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def makan(self):
        print(f"{self.nama} sedang makan.")

class Mamalia(Animal):
    def __init__(self, nama, umur, warna_bulu):
        super().__init__(nama, umur)
        self.warna_bulu = warna_bulu

class Reptil(Animal):
    def __init__(self, nama, umur, jenis_kulit):
        super().__init__(nama, umur)
        self.jenis_kulit = jenis_kulit

