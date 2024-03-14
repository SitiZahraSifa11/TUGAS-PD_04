# Tuliskan program untuk menentukan bilangan itu bilangan positif, negatif atau 0

nilai = int(input("Masukkan bilangan: "))

if nilai > 0:
    print(nilai, "adalah bilangan positif")
elif nilai < 0:
    print(nilai, "adalah bilangan negatif")
else:
    print(nilai, "adalah bilangan 0 / netral")