class Kelinci:

    jumlah_kelinci = 0

    def __init__(self,warna,berat,umur):
        self.warna = warna
        self.berat = berat
        self.umur = umur
        Kelinci.jumlah_kelinci += 1

    def tampilkan_jumlah(self):
        print("Total Kelinci :", Kelinci.jumlah_kelinci)

    def tampilkan_profil(self):
        print("Warna :", self.warna)
        print("Berat :", self.berat)
        print("Umur :", self.umur)

kelinci1 = Kelinci("Hitam", 1.2, 4)
kelinci2 = Kelinci("Putih", 1.5, 3)

kelinci1.tampilkan_profil()
kelinci2.tampilkan_profil()
kelinci1.tampilkan_jumlah()