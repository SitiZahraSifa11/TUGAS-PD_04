# Program untuk mengonversi suhu dari Celsius ke Fahrenheit atau sebaliknya, sesuai dengan input pengguna.

pilihan = input ("Apa yang ingin di Konversi ? celcius / fahrenheit :")
derajat = int(input("Bilangan suhu yang di konversi: "))
suhu = str(input("Ke jenis suhu : "))

if pilihan == "celcius":
    hasil= derajat *1.8+32
else:
    hasil = ((derajat-32)*5)/9


print(derajat, pilihan, " di konversikan menjadi ",hasil, suhu)

