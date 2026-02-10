kelas_A = {"Struktur Data", "Basis Data", "AI",
"Pemrograman Web"}
kelas_B = {"Struktur Data", "Machine Learning", "AI",
"Cloud Computing"}

#1.mata kuliah yang diambil kedua kelas
for x in kelas_A:
    if x in kelas_B:
        print(x)
#2.mata kuliah yang hanya diambil kelas A
for x in kelas_A:
    if x not in kelas_B:
        print(x)


