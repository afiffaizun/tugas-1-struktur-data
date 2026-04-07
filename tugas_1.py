KAPASITAS = 10
nim = []
nama = []

def menu():
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

def insert_beginning():
    if len(nim) == KAPASITAS:
        print("Array penuh!")
        return

    n = input("Masukkan NIM  : ")
    nm = input("Masukkan Nama : ")

    nim.insert(0, n)
    nama.insert(0, nm)

def insert_at_position():
    if len(nim) == KAPASITAS:
        print("Array penuh!")
        return

    try:
        pos = int(input(f"Masukkan index (0 - {len(nim)}): "))
    except:
        print("Input harus angka!")
        return

    if pos < 0 or pos > len(nim):
        print("Index tidak valid!")
        return

    n = input("Masukkan NIM  : ")
    nm = input("Masukkan Nama : ")

    nim.insert(pos, n)
    nama.insert(pos, nm)

def insert_end():
    if len(nim) == KAPASITAS:
        print("Array penuh!")
        return

    n = input("Masukkan NIM  : ")
    nm = input("Masukkan Nama : ")

    nim.append(n)
    nama.append(nm)

def delete_beginning():
    if len(nim) == 0:
        print("Data kosong!")
        return

    nim.pop(0)
    nama.pop(0)

def delete_at_position():
    if len(nim) == 0:
        print("Data kosong!")
        return

    try:
        pos = int(input(f"Masukkan index (0 - {len(nim)-1}): "))
    except:
        print("Input harus angka!")
        return

    if pos < 0 or pos >= len(nim):
        print("Index tidak valid!")
        return

    nim.pop(pos)
    nama.pop(pos)

def delete_end():
    if len(nim) == 0:
        print("Data kosong!")
        return

    nim.pop()
    nama.pop()

def delete_first_occurrence():
    if len(nim) == 0:
        print("Data kosong!")
        return

    target = input("Masukkan NIM yang ingin dihapus: ")

    if target in nim:
        index = nim.index(target)
        nim.pop(index)
        nama.pop(index)
    else:
        print("Data tidak ditemukan!")

def show_data():
    if len(nim) == 0:
        print("Data kosong!")
        return

    print("\nIndex | NIM         | Nama")
    for i in range(len(nim)):
        print(f"{i}     | {nim[i]} | {nama[i]}")

# Program utama
while True:
    menu()
    try:
        pilihan = int(input("Pilih Opsi: "))
    except:
        print("Input harus angka!")
        continue

    if pilihan == 1:
        insert_beginning()
    elif pilihan == 2:
        insert_at_position()
    elif pilihan == 3:
        insert_end()
    elif pilihan == 4:
        delete_beginning()
    elif pilihan == 5:
        delete_at_position()
    elif pilihan == 6:
        delete_end()
    elif pilihan == 7:
        delete_first_occurrence()
    elif pilihan == 8:
        show_data()
    elif pilihan == 9:
        print("Keluar dari program...")
        break
    else:
        print("Pilihan tidak valid!")