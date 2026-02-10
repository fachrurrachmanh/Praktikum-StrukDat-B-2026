angka = [10,20,30,40,50]
#1.Tambahkan angka 60 ke dalam list.
angka.append(60)
angka.remove(20)
max = 10
min = 60

#2.nilai tertinggi
for x in angka:
    if x > max:
        max = x
print(f"nilai tertinggi ialah {max}")

#3.nilai terendah
for x in angka:
    if x < min:
        min = x
print(f"nilai terendah ialah {min}")

#4.rata rata
total = 0
for x in angka:
    total += x
rata_rata=total/len(angka)
print(f"rata ratanya ialah {rata_rata}")

#5.menampilkan list yang udah dirubah
print(angka)