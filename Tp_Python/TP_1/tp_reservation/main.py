from utils.outils import afficher_titre, demonstration_legb, debug
from models.voiture import Voiture
from models.moto import Moto
from models.client import Client
from services.gestion_reservations import GestionReservations

def menu():
    gestion = GestionReservations()
    
    # Jeu d'essai initial
    v1 = Voiture("Toyota", "Avensis", 50, 4)
    m1 = Moto("Yamaha", "MT-07", 80, 700)
    gestion.ajouter_vehicule(v1)
    gestion.ajouter_vehicule(m1)
    
    c1 = Client("Benali", "Karim", "BB12345")
    gestion.ajouter_client(c1)
    
    while True:
        afficher_titre("Menu Principal", style="-", longueur=30)
        print("1. Ajouter véhicule (Voiture)")
        print("2. Ajouter client")
        print("3. Afficher le catalogue")
        print("4. Réserver un véhicule")
        print("5. Afficher les réservations")
        print("6. Afficher les statistiques")
        print("7. Démonstration LEGB")
        print("8. Quitter")
        
        choix = input("Votre choix : ")
        
        if choix == "1":
            marque = input("Marque : ")
            modele = input("Modèle : ")
            prix = float(input("Prix par jour : "))
            portes = int(input("Nombre de portes : "))
            v = Voiture(marque, modele, prix, portes)
            gestion.ajouter_vehicule(v)
            
        elif choix == "2":
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            cin = input("CIN : ")
            c = Client(nom, prenom, cin)
            gestion.ajouter_client(c)
            
        elif choix == "3":
            gestion.afficher_catalogue()
            
        elif choix == "4":
            id_client = input("ID Client : ")
            id_vehic = input("ID Véhicule : ")
            duree = int(input("Durée (jours) : "))
            paiement = input("Moyen de paiement (Carte/Cash) : ")
            debug(id_client=id_client, id_vehicule=id_vehic, duree=duree, paiement=paiement)
            gestion.reserver_vehicule(id_client, id_vehic, duree, paiement=paiement)
            
        elif choix == "5":
            gestion.afficher_reservations()
            
        elif choix == "6":
            GestionReservations.statistiques()
            
        elif choix == "7":
            demonstration_legb()
            
        elif choix == "8":
            print("Au revoir.")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    menu()
