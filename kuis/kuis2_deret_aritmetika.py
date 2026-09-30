# Input: suku pertama a, beda d, dan banyak suku n
# Proses: menghasilkan setiap suku dan menjumlahkannya
# Kondisi berhenti: perulangan selesai setelah n suku
# Output: nomor suku, nilai setiap suku, dan jumlah akhir

print("Deret Aritmetika")

a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))

n = int(input("Banyak suku n: "))

while n <= 0:
    print("Banyak suku harus lebih dari 0.")
    n = int(input("Banyak suku n: "))

total = 0

for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1} = {suku}")

print(f"Jumlah = {total:.2f}")

