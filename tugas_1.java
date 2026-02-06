public class tugas_1 {
    static String[] nim = new String[10];
    static String[] nama = new String[10];
    static int count = 0;

    public static void main(String[] args) {
        int choice;
        java.util.Scanner scanner = new java.util.Scanner(System.in);

        while (true) {
            displayMenu();
            System.out.print("Pilih Opsi (1-9): ");
            choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    insertAtBeginning(scanner);
                    break;
                case 2:
                    insertAtPosition(scanner);
                    break;
                case 3:
                    insertAtEnd(scanner);
                    break;
                case 4:
                    deleteFromBeginning();
                    break;
                case 5:
                    deleteFromPosition(scanner);
                    break;
                case 6:
                    deleteFromEnd();
                    break;
                case 7:
                    deleteFirstOccurrence(scanner);
                    break;
                case 8:
                    showData();
                    break;
                case 9:
                    System.out.println("Program selesai!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Menu tidak valid!");
            }
        }
    }

    static void displayMenu() {
        System.out.println("\n=========== DATA MAHASISWA ============");
        System.out.println("1. Insert at beginning");
        System.out.println("2. Insert at given position");
        System.out.println("3. Insert at end");
        System.out.println("4. Delete from beginning");
        System.out.println("5. Delete given position");
        System.out.println("6. Delete from end");
        System.out.println("7. Delete first occurrence");
        System.out.println("8. Show data");
        System.out.println("9. Exit");
        System.out.println("==============================p==========");
    }

    static void insertAtBeginning(java.util.Scanner scanner) {
        if (count >= 10) {
            System.out.println("Array penuh!");
            return;
        }
        System.out.print("Masukkan NIM: ");
        String inputNim = scanner.nextLine();
        System.out.print("Masukkan Nama: ");
        String inputNama = scanner.nextLine();

        for (int i = count; i > 0; i--) {
            nim[i] = nim[i - 1];
            nama[i] = nama[i - 1];
        }
        nim[0] = inputNim;
        nama[0] = inputNama;
        count++;
        System.out.println("Data berhasil ditambahkan di awal!");
    }

    static void insertAtPosition(java.util.Scanner scanner) {
        if (count >= 10) {
            System.out.println("Array penuh!");
            return;
        }
        System.out.print("Masukkan posisi (0-" + count + "): ");
        int pos = scanner.nextInt();
        scanner.nextLine();

        if (pos < 0 || pos > count) {
            System.out.println("Posisi tidak valid!");
            return;
        }

        System.out.print("Masukkan NIM: ");
        String inputNim = scanner.nextLine();
        System.out.print("Masukkan Nama: ");
        String inputNama = scanner.nextLine();

        for (int i = count; i > pos; i--) {
            nim[i] = nim[i - 1];
            nama[i] = nama[i - 1];
        }
        nim[pos] = inputNim;
        nama[pos] = inputNama;
        count++;
        System.out.println("Data berhasil ditambahkan di posisi " + pos + "!");
    }

    static void insertAtEnd(java.util.Scanner scanner) {
        if (count >= 10) {
            System.out.println("Array penuh!");
            return;
        }
        System.out.print("Masukkan NIM: ");
        String inputNim = scanner.nextLine();
        System.out.print("Masukkan Nama: ");
        String inputNama = scanner.nextLine();

        nim[count] = inputNim;
        nama[count] = inputNama;
        count++;
        System.out.println("Data berhasil ditambahkan di akhir!");
    }

    static void deleteFromBeginning() {
        if (count == 0) {
            System.out.println("Array kosong!");
            return;
        }
        for (int i = 0; i < count - 1; i++) {
            nim[i] = nim[i + 1];
            nama[i] = nama[i + 1];
        }
        nim[count - 1] = null;
        nama[count - 1] = null;
        count--;
        System.out.println("Data di awal berhasil dihapus!");
    }

    static void deleteFromPosition(java.util.Scanner scanner) {
        if (count == 0) {
            System.out.println("Array kosong!");
            return;
        }
        System.out.print("Masukkan posisi yang ingin dihapus (0-" + (count - 1) + "): ");
        int pos = scanner.nextInt();

        if (pos < 0 || pos >= count) {
            System.out.println("Posisi tidak valid!");
            return;
        }

        for (int i = pos; i < count - 1; i++) {
            nim[i] = nim[i + 1];
            nama[i] = nama[i + 1];
        }
        nim[count - 1] = null;
        nama[count - 1] = null;
        count--;
        System.out.println("Data di posisi " + pos + " berhasil dihapus!");
    }

    static void deleteFromEnd() {
        if (count == 0) {
            System.out.println("Array kosong!");
            return;
        }
        nim[count - 1] = null;
        nama[count - 1] = null;
        count--;
        System.out.println("Data di akhir berhasil dihapus!");
    }

    static void deleteFirstOccurrence(java.util.Scanner scanner) {
        if (count == 0) {
            System.out.println("Array kosong!");
            return;
        }
        System.out.print("Masukkan NIM yang ingin dihapus: ");
        String searchNim = scanner.nextLine();

        int foundPos = -1;
        for (int i = 0; i < count; i++) {
            if (nim[i].equals(searchNim)) {
                foundPos = i;
                break;
            }
        }

        if (foundPos == -1) {
            System.out.println("Data tidak ditemukan!");
            return;
        }

        for (int i = foundPos; i < count - 1; i++) {
            nim[i] = nim[i + 1];
            nama[i] = nama[i + 1];
        }
        nim[count - 1] = null;
        nama[count - 1] = null;
        count--;
        System.out.println("Data dengan NIM " + searchNim + " berhasil dihapus!");
    }

    static void showData() {
        if (count == 0) {
            System.out.println("Array kosong!");
            return;
        }
        System.out.println("\n=== DATA MAHASISWA ===");
        System.out.println("Jumlah data: " + count);
        System.out.println("No | NIM           | Nama");
        System.out.println("---|---------------|---------------------");
        for (int i = 0; i < count; i++) {
            System.out.printf("%2d | %-8s | %s%n", i + 1, nim[i], nama[i]);
        }
        System.out.println();
    }
}