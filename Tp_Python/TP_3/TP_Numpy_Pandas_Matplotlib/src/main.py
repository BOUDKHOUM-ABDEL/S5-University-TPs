import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class AnalyseVentes:
    """Classe pour l'analyse des ventes mensuelles (Génération, Nettoyage, Analyse, Visualisation)."""
    
    def __init__(self, base_dir="."):
        self.base_dir = base_dir
        self.data_dir = os.path.join(self.base_dir, "data")
        self.figures_dir = os.path.join(self.base_dir, "figures")
        self.csv_path = os.path.join(self.data_dir, "ventes.csv")
        self.df = None
        
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.figures_dir, exist_ok=True)
        
    def generer_donnees(self, n_ventes=1000):
        """Génère des données de ventes synthétiques avec NumPy et les sauvegarde en CSV."""
        print("--- Génération des données NumPy ---")
        try:
            product_id = np.random.randint(1, 21, n_ventes)
            quantity = np.random.randint(1, 11, n_ventes)
            unit_price = np.random.uniform(10.0, 500.0, n_ventes).round(2)
            month = np.random.randint(1, 13, n_ventes)
            year = np.random.randint(2021, 2025, n_ventes)
            
            data = np.column_stack((product_id, quantity, unit_price, month, year))
            
            np.savetxt(self.csv_path, data, fmt="%d,%d,%.2f,%d,%d", 
                       header="product_id,quantity,unit_price,month,year", comments="")
            print(f"[{n_ventes}] ventes générées dans {self.csv_path}")
        except Exception as e:
            print(f"Erreur lors de la génération des données : {e}")

    def charger_et_nettoyer(self):
        """Charge avec Pandas, affiche stats, gère NaNs, et effectue le nettoyage basique."""
        print("\n--- Chargement et nettoyage Pandas ---")
        try:
            self.df = pd.read_csv(self.csv_path)
            print("Aperçu (head):")
            print(self.df.head())
            print("\nTypes:")
            print(self.df.dtypes)
            print("\nStats:")
            print(self.df.describe())
            
            self.df["total_vente"] = self.df["quantity"] * self.df["unit_price"]
            
            # Injection aléatoire de NaNs
            indices_nan = self.df.sample(frac=0.05).index
            self.df.loc[indices_nan, "unit_price"] = np.nan
            
            # Remplacement des valeurs manquantes par la moyenne
            moyenne_prix = self.df["unit_price"].mean()
            self.df.fillna({"unit_price": moyenne_prix}, inplace=True)
            self.df["total_vente"] = self.df["quantity"] * self.df["unit_price"]
            
            print(f"\nValeurs NaN après nettoyage : {self.df.isna().sum().sum()}")
            
        except Exception as e:
            print(f"Erreur lors du nettoyage : {e}")

    def analyser(self):
        """Filtre, agrège, et analyse les données (évolution, produit max, outliers)."""
        print("\n--- Analyse ---")
        if self.df is None: return

        try:
            ca_par_produit = self.df.groupby("product_id")["total_vente"].sum()
            produit_rentable = ca_par_produit.idxmax()
            print(f"Produit le plus rentable : {produit_rentable} (CA: {ca_par_produit.max():.2f})")
            
            mois_fort = self.df.groupby("month")["total_vente"].sum().idxmax()
            print(f"Mois le plus fort en CA : {mois_fort}")
            
            ca_annuel = self.df.groupby("year")["total_vente"].sum()
            evolution = ca_annuel.pct_change() * 100
            print("Evolution annuelle CA (%) :\n", evolution.dropna().round(2))
            
            min_vente, max_vente = self.df["total_vente"].min(), self.df["total_vente"].max()
            self.df["total_vente_norm"] = (self.df["total_vente"] - min_vente) / (max_vente - min_vente)
            
            moyenne, ecart_type = self.df["total_vente"].mean(), self.df["total_vente"].std()
            atypiques = self.df[self.df["total_vente"] > (moyenne + 2 * ecart_type)]
            print(f"Ventes atypiques détectées (> moyenne + 2std) : {len(atypiques)}")
            
        except Exception as e:
            print(f"Erreur d'analyse : {e}")

    def visualiser(self):
        """Produit 5 types de viz Matplotlib sauvegardées en .png."""
        print("\n--- Visualisation Matplotlib ---")
        if self.df is None: return
            
        try:
            ca_annuel = self.df.groupby("year")["total_vente"].sum()
            plt.figure(figsize=(8,5))
            ca_annuel.plot(kind="bar", color="skyblue")
            plt.title("Chiffre d'Affaires par Année")
            plt.xlabel("Année"); plt.ylabel("CA")
            plt.tight_layout(); plt.savefig(os.path.join(self.figures_dir, "ca_par_annee.png")); plt.close()
            
            ca_mensuel = self.df.groupby(["year", "month"])["total_vente"].sum()
            plt.figure(figsize=(10,5))
            ca_mensuel.plot(kind="line", marker="o", color="orange")
            plt.title("Evolution Mensuelle du CA")
            plt.tight_layout(); plt.savefig(os.path.join(self.figures_dir, "evolution_mensuelle.png")); plt.close()
            
            ca_par_produit = self.df.groupby("product_id")["total_vente"].sum().nlargest(5)
            plt.figure(figsize=(6,6))
            ca_par_produit.plot(kind="pie", autopct="%1.1f%%", cmap="Set3")
            plt.title("Top 5 Produits")
            plt.ylabel("")
            plt.tight_layout(); plt.savefig(os.path.join(self.figures_dir, "repartition_produits.png")); plt.close()
            
            plt.figure(figsize=(8,5))
            plt.hist(self.df["total_vente"], bins=30, color="purple", edgecolor="black")
            plt.title("Histogramme des Ventes")
            plt.tight_layout(); plt.savefig(os.path.join(self.figures_dir, "histogramme_ventes.png")); plt.close()
            
            plt.figure(figsize=(8,5))
            plt.scatter(self.df["quantity"], self.df["unit_price"], alpha=0.5, color="green")
            plt.title("Quantité vs Prix Unitaire")
            plt.xlabel("Quantité"); plt.ylabel("Prix Unitaire")
            plt.tight_layout(); plt.savefig(os.path.join(self.figures_dir, "scatter_qty_price.png")); plt.close()
            
            print(f"5 visualisations sauvegardées dans '{self.figures_dir}'.")
        except Exception as e:
            print(f"Erreur viz : {e}")


if __name__ == "__main__":
    base_proj_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app = AnalyseVentes(base_dir=base_proj_dir)
    app.generer_donnees(1000)
    app.charger_et_nettoyer()
    app.analyser()
    app.visualiser()
