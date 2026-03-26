#utils/outils 
import random as rnd
import time

def generer_id(prefix: str) -> str:
    num = rnd.randint(1000, 9999)
    return f"{prefix}-{num}"

def afficher_titre(titre: str, /, *, style="=", longueur=40):
    espace_total = max(longueur - len(titre), 0)
    gauche = espace_total // 2
    droite = espace_total - gauche
    ligne = (style * gauche) + titre + (style * droite)
    print(ligne)

def debug(*args, **kwargs):
    print("Arguments positionnels (*args):")
    for i, arg in enumerate(args, start=1):
        print(f"  {i}: {arg}")
    print("\nArguments nommes (**kwargs):")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")

def mesure_temps(func):
    def wrapper(*args, **kwargs):
        debut = time.time()
        resultat = func(*args, **kwargs)
        fin = time.time()
        duree = fin - debut
        print(f"Temps d'execution de {func.__name__}: {duree:.5f} secondes")
        return resultat
    return wrapper

@mesure_temps
def calcul():
    return sum(range(1_000_000))

x = "global"
def externe():
    x = "enclosing"
    def interne():
        x = "local"
        print("Local:", x)
    def interne2():
        print("Enclosing:", x)
    interne()
    interne2()

def test_global():
    print("Global:", x)

def test_builtin():
    print("Built-in len:", len([1, 2, 3]))

