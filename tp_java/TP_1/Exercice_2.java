import java.util.Scanner;

public class Exercice_2 {

    static class Student {
        private String name;
        private double note;

        public Student(String name, double note) {
            this.name = name;
            this.note = note;
        }

        public String getName() {
            return this.name;
        }

        public double getNote() {
            return this.note;
        }

        public boolean is_passed() {
            return this.note >= 10;
        }
    }

    public static void main(String[] args) {
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
        sc.close();
    }
}