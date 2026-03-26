import java.util.Scanner;

public class Exercice_5 {

    // Define Student class outside main for clarity
    static class Student {
        private String name;
        private double note;
        static int nbrStudents = 0;

        public Student(String name, double note) {
            this.name = name;
            this.note = note;
            nbrStudents++;
        }

        public String getName() {
            return this.name;
        }

        public double getNote() {
            return this.note;
        }

        public boolean isPassed() {
            return this.note >= 10;
        }

        public static int getNbrStudents() {
            return nbrStudents;
        }

        public boolean startsWith(char c) {
            return this.name.toLowerCase().charAt(0) == Character.toLowerCase(c);
        }

        public boolean contains(String s) {
            return this.name.toLowerCase().contains(s.toLowerCase());
        }
    }
    class EtudiantBoursier extends Student {
        public EtudiantBoursier(String name, double note) {
            super(name, note);
        }

        @Override
        public boolean isPassed() {
            return super.note >= 9;
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int N = 3;
        Student[] S = new Student[N];

        // Input students
        for (int i = 0; i < N; i++) {
            System.out.print("Name of Student " + (i + 1) + " : ");
            String name = sc.nextLine();

            System.out.print("Enter " + name + "'s Note : ");
            double note = sc.nextDouble();
            sc.nextLine(); // clear buffer

            S[i] = new Student(name, note);
        }

        // Display passed students
        for (int i = 0; i < N; i++) {
            if (S[i].isPassed()) {
                System.out.println(S[i].getName() + " has passed");
            }
        }

        // Display number of students
        System.out.println("Number of Students is : " + Student.getNbrStudents());

        // Check first student name
        if (S[0].startsWith('a')) {
            System.out.println(S[0].getName() + " starts with 'a'");
        } else {
            System.out.println(S[0].getName() + " does not start with 'a'");
        }

        if (S[0].contains("al")) {
            System.out.println(S[0].getName() + " contains 'al'");
        } else {
            System.out.println(S[0].getName() + " does not contain 'al'");
        }

        sc.close();
    }
}
