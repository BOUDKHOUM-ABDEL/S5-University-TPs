package Exercice_1;

public class Doctorant extends Etudiant implements DroitRetrait{
    public Doctorant (String nom) {
        super(nom);
    
    }
    @Override
    public  boolean estAdmis(){
        return calculerMoyenne()>=10;
    }
    @Override
    public  String getNiveau(){
        return "Doctorant";
    }
     @Override
    public  void afficherDoits(){
        System.out.print(" |  " + getDureeMax() + " jours");
        System.out.print(" |  " + getDocuments());
    }

    @Override
    public int getDureeMax() {   
        return 60;
    }
    @Override
    public String getDocuments() {
        return "Baccalauréat et Licence";
    }
}
