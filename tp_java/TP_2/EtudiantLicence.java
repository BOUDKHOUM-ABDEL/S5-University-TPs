package Exercice_1;


public class EtudiantLicence extends Etudiant implements DroitRetrait{

    public EtudiantLicence(String nom) {
        super(nom);
    
    }
    @Override
    public  boolean estAdmis(){
        return calculerMoyenne()>=10;
    }
    @Override
    public  String getNiveau(){
        return "Licence";
    }
    @Override
    public  void afficherDoits(){
        System.out.print(" |  " + getDureeMax() + " jours");
        System.out.print(" |  " + getDocuments());
    }
    
    @Override
    public int getDureeMax() {
        
        return 15;
    }
    @Override
    public String getDocuments() {
        return "Baccalauréat";
    }

   
}
