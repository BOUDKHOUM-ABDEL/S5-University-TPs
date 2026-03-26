package Exercice_1;

public class EtudiantMaster extends Etudiant implements DroitRetrait{
    public EtudiantMaster(String nom) {
        super(nom);
    
    }
    @Override
    public  boolean estAdmis(){
        return calculerMoyenne()>=10;
    }
    @Override
    public  String getNiveau(){
        return "Master";
    }
     @Override
    public  void afficherDoits(){
        System.out.print(" | " + getDureeMax() + " jours");
        System.out.print(" | " + getDocuments());
    }

    @Override
    public int getDureeMax() {   
        return 30;
    }
    @Override
    public String getDocuments() {
        return "Baccalauréat";
    }

}
