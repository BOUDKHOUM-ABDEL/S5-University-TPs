from models.vehicule import Vehicule

class Moto(Vehicule):
    """Classe représentant une Moto, hérite de Vehicule."""
    
    def __init__(self, marque: str, modele: str, prix_location: float, cylindree: int):
        super().__init__(marque, modele, prix_location)
        self.cylindree = cylindree
        
    def type_vehicule(self):
        return "Moto"
        
    def afficher_details(self):
        super().afficher_details()
        print(f"  -> Type: {self.type_vehicule()}, Cylindrée: {self.cylindree}cc")
        
    @staticmethod
    def est_sportive(cylindree: int) -> bool:
        """Détermine si la moto est sportive selon la cylindrée."""
        return cylindree >= 600
