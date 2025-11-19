#segitiga_08.py
# Program untuk menampilkan segitiga terbalik dari bintang (*)

# Meminta input dari pengguna
n = int(input("Masukkan angka : "))

# Loop untuk membuat segitiga terbalik
for i in range(n, 0, -1):
    # Spasi di depan
    for j in range(n - i):
        print(" ", end="")
    # Bintang
    for k in range((2 * i) - 1):
        print("*", end="")
    print()
# segitiga_keatas.py
# Program menampilkan segitiga ke atas

# Input jumlah baris
baris = int(input("Masukkan jumlah baris segitiga ke atas: "))

# Looping untuk mencetak segitiga
for i in range(1, baris + 1):
    # Spasi di awal
    print(" " * (baris - i) + "* " * i)
