import java.util.Scanner;

public class Exercice_3 {

    public static void main(String[] args) {
        class Student {
            private String name;
            private double note;
            static int nbrStudens = 0;

            public Student(String name, double note) {
                this.name = name;
                this.note = note;
                nbrStudens++;
            }
            public String getName() {
                return this.name;
            }
            public Double getNote() {
                return this.note;
            }
            public boolean is_passed() {
                return this.note >= 10;
            }
            static int getNbrStudens() {
                return nbrStudens;
            }
        }

        Scanner sc = new Scanner(System.in);
        int N = 3;
        Student[] S = new Student[N];
        for (int i = 0; i < N; i++) {
            System.out.print("Name of Student " + (i + 1) + " : ");
            String name = sc.nextLine();

            System.out.print("Enter " + name + "'s Note : ");
            double note = sc.nextDouble();
            sc.nextLine();
            S[i] = new Student(name, note);
        }
        for (int i = 0; i < N; i++) {
            if (S[i].is_passed()) {
                System.out.println(S[i].getName() + " is passed");
            }
        }
        System.out.println("nombers of Students is : " + Student.getNbrStudens());
    }
}