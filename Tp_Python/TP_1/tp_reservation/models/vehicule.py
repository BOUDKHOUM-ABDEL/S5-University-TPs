from utils.outils import generer_id

class Vehicule:
    """Classe abstraite représentant un véhicule."""
    
    def __init__(self, marque: str, modele: str, prix_location: float):
        self._marque = marque
        self._modele = modele
        self._prix_location = float(prix_location)
        self.id = generer_id("VEH")
        
    @property
    def marque(self):
        return self._marque
        
    @marque.setter
    def marque(self, valeur: str):
        self._marque = valeur
        
    @property
    def modele(self):
        return self._modele
        
    @modele.setter
    def modele(self, valeur: str):
        self._modele = valeur

    @property
    def prix_location(self):
        return self._prix_location
        
    @prix_location.setter
    def prix_location(self, valeur: float):
        if valeur >= 0:
            self._prix_location = valeur
        else:
            raise ValueError("Le prix de location doit être positif.")

    @classmethod
    def from_string(cls, chaine: str):
        """Constructeur secondaire via une chaîne formatée (ex: 'Toyota;Yaris;150')."""
        try:
            marque, modele, prix = chaine.split(";")
            return cls(marque, modele, float(prix))
        except ValueError:
            raise ValueError("Le format attendu est 'Marque;Modele;Prix'")
            
    def afficher_details(self):
        """Affiche les détails du véhicule."""
        print(f"[{self.id}] {self._marque} {self._modele} - {self._prix_location}€/jour")
        
    @staticmethod
    def est_vehicule_valide(marque: str) -> bool:
        """Méthode statique vérifiant la validité d'une marque."""
        marques_valides = ["Toyota", "Renault", "Peugeot", "BMW", "Audi", "Yamaha", "Suzuki", "Mercedes"]
        return marque.capitalize() in marques_valides

    def type_vehicule(self):
        """Méthode polymorphe à redéfinir dans les classes filles."""
        raise NotImplementedError("La méthode type_vehicule doit être surchargée par les classes enfants.")
