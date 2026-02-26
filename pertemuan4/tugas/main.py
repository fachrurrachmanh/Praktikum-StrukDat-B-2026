from tabulate import tabulate
import kurs
import konverter


    
    
tabel = [[k, f"{v:,}"] for k, v in kurs.kurs.items()]
print(tabulate(tabel, headers=["Kode", "Kurs"], tablefmt="grid"))
    
 
dari = input("\nDari (IDR/USD/EUR/SGD/JPY): ").upper()
ke = input("Ke   (IDR/USD/EUR/SGD/JPY): ").upper()
    
try:
    jumlah = float(input("Jumlah: "))
        
    hasil = konverter.konversi(jumlah, dari, ke, kurs.kurs)
        
    if dari == "IDR":
        print(f"\nRp {jumlah:,.0f} = {hasil:.2f} {ke}")
    else:
        print(f"\n{jumlah} {dari} = Rp {hasil:,.0f}")
            
except ValueError:
    print("Error: Masukkan angka yang valid!")
except KeyError:
    print("Error: Kode mata uang tidak terdaftar!")

