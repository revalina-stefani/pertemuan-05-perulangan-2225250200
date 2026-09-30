# Input: bilangan bulat n
# Proses: menghitung perkalian n dengan 1 sampai 10
# Kondisi berhenti: perulangan berhenti setelah i mencapai 10
# Output: tabel perkalian n x 1 sampai n x 10

n = int(input("Bilangan: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
