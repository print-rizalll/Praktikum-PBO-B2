# # # # class Hero:
# # # #     def __init__(self, nama, health):
# # # #         self.nama = nama
# # # #         self.health = health

# # # #     def serang(self, hero_target):
# # # #         hero_target.health -= 10

# # # # class TampilanHero:
# # # #     def tampilan (self, hero):
# # # #         print(f"{hero.name} | HP {hero.health}")

# # # # class PenyimpanHero:
# # # #     def simpan(self, hero, nama_file):
# # # #         with open(nama_file, "a") as f:
# # # #             f.write(f"{hero.name}, {hero.health}\n")

# # # # layla = Hero("Layla", 70)
# # # # Hero("Balmond", 120).serang(layla)
# # # # TampilanHero().tampilan(layla)
# # # # PenyimpanHero().simpan(layla, "data_hero.txt")


# # # class Unit():
# # #     pass

# # # class UnitBergerak(Unit):  
# # #     def bergerak(self):
# # #         pass

# # # class Minion(UnitBergerak):
# # #     def bergerak(self):
# # #         print("Minian sedang bergerak")

# # # class Turet(Unit):
# # #     pass

# # # class Lord(UnitBergerak):
# # #     print("Lord sedang bergerak")

# # # def maju(unit):
# # #     unit.bergerak()

# # # maju(Minion())

# # from abc import ABC, abstractmethod

# # class BisaMenyerang(ABC):

# #     @abstractmethod
# #     def serang(self):
# #         pass

# # class BisaHeal(ABC):
# #     @abstractmethod
# #     def heal(self):
# #         pass

# # class Fighter(BisaMenyerang):
# #     def serang(self):
# #         print("Fighter menyerang")

# # class Support(BisaMenyerang, BisaHeal):
# #     def serang(self):
# #         print("Support menyerang")

# # def heal(self):
# #     print("Support memulihkan rekan")

# # Fighter().serang()
# # Support().heal()
# # print(isinstance(Fighter(), BisaHeal))

# from abc import ABC, abstractmethod

# class PapanSkor(ABC): # abstraksi

#     @abstractmethod
#     def catat(self, pesan):
#         pass

# class PapanSkorKonsol(PapanSkor):
#     def catat(self, pesan):
#         print(f"[KONSOL] {pesan}")

# class PapanSkorFile(PapanSkor):
#     def catat(self, pesan):
#         with open("riwayat.txt", "a") as f:
#             f.write(pesan + "\n")
#             print("[FILE] tersimpan di riwayat.txt")

# class Arena:
#     def __init__(self, papan_skor: PapanSkor): # disuntikkan dari luar
#         self.papan_skor = papan_skor

#     def adu(self, a, b):
#         self.papan_skor.catat(f"{a} vs {b}")

# Arena(PapanSkorKonsol()).adu("Balmond", "Layla")
# Arena(PapanSkorFile()).adu("Layla", "Balmond")

from abc import ABC, abstractmethod
from os import name

class Senjata(ABC):
    @abstractmethod
    def pukul(self):
        pass

class Pedang(Senjata):
    def pukul(self):
        return 20

class Panah(Senjata):
    def pukul(self):
        return 10

class hero:
    def serang(self):
