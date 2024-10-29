# Rey Rizky Andifa
# F55123079


A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]

x = int(input("Masukkan nilai x: "))


count_x = A.count(x)

indeks_kemunculan = [i for i, value in enumerate(A) if value == x]

print(f"Nilai {x} muncul sebanyak {count_x} kali di A.")
print(f"Indeks kemunculan nilai {x} adalah: {indeks_kemunculan}")
