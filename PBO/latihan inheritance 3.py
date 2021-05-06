# INHERITANCE / PEWARISAN
# super class / parent class
class Manusia:
    # konstruktor
    def __init__(self, nama, jk, usia):
        self.nama = nama
        self.jk = jk
        self.usia = usia

    def info(self):
        print("Nama : {}\nJenis Kelamin : {}\nUsia : {}".format(self.nama, self.jk, self.usia))
        print("-" * 25)
    
    def makan(self):
        print("Sedang makan nasi")
        print("-" * 25)

# sub class / child class
class Pelajar(Manusia):
    # konstruktor anak
    def __init__(self, nama, jk, usia, nis, nilai):
        Manusia.__init__(self, nama, jk, usia)
        self.nis = nis
        self.nilai = nilai

    def belajar(self):
        print("{} Sedang belajar".format(self.nama))
        print("-" * 25)
        
    # methode overriding
    def makan(self):
        print("{}  sedang sarapan pagi dengan nasi". format(self.nama))
        print("-" * 25)

# sub class / child class
class Pekerja(Manusia):
    # konstruktor anak
    def __init__(self, nama, jk, usia, nip, gaji):
        Manusia.__init__(self, nama, jk, usia)
        self.nip = nip
        self.gaji = gaji

    def bekerja(self):
        print("{} sedang bekerja".format(self.nama))
        print("-" * 25)

# instansiasi objek
Rudi = Pelajar("Rudianto", "Laki-laki", 16, "15234", 90)
Wawan = Pekerja("Iwan", "Laki-laki", 29, "1987463", 50000000)

# pemanggilan
Rudi.info()
Rudi.belajar()
Rudi.makan() # memanggil methode anak
Wawan.info()
Wawan.bekerja()
Wawan.makan() # memanggil methode induk
