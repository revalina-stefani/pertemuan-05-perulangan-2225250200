# Input: bilangan bulat positif n
# Proses: menghitung jumlah 1 + 2 + ... + n
# Kondisi berhenti: perulangan selesai setelah i mencapai n
# Output: jumlah bilangan dari 1 sampai n

n = int(input("n: "))

total = 0

for i in range(1, n + 1):
    total += i

print(f"Jumlah = {total}")
