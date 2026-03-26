from utils.outils import generer_id

class Client:
    """Classe représentant un client du système de réservation."""
    
    def __init__(self, nom: str, prenom: str, cin: str):
        self.id = generer_id("CLI")
        self.nom = nom
        self.prenom = prenom
        self.cin = cin
        
    def afficher_profil(self):
        """Affiche le profil du client."""
        print(f"Client [{self.id}]: {self.nom.upper()} {self.prenom.capitalize()} (CIN: {self.cin})")
