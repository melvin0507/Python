def print_faktor(x):
    print("Faktor dari ", x , " adalah : ")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num = int(input("Masukkan bilangan: "))
print_faktor(num)
#Melvin Waluyo XI MIPA 5/20 