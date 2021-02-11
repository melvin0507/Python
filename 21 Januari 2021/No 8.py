from statistics import mode 
def modus(listangka):
    modus = mode(listangka)
    print("Modusnya adalah:", modus) 

while True:
    a = input("Masukkan List Angka: ")
    listangka = a.split()
    modus(listangka)
    print("")

#Melvin Waluyo XI MIPA 5/20 