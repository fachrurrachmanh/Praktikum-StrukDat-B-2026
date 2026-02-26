def konversi(jumlah, dari_mata_uang, ke_mata_uang, kurs):
    if dari_mata_uang == "IDR":
        jumlah_idr = jumlah
    else:
        jumlah_idr = jumlah * kurs[dari_mata_uang]
    
    if ke_mata_uang == "IDR":
        return jumlah_idr
    else:
        return jumlah_idr / kurs[ke_mata_uang]