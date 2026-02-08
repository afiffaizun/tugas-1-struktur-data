kapasitas = 10
nim = [None] * kapasitas
nama = [None] * kapasitas
jumlah_data = 0

while True:
    print("\n=== DATA MAHASISWA ===")
    print("1. Insert at beginning")
    print("2. Insert at given position")
    print("3. Insert at end")
    print("4. Delete from beginnin")
    print("5. Delete given position")
    print("6. Delete from end")
    print("7. Delete first occurrence")
    print("8. Show data")
    print("9. Exit")

    pilihan = input("Pilih Opsi: ")

    # =============== INSERT ===============
    if pilihan == "1":  # Insert at beginning
        if jumlah_data == kapasitas:
            print("Array penuh!")
        else:
            n = input("Masukkan NIM  : ")
            nm = input("Masukkan Nama : ")

            for i in range(jumlah_data, 0, -1):
                nim[i] = nim[i - 1]
                nama[i] = nama[i - 1]

            nim[0] = n
            nama[0] = nm
            jumlah_data += 1

    elif pilihan == "2":  # Insert at given position
        if jumlah_data == kapasitas:
            print("Array penuh!")
        else:
            pos = int(input(f"Masukkan index (0 - {jumlah_data}): "))

            if pos < 0 or pos > jumlah_data:
                print("Index tidak valid!")
            else:
                n = input("Masukkan NIM  : ")
                nm = input("Masukkan Nama : ")

                for i in range(jumlah_data, pos, -1):
                    nim[i] = nim[i - 1]
                    nama[i] = nama[i - 1]

                nim[pos] = n
                nama[pos] = nm
                jumlah_data += 1

    elif pilihan == "3":  # Insert at end
        if jumlah_data == kapasitas:
            print("Array penuh!")
        else:
            nim[jumlah_data] = input("Masukkan NIM  : ")
            nama[jumlah_data] = input("Masukkan Nama : ")
            jumlah_data += 1

    # =============== DELETE ===============
    elif pilihan == "4":  # Delete from beginning
        if jumlah_data == 0:
            print("Data kosong!")
        else:
            for i in range(jumlah_data - 1):
                nim[i] = nim[i + 1]
                nama[i] = nama[i + 1]
            jumlah_data -= 1

    elif pilihan == "5":  # Delete given position
        if jumlah_data == 0:
            print("Data kosong!")
        else:
            pos = int(input(f"Masukkan index (0 - {jumlah_data - 1}): "))

            if pos < 0 or pos >= jumlah_data:
                print("Index tidak valid!")
            else:
                for i in range(pos, jumlah_data - 1):
                    nim[i] = nim[i + 1]
                    nama[i] = nama[i + 1]
                jumlah_data -= 1

    elif pilihan == "6":  # Delete from end
        if jumlah_data == 0:
            print("Data kosong!")
        else:
            jumlah_data -= 1

    elif pilihan == "7":  # Delete first occurrence
        if jumlah_data == 0:
            print("Data kosong!")
        else:
            target = input("Masukkan NIM yang ingin dihapus: ")
            indeks = -1

            for i in range(jumlah_data):
                if nim[i] == target:
                    indeks = i
                    break

            if indeks == -1:
                print("Data tidak ditemukan!")
            else:
                for i in range(indeks, jumlah_data - 1):
                    nim[i] = nim[i + 1]
                    nama[i] = nama[i + 1]
                jumlah_data -= 1

    # SHOW Data
    elif pilihan == "8":
        if jumlah_data == 0:
            print("Data kosong!")
        else:
            print("\nIndex | NIM           | Nama")
            for i in range(jumlah_data):
                print(i, "    | ", nim[i], " | ", nama[i])

    elif pilihan == "9":
        print("Keluar dari program...")
        break

    else:
        print("Pilihan tidak valid!")
