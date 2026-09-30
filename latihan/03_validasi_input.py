# Input: nilai ujian 0 sampai 100
# Proses: memeriksa apakah nilai berada dalam rentang 0 sampai 100
# Kondisi berhenti: perulangan berhenti jika nilai sudah valid
# Output: nilai yang diterima

nilai = float(input("Nilai 0-100: "))

while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

print(f"Nilai diterima: {nilai}")
