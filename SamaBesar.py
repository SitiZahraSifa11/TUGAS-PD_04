# Tuliskan program yang meminta input 3 buah bilangan dan tentukan bilangan mana yang lebih besar, 
# 2 bilangan lebih besar dari yang lain atau semua bilangan sama besar

angka1 = int(input("Masukan nilai 1 :"))
angka2 = int(input("Masukan nilai 2 :"))
angka3 = int(input("Masukan nilai 3 :"))

if angka1 > angka2 and angka3 > angka2:
    print(angka1," adalah yang terbesar juga ada 2 dan ",  "Lebih besar dari ",angka2)
elif angka2 > angka1 and angka3 > angka1:
    print(angka2, " adalah yang terbesar juga ada 2 dan ", "lebih besar dari ", angka1)
elif angka2 > angka3 and angka1 > angka3:
    print(angka1 , " adalah yang terbesar juga ada 2 dan " , "lebih besar dari ", angka3)

elif angka1 == angka2 and angka1 > angka3:
    print(angka2,"adalah yang terbesar juga ada 2 dan ", "lebih besar dari ", angka3)
elif angka1 == angka3 and angka1 > angka2:
    print(angka1, " adalah yang terbesar juga ada 2 dan", "lebih besar dari ", angka2)
elif angka2 == angka3 and angka2 > angka1:
    print(angka2, " adalah yang terbesar juga ada 2 dan ", "lebih besar dari ", angka1)
    

else:
    print("Semua bilangan sama besar")