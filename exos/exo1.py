

# Calcul les prix soldés d'un vêtement,
def prixVetementSolde(prix):
    solde20 = prix * 0.8 # prix à -20%
    solde40 = prix * 0.6 # prix à -40%
    solde50 = prix * 0.5 # prix à -50%
    return solde20, solde40, solde50


def exercice1():
    prixVetement = 200
    prixSolde20, prixSolde40, prixSolde50 = prixVetementSolde(prixVetement)
    #Affichage des prix en fonction des soldes appliquées.
    print(f"Prix du vêtement: {prixVetement}\n"
        f"Avec -20%: {prixSolde20}\n"
        f"Avec -40%: {prixSolde40}\n"
        f"Avec -50%: {prixSolde50}")