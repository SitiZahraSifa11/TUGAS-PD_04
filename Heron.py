import math

# Buatlah program yang menghitung luas dan keliling segitiga berdasarkan panjang sisi-sisinya. (Gunakan Rumus Heron)

a = float(input("Masukkan panjang sisi a: "))
b = float(input("Masukkan panjang sisi b: "))
c = float(input("Masukkan panjang sisi c: "))

s= (a+b+c)/2
luas = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Luas segitiga menggunakan rumus heron adalah :", luas)

keliling=a+b+c
print("Keliling segitiga adalah :", keliling)








