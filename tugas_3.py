# tugas_3.py
# Program verifikasi tipe data input dari pengguna

# Meminta input dari pengguna
data = input("Masukkan Umur Kamu: ")

# Percobaan mengubah input menjadi integer
try:
    angka = int(data)
    print(f"Data ini adalah angka integer. Angka = {angka}")

# Jika gagal, coba ubah ke float
except ValueError:
    try:
        angka = float(data)
        print(f"Data ini adalah angka float. Angka = {angka}")
    except ValueError:
        # Jika bukan integer atau float, maka tipe data lain (string)
        print(f"Data yang anda inputkan adalah tipe string")