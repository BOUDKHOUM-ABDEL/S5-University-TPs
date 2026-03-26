# models/vehicule.py
from utils.outils import generer_id  as gen_id 

class Vehicule:
    
    def __init__(self, marque, modele, prix_location):
        self._marque = marque
        self._modele = modele
        self._prix_location = prix_location
        self.id = gen_id(marque)

    @property
    def marque(self) -> str:
        return self._marque

    @marque.setter
    def marque(self, valeur: str):
        self._marque = valeur

    
    @property
    def modele(self) -> str:
        return self._modele

    @modele.setter
    def modele(self, valeur: str):
        self._modele = valeur

   
    @property
    def prix_location(self) -> float:
        return self._prix_location

    @prix_location.setter
    def prix_location(self, valeur: float):
        self._prix_location = valeur

    
    def afficher_infos(self):
        return f"[{self.id}] {self.marque} {self.modele} - {self.prix_location} €/jour"

    @classmethod
    def from_string(cls, data: str):
          marque, modele, prix = data.split(";")
          return cls(marque, modele, float(prix))

    def afficher_details(self):
        print("****** Details du vehicule *****")
        print(f"ID: {self.id}")
        print(f"Marque: {self.marque}")
        print(f"Modele: {self.modele}")
        print(f"Prix de location: {self.prix_location} DH/jour")

    
    @staticmethod
    def est_vehicule_valide(marque: str) -> bool:
        return bool(marque and marque.strip())

    
    def type_vehicule(self) -> str:
        return "is Vihicule X"
      

