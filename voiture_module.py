from dataclasses import dataclass

@dataclass
class Voiture:
    num_imma: int
    marque: str
    modele: str
    kilometrage: int
    prix_location: float
    status: str = "Disponible"
    current_owner: int = None

    def __str__(self):
        return f" Voiture {self.marque} {self.modele} ({self.num_imma}) - {self.status}"


def ajouter_voiture(liste_voitures: list, num_imma, marque, modele, kilometrage, prix_location):
    """Ajoute une voiture à la liste."""
    voiture = Voiture(num_imma, marque, modele, kilometrage, prix_location)
    liste_voitures.append(voiture)



def supprimer_voiture(liste_voitures: list, num_imma: int) -> bool:
    """Supprime une voiture par son numéro d'immatriculation et retourne True si supprimée."""
    voiture = rechercher_voiture(liste_voitures, num_imma)

    if voiture:
        liste_voitures.remove(voiture)
        return True  # ✅ Correctly return True only after deletion

    return False  # Return False if no voiture was found


def rechercher_voiture(liste_voitures:list, num_imma: int):
    """Recherche """
    for voiture in liste_voitures:
        if voiture.num_imma == num_imma:
            return voiture
    return None


def modifier_voiture(
    liste_voitures: list,
    num_imma: int,
    nouvelle_marque: str = "",
    nouveau_modele: str = "",
    nouveau_km: str = "",
    nouveau_prix: str = ""
) -> str:
    """Modifie les informations d'une voiture en conservant les valeurs actuelles si les nouveaux champs sont vides."""

    voiture = rechercher_voiture(liste_voitures, num_imma)
    if not voiture:
        return "❌ Voiture introuvable."

    # Keep old values if new values are empty
    voiture.marque = nouvelle_marque or voiture.marque
    voiture.modele = nouveau_modele or voiture.modele

    # Ensure numeric values remain valid
    if nouveau_km.isdigit():
        voiture.kilometrage = int(nouveau_km)

    if nouveau_prix.replace('.', '', 1).isdigit():
        voiture.prix_location = float(nouveau_prix)

    return "✅ Voiture mise à jour avec succès."



def verifier_statut_voiture(liste_voitures: list, num_imma: int) -> str:
    """Affiche le statut actuel d'une voiture."""
    voiture = rechercher_voiture(liste_voitures, num_imma)
    if not voiture:
        return "❌ Voiture introuvable."
    return f"🚗 Statut de la voiture {voiture.marque} {voiture.modele} ({voiture.num_imma}): {voiture.status}"

