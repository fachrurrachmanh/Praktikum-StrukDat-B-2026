class Hantu:
    def __init__(self, jenis, nama, suara):
        self.jenis = jenis
        self.nama = nama
        self.suara = suara
    def jumpscare (self):
        print("cilupbah")
    def makan (self):
        print("nyamnyamnyam")

h1 = Hantu("pocong","jojo","hmmmmm")
h2 = Hantu("kunti","eeng","kikikikik")
h3 = Hantu("tuyul","hamud","alamak duitni")

h1.makan()
h2.jumpscare()

print(h1.nama, h1.jenis, h1.suara)
print(h2.nama, h2.jenis, h2.suara)
print(h3.nama, h3.jenis, h3.suara)

h1.nama = "rere"
print(h1.nama)