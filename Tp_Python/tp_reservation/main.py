# main.py
from models.vehicule import Vehicule



vehicules = []
clients = []
reservations = []

def ajouter_vehicule():
    marque = input("Marque du vehicule: ")
    modele = input("Modele du vehicule: ")
    prix = float(input("Prix de location par jour: "))
    v = Vehicule(marque, modele, prix)
    vehicules.append(v)
    print("Vehicule ajoute avec succes !")
    print(v.afficher_infos())

def ajouter_client():
    nom = input("Nom du client: ")
    prenom = input("Prenom du client: ")
    client = {"nom": nom, "prenom": prenom}
    clients.append(client)
    print("Client ajoute avec succes !")

def reserver_vehicule():
    if not vehicules or not clients:
        print("Ajoutez d'abord des vehicules et des clients.")
        return
    print("Liste des vehicules disponibles:")
    for i, v in enumerate(vehicules, start=1):
        print(f"{i}. {v.afficher_infos()}")
    choix_v = int(input("Choisissez un vehicule (numero): ")) - 1

    print("Liste des clients:")
    for i, c in enumerate(clients, start=1):
        print(f"{i}. {c['prenom']} {c['nom']}")
    choix_c = int(input("Choisissez un client (numero): ")) - 1

    reservation = {"client": clients[choix_c], "vehicule": vehicules[choix_v]}
    reservations.append(reservation)
    print("Reservation effectuee avec succes !")

def afficher_reservations():
    if not reservations:
        print("Aucune reservation.")
        return
    print("=== Liste des reservations ===")
    for r in reservations:
        client = r["client"]
        vehicule = r["vehicule"]
        print(f"{client['prenom']} {client['nom']} a reserve {vehicule.afficher_infos()}")

def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Ajouter vehicule")
        print("2. Ajouter client")
        print("3. Reserver un vehicule")
        print("4. Afficher reservations")
        print("5. Quitter")

        choix = input("Votre choix: ")

        if choix == "1":
            ajouter_vehicule()
        elif choix == "2":
            ajouter_client()
        elif choix == "3":
            reserver_vehicule()
        elif choix == "4":
            afficher_reservations()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, reessayez.")

if __name__ == "__main__":
    menu()
