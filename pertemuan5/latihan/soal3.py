sesi_pagi = {"Andi", "Budi", "Cici"} 
sesi_siang = {"Budi", "Deni", "Eka"}
# a.Tampilkan nama mahasiswa yang hadir di kedua sesi (pagi DAN siang) 
hadir_keduasesi = sesi_pagi.intersection(sesi_siang)
print(hadir_keduasesi)
# b. Tampilkan total daftar nama unik yang hadir hari itu (semua mahasiswa dari kedua  sesi tanpa duplikat). 
nama_unik = sesi_pagi.symmetric_difference(sesi_siang)
print(nama_unik) 
# c. Gabungkan kedua set tersebut menjadi satu set bernama sesi_hari_ini.  
sesi_hari_ini = sesi_pagi.union(sesi_siang)
print(sesi_hari_ini)

