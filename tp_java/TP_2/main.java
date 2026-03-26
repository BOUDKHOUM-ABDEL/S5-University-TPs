package Exercice_1;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Etudiant> Etudiants = new ArrayList<>();
        Etudiant EL1 = new EtudiantLicence("Amine 1");
        Etudiant EL2 = new EtudiantLicence("Amine 2");
        Etudiant EL3 = new EtudiantLicence("Amine 3");
        Etudiant EL4 = new EtudiantLicence("Amine 4");
        
        Etudiant EM1 = new EtudiantMaster("Salim 1");
        Etudiant EM2 = new EtudiantMaster("Salim 2");
        Etudiant EM3 = new EtudiantMaster("Salim 3");
        Etudiant EM4 = new EtudiantMaster("Salim 4");

        Etudiant D1  = new Doctorant("Mounir 1") ;
        Etudiant D2  = new Doctorant("Mounir 2") ;
        Etudiant D3  = new Doctorant("Mounir 3") ;
        Etudiant D4  = new Doctorant("Mounir 4") ;    

        EL1.ajouterModule(new Module("L1","Info",12));
        EL1.ajouterModule(new Module("L2","Math",18.5));
        EL2.ajouterModule(new Module("L1","Info",9));
        EL2.ajouterModule(new Module("L2","Math",9));
        EL3.ajouterModule(new Module("L1","Info",19));
        EL3.ajouterModule(new Module("L2","Math",18.5));
        EL4.ajouterModule(new Module("L1","Info",17));
        EL4.ajouterModule(new Module("L2","Math",20));


        EM1.ajouterModule(new Module("M1", "Info", 10));
        EM1.ajouterModule(new Module("M2", "Math", 18.5));
        EM2.ajouterModule(new Module("M1", "Info", 17));
        EM2.ajouterModule(new Module("M2", "Math", 13.5));
        EM3.ajouterModule(new Module("M1", "Info", 12.5));
        EM3.ajouterModule(new Module("M2", "Math", 18.5));
        EM4.ajouterModule(new Module("M1", "Info", 7));
        EM4.ajouterModule(new Module("M2", "Math", 0));

        D1.ajouterModule(new Module("D1", "Recherche Avancée", 16));
        D1.ajouterModule(new Module("D2", "Méthodologie Scientifique", 18));
        D2.ajouterModule(new Module("D1", "Recherche Avancée", 14));
        D2.ajouterModule(new Module("D2", "Méthodologie Scientifique", 15.5));
        D3.ajouterModule(new Module("D1", "Recherche Avancée", 19));
        D3.ajouterModule(new Module("D2", "Méthodologie Scientifique", 17));
        D4.ajouterModule(new Module("D1", "Recherche Avancée", 13));
        D4.ajouterModule(new Module("D2", "Méthodologie Scientifique", 16));

        Etudiants.add(EM1);
        Etudiants.add(EM2);
        Etudiants.add(EM3);
        Etudiants.add(EM4);

        Etudiants.add(EL1);
        Etudiants.add(EL2);
        Etudiants.add(EL3);
        Etudiants.add(EL4);

        Etudiants.add(D1);
        Etudiants.add(D2);
        Etudiants.add(D3);
        Etudiants.add(D4);
       


       System.out.println("Niveau____Nom____Moyenne____Admis____________Duree____________Documents____\n");

        for(Etudiant e : Etudiants){

          System.out.print(e.toString() );
          if(e.estAdmis()){
            System.out.print(" | Admis");
          }else {
            System.out.print(" | non Admis");
          }
          e.afficherDoits();
          System.out.println();
          System.out.println("_______________________________________________________________");
          
        }
    }        
            
            
}
