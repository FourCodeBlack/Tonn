Angka = int(input("Masukkan angka : "))
print(f"Tabel Perkalian {Angka}")

A = 0

while A <= 9:
    A = A + 1
    B = Angka * A
    print(Angka, "x", A, "=", B)
