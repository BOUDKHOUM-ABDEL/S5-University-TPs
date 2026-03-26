package Exercice_1;

import java.util.ArrayList;

public abstract class Etudiant {

    protected String nom;
    protected ArrayList<Module> modules;

    public Etudiant(String nom) {
        this.nom = nom;
        this.modules = new ArrayList<>();
    }
    public void ajouterModule(Module m){
        modules.add(m);
    }
       
    public double calculerMoyenne(){
        if (modules.isEmpty() )return 0;
        double Somme = 0;
        for (Module m : modules) {
            Somme += m.getNote();
        }
        return Somme/modules.size();
    }

    public abstract boolean estAdmis();
    public abstract String getNiveau();
    public abstract void afficherDoits();

    public String toString(){
        return this.getNiveau()+" | " + this.nom + " | " + this.calculerMoyenne();
    }
}
// 2) Méthodes :
//  constructeur (initialise le nom)
//  ajouterModule(...)
//  calculerMoyenne()
//  estAdmis() (abstraite)
//  getNiveau() (abstraite)
//  toString() :  retourne un String: niveau | nom | moyenne