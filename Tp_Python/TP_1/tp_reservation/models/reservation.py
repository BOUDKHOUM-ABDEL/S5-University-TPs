from models.vehicule import Vehicule
from models.client import Client

class Reservation:
    """Classe représentant une réservation (Composition: Client, Vehicule)."""
    
    def __init__(self, client: Client, vehicule: Vehicule, duree_jours: int):
        self.client = client
        self.vehicule = vehicule
        self.duree_jours = duree_jours
        self.cout_total = self.calculer_cout()
        
    def calculer_cout(self) -> float:
        """Calcule le coût total de la réservation."""
        return self.vehicule.prix_location * self.duree_jours
        
    def resume(self):
        """Affiche un résumé détaillé de la réservation."""
        print("--- Résumé de la Réservation ---")
        self.client.afficher_profil()
        print("Véhicule réservé:")
        self.vehicule.afficher_details()
        print(f"Durée: {self.duree_jours} jours")
        print(f"Coût Total: {self.cout_total}€")
        print("--------------------------------")
