package Exercice_1;

public class Module {
    String code;
    String intitule;
    double note;

    public Module(String code, String intitule, double note) {
        this.code = code;
        this.intitule = intitule;
        this.note = note;
    }

    public double getNote() {
        return note;
    }
}
