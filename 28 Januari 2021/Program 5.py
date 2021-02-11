def konversi(x):
    if x == 1 or x == 0:
        return x

    panjang = len(str(x))
    AngkaPertama = x//pow(10, panjang-1)

    return (pow(2, panjang-1) * AngkaPertama) + konversi(x % pow(10, panjang-1))

while True:
    Biner = int(input('Masukkan Biner : '))
    Desimal = konversi(Biner)

    print("Desimal dari", Biner, 'adalah', Desimal)