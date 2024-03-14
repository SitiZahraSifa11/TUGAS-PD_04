# Program yang mensimulasikan permainan batu-gunting-kertas antara dua pemain dan menentukan pemenangnya.

pemain1 = input("Pemain 1 : masukkan pilihan (batu/gunting/kertas): ").lower()
pemain2 = input("Pemain 2 : masukkan pilihan (batu/gunting/kertas): ").lower()

if pemain1 == pemain2:
            print("Pertandingan seri!")
elif (pemain1 == 'batu' and pemain2 == 'gunting') or
     (pemain1 == 'gunting' and pemain2 == 'kertas') or
     (pemain1 == 'kertas' and pemain2 == 'batu'):
            print("Pemain 1 yang menang!")
else:
            print("Pemain 2 yang menang!")
