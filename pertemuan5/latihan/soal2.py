kumpulan_nilai = [("Andi", 85), ("Budi", 60), ("Cici", 90), ("Deni", 72)]
# Gunakan perulangan untuk memproses setiap tuple tersebut. 
# Jika nilai >= 75,tampilkan: "Selamat [Nama], Anda Lulus!". 
# Jika di bawah 75, tampilkan: "Maaf [Nama], Anda harus remidi." 
for nama, nilai in kumpulan_nilai:
    if nilai >= 75:
        print(f"selamat {nama}, Anda lulus")
    if nilai < 75:
        print(f"Maaf {nama}, Anda harus remidi")
