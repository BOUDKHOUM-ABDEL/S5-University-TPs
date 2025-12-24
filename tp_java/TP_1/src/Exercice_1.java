import java.util.Scanner;

public class Exercice_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] Students;
        double[] Notes;
        int N = 3;
        Students = new String[N];
        Notes = new double[N];

        for (int i = 0; i < N; i++) {
            System.out.print("Name of Student " + (i + 1) + " : ");
            Students[i] = sc.nextLine();

            System.out.print("Enter " + Students[i] + "'s Note : ");
            Notes[i] = sc.nextDouble();
            sc.nextLine();
        }

        for (int i = 0; i < N; i++) {
            System.out.print(Students[i] + " 's Note is : " + Notes[i] + "\n");
        }
        double total = 0;
        for (int i = 0; i < N; i++) {
            total = total + Notes[i];
        }
        System.out.println("Average Note is : " + total / N);
        int student_adm = 0;
        for (int i = 0; i < N; i++) {
            if (Notes[i] >= 10) {
                student_adm++;
            }
        }
        System.out.println("the number of students who passed (grade ≥ 10) is : " + student_adm);

    }
}
