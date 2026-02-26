transaksi = [  
{"produk": "Buku", "harga": 10000, "jumlah": 3},  
{"produk": "Pena", "harga": 5000, "jumlah": 10},  
{"produk": "Penghapus", "harga": 2000, "jumlah": 2}  
]  
# a. Ubah jumlah buku menjadi 8.  
transaksi[0]["jumlah"] = 8
print(transaksi)
print()
# b. Tambahkan 2 produk baru.  
transaksi.append({"produk": "pensil", "harga": 2000, "jumlah": 3})
transaksi.append({"produk": "charger", "harga": 15000, "jumlah": 10})
print(transaksi)
print()
# c. Hitung Total Pendapatan (Harga x Jumlah) untuk setiap transaksi menggunakan perulangan. 
# Tampilkan ringkasan seperti ini:  Produk: Buku | Total: 30000 Produk: Pena | Total: 50000 ... dan seterusnya.
indeks=0
for x in transaksi: 
    print(f"produk:{transaksi[indeks]["produk"]} | Total: {transaksi[indeks]["harga"]*transaksi[indeks]["jumlah"]}")
    indeks += 1
