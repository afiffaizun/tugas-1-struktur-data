kapasitas = 10
nim = [None] * kapasitas
nama = [None] * kapasitas
count = 0

while True:
    print("\n=== MENU DATA MAHASISWA ===")
    print("1. Insert at beginning")
    print("2. Insert at given position")
    print("3. Insert at end")
    print("4. Delete from beginning")
    print("5. Delete given position")
    print("6. Delete from end")
    print("7. Delete first occurrence")
    print("8. Show data")
    print("9. Exit")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":  # Insert at beginning
        if count == kapasitas:
            print("Array penuh!")
        else:
            n = input("Masukkan NIM  : ")
            nm = input("Masukkan Nama : ")

            for i in range(count, 0, -1):
                nim[i] = nim[i - 1]
                nama[i] = nama[i - 1]

            nim[0] = n
            nama[0] = nm
            count += 1

    elif pilihan == "2":  # Insert at given position
        if count == kapasitas:
            print("Array penuh!")
        else:
            pos = int(input(f"Masukkan posisi (1 - {count + 1}): "))

            if pos < 1 or pos > count + 1:
                print("Posisi tidak valid!")
            else:
                n = input("Masukkan NIM  : ")
                nm = input("Masukkan Nama : ")

                index = pos - 1
                for i in range(count, index, -1):
                    nim[i] = nim[i - 1]
                    nama[i] = nama[i - 1]

                nim[index] = n
                nama[index] = nm
                count += 1

    elif pilihan == "3":  # Insert at end
        if count == kapasitas:
            print("Array penuh!")
        else:
            nim[count] = input("Masukkan NIM  : ")
            nama[count] = input("Masukkan Nama : ")
            count += 1

    elif pilihan == "4":  # Delete from beginning
        if count == 0:
            print("Data kosong!")
        else:
            for i in range(count - 1):
                nim[i] = nim[i + 1]
                nama[i] = nama[i + 1]
            count -= 1

    elif pilihan == "5":  # Delete given position
        if count == 0:
            print("Data kosong!")
        else:
            pos = int(input(f"Masukkan posisi (1 - {count}): "))

            if pos < 1 or pos > count:
                print("Posisi tidak valid!")
            else:
                index = pos - 1
                for i in range(index, count - 1):
                    nim[i] = nim[i + 1]
                    nama[i] = nama[i + 1]
                count -= 1

    elif pilihan == "6":  # Delete from end
        if count == 0:
            print("Data kosong!")
        else:
            count -= 1

    elif pilihan == "7":  # Delete first occurrence
        if count == 0:
            print("Data kosong!")
        else:
            target = input("Masukkan NIM yang ingin dihapus: ")
            index = -1

            for i in range(count):
                if nim[i] == target:
                    index = i
                    break

            if index == -1:
                print("Data tidak ditemukan!")
            else:
                for i in range(index, count - 1):
                    nim[i] = nim[i + 1]
                    nama[i] = nama[i + 1]
                count -= 1

    # Show data
    elif pilihan == "8":
        if count == 0:
            print("Data kosong!")
        else:
            print("\nData Mahasiswa:")
            for i in range(count):
                print(i + 1, nim[i], "-", nama[i])

    elif pilihan == "9":
        print("Keluar dari program...")
        break

    else:
        print("Pilihan tidak valid!")
