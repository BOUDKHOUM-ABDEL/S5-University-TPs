from models.vehicule import Vehicule
from models.client import Client
from models.reservation import Reservation
from utils.outils import afficher_titre, mesure_temps

class GestionReservations:
    """Service de gestion des réservations."""
    
    _total_reservations = 0
    _moyens_paiement = []
    
    def __init__(self):
        self.vehicules_disponibles = []
        self.clients_enregistres = []
        self.reservations_effectuees = []
        
    def ajouter_vehicule(self, vehicule: Vehicule):
        self.vehicules_disponibles.append(vehicule)
        print(f"Véhicule ajouté : {vehicule.marque} {vehicule.modele}")
        
    def ajouter_client(self, client: Client):
        self.clients_enregistres.append(client)
        print(f"Client ajouté : {client.nom} {client.prenom}")
        
    @mesure_temps
    def reserver_vehicule(self, id_client: str, id_vehicule: str, duree: int, **kwargs):
        client = next((c for c in self.clients_enregistres if c.id == id_client), None)
        vehicule = next((v for v in self.vehicules_disponibles if v.id == id_vehicule), None)
        
        if not client:
            print("Erreur : Client introuvable.")
            return False
            
        if not vehicule:
            print("Erreur : Véhicule introuvable ou déjà réservé.")
            return False
            
        self.vehicules_disponibles.remove(vehicule)
        
        reservation = Reservation(client, vehicule, duree)
        if "paiement" in kwargs:
            GestionReservations._moyens_paiement.append(kwargs["paiement"])
            
        self.reservations_effectuees.append(reservation)
        GestionReservations._total_reservations += 1
        
        print(f"Réservation confirmée pour {client.nom} ({vehicule.marque}).")
        return True
        
    def afficher_catalogue(self):
        afficher_titre("Catalogue des Véhicules Disponibles")
        if not self.vehicules_disponibles:
            print("Aucun véhicule disponible.")
        for v in self.vehicules_disponibles:
            print(f"[{v.type_vehicule()}] ", end="")
            v.afficher_details()
            
    def afficher_reservations(self):
        afficher_titre("Liste des Réservations")
        for res in self.reservations_effectuees:
            res.resume()
            
    @classmethod
    def statistiques(cls):
        afficher_titre("Statistiques Globales")
        print(f"Nombre total de réservations : {cls._total_reservations}")
        if cls._moyens_paiement:
            frequent = max(set(cls._moyens_paiement), key=cls._moyens_paiement.count)
            print(f"Moyen de paiement le plus fréquent : {frequent}")
        else:
            print("Aucun paiement enregistré.")
