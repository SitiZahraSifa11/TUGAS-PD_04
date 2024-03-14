sisi_a=int(input("Masukkan bilangan: "))
sisi_b=int(input("Masukkan bilangan: "))
sisi_c=int(input("Masukkan bilangan: "))

if sisi_a == sisi_b and sisi_b == sisi_c:
    print("Segitiga sama sisi")
elif sisi_a == sisi_b or sisi_a== sisi_c or sisi_b == sisi_c:
    print("Segitiga sama kaki")
else:
    print("Segitiga sembarang")