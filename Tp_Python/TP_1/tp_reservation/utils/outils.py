import random
import time
from functools import wraps

# Portée globale pour l'exemple LEGB
compteur_global = 1000

def generer_id(prefix: str) -> str:
    """Génère un identifiant unique (Exemple: VEH-1032)."""
    global compteur_global
    suffix = random.randint(100, 999) # Utilisation de random
    compteur_global += 1
    return f"{prefix}-{suffix}{compteur_global}"

def afficher_titre(titre: str, /, *, style="=", longueur=40):
    """
    Affiche un titre formaté.
    'titre' est positionnel-only.
    'style' et 'longueur' sont keyword-only.
    """
    print(style * longueur)
    print(titre.center(longueur))
    print(style * longueur)

def debug(*args, **kwargs):
    """Fonction de debug montrant les args positionnels et nommés."""
    print("[DEBUG] Arguments positionnels:", args)
    print("[DEBUG] Arguments nommés:", kwargs)

def mesure_temps(func):
    """Décorateur mesurant le temps d'exécution d'une fonction."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        debut = time.time()
        result = func(*args, **kwargs)
        fin = time.time()
        print(f"[Temps d'exécution] {func.__name__} : {fin - debut:.4f} sec")
        return result
    return wrapper

def demonstration_legb():
    """Démonstration de la règle de résolution de portée LEGB."""
    var_globale = "Je suis globale (G)"
    
    def enclosing_function():
        var_enclosing = "Je suis dans la fonction englobante (E)"
        
        def local_function():
            var_locale = "Je suis locale (L)"
            print("--- Demo LEGB ---")
            print(f"Local: {var_locale}")
            print(f"Enclosing: {var_enclosing}")
            print(f"Global: {var_globale}")
            # len() est une fonction Built-in (B)
            print(f"Built-in (len(var_locale)): {len(var_locale)}")
            
        local_function()
        
    enclosing_function()
