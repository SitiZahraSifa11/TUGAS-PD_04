# Tulisan program yang meminta input 3 buah bilangan dan tentukan bilangan mana yang lebih kecil


angka_a =int(input("Masukkan angka pertama :"))
angka_b = int(input("Masukkan angka kedua :"))
angka_c = int(input("Masukkan angka ketiga :"))

if angka_a < angka_b and angka_b<angka_c:
    print("Bilangan pertama lebih kecil:", angka_a)
elif angka_b<angka_c and angka_c<angka_b :
    print ("Bilangan kedua lebih kecil :",angka_b)
else :
    print("Bilangan ketiga lebih kecil:", angka_c)


