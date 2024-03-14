# Tuliskan program untuk menentukan bilangan itu bilangan (ganjil/genap) positif, negatif atau 0

nilai = int(input("Masukkan bilangan: "))

if nilai % 2 == 0 and nilai > 0:
    print(nilai, "adalah bilangan genap positif")
elif nilai % 2 == 0 and nilai < 0:
    print(nilai, "adalah bilangan genap negatif")
elif nilai % 2 != 0 and nilai > 0:
    print(nilai, "adalah bilangan ganjil positif")
elif nilai % 2 != 0 and nilai < 0:
    print(nilai, "adalah bilangan ganjil negatif")
else:
    print(nilai, "adalah bilangan 0 / netral")