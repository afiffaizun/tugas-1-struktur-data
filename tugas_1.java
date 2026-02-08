import java.util.Scanner;

public class tugas_1 {

    static final int KAPASITAS = 10;
    static String[] nim = new String[KAPASITAS];
    static String[] nama = new String[KAPASITAS];
    static int jumlahData = 0;

    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int pilihan;

        do {
            menu();
            pilihan = input.nextInt();
            input.nextLine(); // buang newline

            switch (pilihan) {
                case 1:
                    insertBeginning();
                    break;
                case 2:
                    insertAtPosition();
                    break;
                case 3:
                    insertEnd();
                    break;
                case 4:
                    deleteBeginning();
                    break;
                case 5:
                    deleteAtPosition();
                    break;
                case 6:
                    deleteEnd();
                    break;
                case 7:
                    deleteFirstOccurrence();
                    break;
                case 8:
                    showData();
                    break;
                case 9:
                    System.out.println("Keluar dari program...");
                    break;
                default:
                    System.out.println("Pilihan tidak valid!");
            }
        } while (pilihan != 9);
    }

    static void menu() {
        System.out.println("\n=== DATA MAHASISWA ===");
        System.out.println("1. Insert at beginning (index 0)");
        System.out.println("2. Insert at given position (index array)");
        System.out.println("3. Insert at end");
        System.out.println("4. Delete from beginning (index 0)");
        System.out.println("5. Delete given position (index array)");
        System.out.println("6. Delete from end");
        System.out.println("7. Delete first occurrence (berdasarkan NIM)");
        System.out.println("8. Show data");
        System.out.println("9. Exit");
        System.out.print("Pilih menu: ");
    }

    static void insertBeginning() {
        if (jumlahData == KAPASITAS) {
            System.out.println("Array penuh!");
            return;
        }

        System.out.print("Masukkan NIM  : ");
        String n = input.nextLine();
        System.out.print("Masukkan Nama : ");
        String nm = input.nextLine();

        for (int i = jumlahData; i > 0; i--) {
            nim[i] = nim[i - 1];
            nama[i] = nama[i - 1];
        }

        nim[0] = n;
        nama[0] = nm;
        jumlahData++;
    }

    static void insertAtPosition() {
        if (jumlahData == KAPASITAS) {
            System.out.println("Array penuh!");
            return;
        }

        System.out.print("Masukkan index (0 - " + jumlahData + "): ");
        int pos = input.nextInt();
        input.nextLine();

        if (pos < 0 || pos > jumlahData) {
            System.out.println("Index tidak valid!");
            return;
        }

        System.out.print("Masukkan NIM  : ");
        String n = input.nextLine();
        System.out.print("Masukkan Nama : ");
        String nm = input.nextLine();

        for (int i = jumlahData; i > pos; i--) {
            nim[i] = nim[i - 1];
            nama[i] = nama[i - 1];
        }

        nim[pos] = n;
        nama[pos] = nm;
        jumlahData++;
    }

    static void insertEnd() {
        if (jumlahData == KAPASITAS) {
            System.out.println("Array penuh!");
            return;
        }

        System.out.print("Masukkan NIM  : ");
        nim[jumlahData] = input.nextLine();
        System.out.print("Masukkan Nama : ");
        nama[jumlahData] = input.nextLine();

        jumlahData++;
    }

    static void deleteBeginning() {
        if (jumlahData == 0) {
            System.out.println("Data kosong!");
            return;
        }

        for (int i = 0; i < jumlahData - 1; i++) {
            nim[i] = nim[i + 1];
            nama[i] = nama[i + 1];
        }

        jumlahData--;
    }

    static void deleteAtPosition() {
        if (jumlahData == 0) {
            System.out.println("Data kosong!");
            return;
        }

        System.out.print("Masukkan index (0 - " + (jumlahData - 1) + "): ");
        int pos = input.nextInt();
        input.nextLine();

        if (pos < 0 || pos >= jumlahData) {
            System.out.println("Index tidak valid!");
            return;
        }

        for (int i = pos; i < jumlahData - 1; i++) {
            nim[i] = nim[i + 1];
            nama[i] = nama[i + 1];
        }

        jumlahData--;
    }

    static void deleteEnd() {
        if (jumlahData == 0) {
            System.out.println("Data kosong!");
            return;
        }

        jumlahData--;
    }

    static void deleteFirstOccurrence() {
        if (jumlahData == 0) {
            System.out.println("Data kosong!");
            return;
        }

        System.out.print("Masukkan NIM yang ingin dihapus: ");
        String target = input.nextLine();

        int index = -1;
        for (int i = 0; i < jumlahData; i++) {
            if (nim[i].equals(target)) {
                index = i;
                break;
            }
        }

        if (index == -1) {
            System.out.println("Data tidak ditemukan!");
            return;
        }

        for (int i = index; i < jumlahData - 1; i++) {
            nim[i] = nim[i + 1];
            nama[i] = nama[i + 1];
        }

        jumlahData--;
    }

    static void showData() {
        if (jumlahData == 0) {
            System.out.println("Data kosong!");
            return;
        }

        System.out.println("\nIndex | NIM        | Nama");
        for (int i = 0; i < jumlahData; i++) {
            System.out.println(i + "     | " + nim[i] + " | " + nama[i]);
        }
    }
}
