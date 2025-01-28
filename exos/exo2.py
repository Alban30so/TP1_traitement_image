import numpy as np

def exercice2():
    # tableau 3x4 généré aléatoirement
    tab = np.random.randint(1, 32, (3, 4), dtype=int)
    print(f"Tableau 3x4 généré:\n{tab}")
    # somme des éléments pour chaque colonne du tableau
    sommeColonnes = np.sum(tab, axis=0)
    print(f"Somme colonne: {sommeColonnes}")
    # somme des éléments pour chaque ligne du tableau
    sommeLignes = np.sum(tab, axis=1)
    print(f"Somme ligne: {sommeLignes}")