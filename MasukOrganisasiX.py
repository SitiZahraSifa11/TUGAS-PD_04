# Buatlah program untuk menghitung kelayakan orang lulus organisasi X. Organisasi X memiliki kriteria untuk Anggota
# 1. Perempuan dengan berat badan minimal 45kilo gram, maks 50 kilogram dan Tingginya minimal 165 cm dan Usianya kurang dari 20 tahun
# 2. Laki-laki dengan berat badan maks 70 kilo dan Tingginya minimal 170 cm dan usianya maks 25 tahun
# 3. Laki-laki dan Perempuan dengan nilai rata-rata Akademis 90 dan usianya kurang dari 30 tahun
# 4. Laki-laki dan Perempuan yang Memiliki Skill Menembak, Memanah atau Berkuda

# Ke 4 Kriteria diatas akan diterima hanya dan hanya jika tidak memiliki anggota tubuh yang cacat.

# Buatlah Program Questioner untuk mengakomodasi kasus diatas.


print("                            SELAMAT DATANG DI ORGANISASI X                              ")
print("========================================================================================")
print("Silakan jawab pertanyaan berikut untuk mengetahui apakah Anda layak menjadi anggota")

jenis_kelamin = input("Jenis kelamin (laki-laki/perempuan): ").lower()
berat_badan = float(input("Berat badan (kg): "))
tinggi_badan = float(input("Tinggi badan (cm): "))
usia = int(input("Usia: "))
nilai_akademis = float(input("Nilai akademis (jika ada, jika tidak ada masukkan angka 0): "))
memiliki_skill = input("Apakah Anda memiliki skill menembak, memanah, atau berkuda? (ya/tidak): ").lower()
memiliki_cacat = input("Apakah Anda memiliki cacat anggota tubuh? (ya/tidak): ").lower()

  
if jenis_kelamin == 'perempuan':
        if 45 >= berat_badan <= 50 and tinggi_badan >= 165 and usia < 20 and memiliki_cacat == 'tidak'and nilai_akademis > 90 and memiliki_skill=='ya':
           print(" Keputusan : Anda layak menjadi anggota Organisasi X.")   
        else:
           print(" Keputusan : Maaf, Anda tidak layak menjadi anggota Organisasi X.")
elif jenis_kelamin == 'laki-laki':
        if berat_badan <= 70 and tinggi_badan >= 170 and usia <= 25 and memiliki_cacat == 'tidak' and nilai_akademis > 90 and memiliki_skill=='ya':
           print(" Keputusan : Anda layak menjadi anggota Organisasi X.")
        else:
           print(" Keputusan : Maaf, Anda tidak layak menjadi anggota Organisasi X.")
