# ====== DEKLARASI ======
kapasitas = 10
nim = [None] * kapasitas
nama = [None] * kapasitas
jumlah_data = 0


# ====== FUNCTION ======
def insert_awal():
    global jumlah_data
    if jumlah_data == kapasitas:
        print("Array penuh!")
        return

    n = input("Masukkan NIM  : ")
    nm = input("Masukkan Nama : ")

    for i in range(jumlah_data, 0, -1):
        nim[i] = nim[i - 1]
        nama[i] = nama[i - 1]

    nim[0] = n
    nama[0] = nm
    jumlah_data += 1


def insert_posisi():
    global jumlah_data
    if jumlah_data == kapasitas:
        print("Array penuh!")
        return

    pos = int(input(f"Masukkan index (0 - {jumlah_data}): "))
    if pos < 0 or pos > jumlah_data:
        print("Index tidak valid!")
        return

    n = input("Masukkan NIM  : ")
    nm = input("Masukkan Nama : ")

    for i in range(jumlah_data, pos, -1):
        nim[i] = nim[i - 1]
        nama[i] = nama[i - 1]

    nim[pos] = n
    nama[pos] = nm
    jumlah_data += 1


def insert_akhir():
    global jumlah_data
    if jumlah_data == kapasitas:
        print("Array penuh!")
        return

    nim[jumlah_data] = input("Masukkan NIM  : ")
    nama[jumlah_data] = input("Masukkan Nama : ")
    jumlah_data += 1


def delete_awal():
    global jumlah_data
    if jumlah_data == 0:
        print("Data kosong!")
        return

    for i in range(jumlah_data - 1):
        nim[i] = nim[i + 1]
        nama[i] = nama[i + 1]

    jumlah_data -= 1


def delete_posisi():
    global jumlah_data
    if jumlah_data == 0:
        print("Data kosong!")
        return

    pos = int(input(f"Masukkan index (0 - {jumlah_data - 1}): "))
    if pos < 0 or pos >= jumlah_data:
        print("Index tidak valid!")
        return

    for i in range(pos, jumlah_data - 1):
        nim[i] = nim[i + 1]
        nama[i] = nama[i + 1]

    jumlah_data -= 1


def delete_akhir():
    global jumlah_data
    if jumlah_data == 0:
        print("Data kosong!")
        return

    jumlah_data -= 1


def delete_pertama():
    global jumlah_data
    if jumlah_data == 0:
        print("Data kosong!")
        return

    target = input("Masukkan NIM yang ingin dihapus: ")
    indeks = -1

    for i in range(jumlah_data):
        if nim[i] == target:
            indeks = i
            break

    if indeks == -1:
        print("Data tidak ditemukan!")
        return

    for i in range(indeks, jumlah_data - 1):
        nim[i] = nim[i + 1]
        nama[i] = nama[i + 1]

    jumlah_data -= 1


def show_data():
    if jumlah_data == 0:
        print("Data kosong!")
        return

    print("\nIndex | NIM        | Nama")
    for i in range(jumlah_data):
        print(i, "    |", nim[i], "|", nama[i])


# ====== MAIN PROGRAM ======
while True:
    print("\n=== DATA MAHASISWA ===")
    print("1. Insert at beginning")
    print("2. Insert at given position")
    print("3. Insert at end")
    print("4. Delete from beginning")
    print("5. Delete given position")
    print("6. Delete from end")
    print("7. Delete first occurrence")
    print("8. Show data")
    print("9. Exit")

    pilihan = input("Pilih Opsi: ")

    match pilihan:
        case "1":
            insert_awal()
        case "2":
            insert_posisi()
        case "3":
            insert_akhir()
        case "4":
            delete_awal()
        case "5":
            delete_posisi()
        case "6":
            delete_akhir()
        case "7":
            delete_pertama()
        case "8":
            show_data()
        case "9":
            print("Keluar dari program...")
            break
        case _:
            print("Pilihan tidak valid!")
