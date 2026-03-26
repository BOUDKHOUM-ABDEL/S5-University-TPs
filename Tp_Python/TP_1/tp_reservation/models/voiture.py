from models.vehicule import Vehicule

class Voiture(Vehicule):
    """Classe représentant une Voiture, hérite de Vehicule."""
    
    def __init__(self, marque: str, modele: str, prix_location: float, nb_portes: int):
        super().__init__(marque, modele, prix_location)
        self.nb_portes = nb_portes
        
    def type_vehicule(self):
        return "Voiture"
        
    def afficher_details(self):
        super().afficher_details()
        print(f"  -> Type: {self.type_vehicule()}, Portes: {self.nb_portes}")
        
    @staticmethod
    def est_suv(modele: str) -> bool:
        """Détermine si le modèle correspond à un SUV."""
        suv_modeles = ["X5", "Q7", "3008", "Tucson", "Duster", "Kadjar"]
        return modele in suv_modeles
