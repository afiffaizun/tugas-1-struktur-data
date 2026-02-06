MAX = 10

def clear_screen():
    print("\n" * 2)

def print_menu():
    print("Program Manajemen Data Mahasiswa")
    print("1. Insert at beginning")
    print("2. Insert at given position")
    print("3. Insert at end")
    print("4. Delete from beginning")
    print("5. Delete given position")
    print("6. Delete from end")
    print("7. Delete first occurrence (by NIM)")
    print("8. Show data")
    print("9. Exit")

def show_data(nim_arr, nama_arr, count):
    if count == 0:
        print("Data kosong.")
        return
    print("{:<3} | {:<12} | {}".format("No", "NIM", "Nama"))
    print("-" * 36)
    for i in range(count):
        print("{:<3} | {:<12} | {}".format(i, nim_arr[i], nama_arr[i]))

def input_nim_nama():
    nim = input("Masukkan NIM: ").strip()
    nama = input("Masukkan Nama: ").strip()
    return nim, nama

def insert_at_beginning(nim_arr, nama_arr, count):
    if count >= MAX:
        print("Gagal: array penuh.")
        return count
    nim, nama = input_nim_nama()
    # geser ke kanan
    for i in range(count, 0, -1):
        nim_arr[i] = nim_arr[i-1]
        nama_arr[i] = nama_arr[i-1]
    nim_arr[0] = nim
    nama_arr[0] = nama
    count += 1
    print("Berhasil insert di awal.")
    return count

def insert_at_position(nim_arr, nama_arr, count):
    if count >= MAX:
        print("Gagal: array penuh.")
        return count
    print(f"Posisi tersedia untuk disisipkan: 0 .. {count} (maks {MAX-1})")
    try:
        pos = int(input("Masukkan posisi (0-based): ").strip())
    except:
        print("Input posisi tidak valid.")
        return count
    if pos < 0 or pos > count or pos >= MAX:
        print("Posisi tidak valid.")
        return count
    nim, nama = input_nim_nama()
    # geser kanan dari count-1 ke pos
    for i in range(count, pos, -1):
        nim_arr[i] = nim_arr[i-1]
        nama_arr[i] = nama_arr[i-1]
    nim_arr[pos] = nim
    nama_arr[pos] = nama
    count += 1
    print(f"Berhasil insert di posisi {pos}.")
    return count

def insert_at_end(nim_arr, nama_arr, count):
    if count >= MAX:
        print("Gagal: array penuh.")
        return count
    nim, nama = input_nim_nama()
    nim_arr[count] = nim
    nama_arr[count] = nama
    count += 1
    print("Berhasil insert di akhir.")
    return count

def delete_from_beginning(nim_arr, nama_arr, count):
    if count == 0:
        print("Gagal: array kosong.")
        return count
    # geser kiri
    for i in range(0, count-1):
        nim_arr[i] = nim_arr[i+1]
        nama_arr[i] = nama_arr[i+1]
    nim_arr[count-1] = None
    nama_arr[count-1] = None
    count -= 1
    print("Berhasil menghapus data dari awal.")
    return count

def delete_given_position(nim_arr, nama_arr, count):
    if count == 0:
        print("Gagal: array kosong.")
        return count
    try:
        pos = int(input(f"Masukkan posisi yang akan dihapus (0..{count-1}): ").strip())
    except:
        print("Input posisi tidak valid.")
        return count
    if pos < 0 or pos >= count:
        print("Posisi tidak valid.")
        return count
    for i in range(pos, count-1):
        nim_arr[i] = nim_arr[i+1]
        nama_arr[i] = nama_arr[i+1]
    nim_arr[count-1] = None
    nama_arr[count-1] = None
    count -= 1
    print(f"Berhasil menghapus posisi {pos}.")
    return count

def delete_from_end(nim_arr, nama_arr, count):
    if count == 0:
        print("Gagal: array kosong.")
        return count
    nim_arr[count-1] = None
    nama_arr[count-1] = None
    count -= 1
    print("Berhasil menghapus data dari akhir.")
    return count

def delete_first_occurrence(nim_arr, nama_arr, count):
    if count == 0:
        print("Gagal: array kosong.")
        return count
    target = input("Masukkan NIM yang akan dihapus (first occurrence): ").strip()
    idx = -1
    for i in range(count):
        if nim_arr[i] == target:
            idx = i
            break
    if idx == -1:
        print("NIM tidak ditemukan.")
        return count
    for i in range(idx, count-1):
        nim_arr[i] = nim_arr[i+1]
        nama_arr[i] = nama_arr[i+1]
    nim_arr[count-1] = None
    nama_arr[count-1] = None
    count -= 1
    print(f"Berhasil menghapus NIM {target} pada posisi {idx}.")
    return count

def main():
    nim_arr = [None] * MAX
    nama_arr = [None] * MAX
    count = 0
    while True:
        print_menu()
        choice = input("Pilih menu (1-9): ").strip()
        if choice == "1":
            count = insert_at_beginning(nim_arr, nama_arr, count)
        elif choice == "2":
            count = insert_at_position(nim_arr, nama_arr, count)
        elif choice == "3":
            count = insert_at_end(nim_arr, nama_arr, count)
        elif choice == "4":
            count = delete_from_beginning(nim_arr, nama_arr, count)
        elif choice == "5":
            count = delete_given_position(nim_arr, nama_arr, count)
        elif choice == "6":
            count = delete_from_end(nim_arr, nama_arr, count)
        elif choice == "7":
            count = delete_first_occurrence(nim_arr, nama_arr, count)
        elif choice == "8":
            show_data(nim_arr, nama_arr, count)
        elif choice == "9":
            print("Keluar program.")
            break
        else:
            print("Pilihan tidak valid.")
        input("\nTekan Enter untuk lanjut...")
        clear_screen()

if __name__ == "__main__":
    main()