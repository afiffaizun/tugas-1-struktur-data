import java.util.Scanner;

public class tugas_1 {

    static final int kapasitas = 10;
    static String[] nim = new String[kapasitas];
    static String[] nama = new String[kapasitas];
    static int count = 0;

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
        System.out.println("\n=== MENU DATA MAHASISWA ===");
        System.out.println("1. Insert at beginning");
        System.out.println("2. Insert at given position");
        System.out.println("3. Insert at end");
        System.out.println("4. Delete from beginning");
        System.out.println("5. Delete given position");
        System.out.println("6. Delete from end");
        System.out.println("7. Delete first occurrence");
        System.out.println("8. Show data");
        System.out.println("9. Exit");
        System.out.print("Pilih menu: ");
    }

    // ================= INSERT =================

    static void insertBeginning() {
        if (count == kapasitas) {
            System.out.println("Array penuh!");
            return;
        }

        System.out.print("Masukkan NIM  : ");
        String n = input.nextLine();
        System.out.print("Masukkan Nama : ");
        String nm = input.nextLine();

        for (int i = count; i > 0; i--) {
            nim[i] = nim[i - 1];
            nama[i] = nama[i - 1];
        }

        nim[0] = n;
        nama[0] = nm;
        count++;
    }

    static void insertAtPosition() {
        if (count == kapasitas) {
            System.out.println("Array penuh!");
            return;
        }

        System.out.print("Masukkan posisi (0 - " + count  + "): ");
        int pos = input.nextInt();
        input.nextLine();

        if (pos < 1 || pos > count + 1) {
            System.out.println("Posisi tidak valid!");
            return;
        }

        System.out.print("Masukkan NIM  : ");
        String n = input.nextLine();
        System.out.print("Masukkan Nama : ");
        String nm = input.nextLine();

        for (int i = count; i >= pos; i--) {
            nim[i] = nim[i - 1];
            nama[i] = nama[i - 1];
        }

        nim[pos - 1] = n;
        nama[pos - 1] = nm;
        count++;
    }

    static void insertEnd() {
        if (count == kapasitas) {
            System.out.println("Array penuh!");
            return;
        }

        System.out.print("Masukkan NIM  : ");
        nim[count] = input.nextLine();
        System.out.print("Masukkan Nama : ");
        nama[count] = input.nextLine();

        count++;
    }

    // ================= DELETE =================

    static void deleteBeginning() {
        if (count == 0) {
            System.out.println("Data kosong!");
            return;
        }

        for (int i = 0; i < count - 1; i++) {
            nim[i] = nim[i + 1];
            nama[i] = nama[i + 1];
        }

        count--;
    }

    static void deleteAtPosition() {
        if (count == 0) {
            System.out.println("Data kosong!");
            return;
        }

        System.out.print("Masukkan posisi (1 - " + count + "): ");
        int pos = input.nextInt();

        if (pos < 1 || pos > count) {
            System.out.println("Posisi tidak valid!");
            return;
        }

        for (int i = pos - 1; i < count - 1; i++) {
            nim[i] = nim[i + 1];
            nama[i] = nama[i + 1];
        }

        count--;
    }

    static void deleteEnd() {
        if (count == 0) {
            System.out.println("Data kosong!");
            return;
        }

        count--;
    }

    static void deleteFirstOccurrence() {
        if (count == 0) {
            System.out.println("Data kosong!");
            return;
        }

        System.out.print("Masukkan NIM yang ingin dihapus: ");
        String target = input.nextLine();

        int index = -1;
        for (int i = 0; i < count; i++) {
            if (nim[i].equals(target)) {
                index = i;
                break;
            }
        }

        if (index == -1) {
            System.out.println("Data tidak ditemukan!");
            return;
        }

        for (int i = index; i < count - 1; i++) {
            nim[i] = nim[i + 1];
            nama[i] = nama[i + 1];
        }

        count--;
    }

    // ================= SHOW =================

    static void showData() {
        if (count == 0) {
            System.out.println("Data kosong!");
            return;
        }

        System.out.println("\nData Mahasiswa:");
        for (int i = 0; i < count; i++) {
            System.out.println((i + 1) + ". " + nim[i] + " - " + nama[i]);
        }
    }
}
