from dataclasses import dataclass, field

@dataclass
class Locataire:
    id_loc: int
    nom: str
    prenom: str
    adresse: str
    voitures: list = field(default_factory=list)  # Ensure a new list per instance

    def __str__(self):
        return f"{self.nom} {self.prenom} (ID: {self.id_loc}) - {self.adresse}"


def ajouter_locataire(list_locataire: list, id_loc: int, nom: str, prenom: str, adresse: str)  :
    """Ajoute un locataire à la liste."""
    locataire = Locataire(id_loc, nom, prenom, adresse)
    list_locataire.append(locataire)



def supprimer_locataire(list_locataire: list, id_loc: int) :
    """Supprime un locataire par son identifiant."""
    locataire = rechercher_locataire_par_id(list_locataire, id_loc)
    if locataire :
        list_locataire.remove(locataire)
        return True
    return False

def rechercher_locataire_par_nom(list_locataire: list, nom: str) :
    """Recherche un locataire par son nom."""
    for loc in list_locataire:
        if loc.nom.lower() == nom.lower():
            return loc
    return None  # retourne None si le locataire n'existe pas


def rechercher_locataire_par_id(list_locataire: list, id_loc: int) :
    """Recherche un locataire par son identifiant."""
    for loc in list_locataire:
        if loc.id_loc == id_loc:
            return loc
    return None


def sort_list_locataire(list_locataire: list) -> list:
    """Trie la liste des locataires par ordre alphabétique basé sur le nom."""
    for loc in list_locataire:
        print(loc.nom)
    return sorted(list_locataire, key=lambda loc: loc.nom.lower())


def modifier_locataire(
        liste_locataires: list,
        id_loc: int,
        nouveau_nom: str = "",
        nouveau_prenom: str = "",
        nouvelle_adresse: str = ""
) -> str:
    """Modifie les informations d'un locataire en conservant les valeurs actuelles si les nouveaux champs sont vides."""

    locataire = rechercher_locataire_par_id(liste_locataires, id_loc)
    if not locataire:
        return "❌ Locataire introuvable."

    # Keep old values if new values are empty
    locataire.nom = nouveau_nom or locataire.nom
    locataire.prenom = nouveau_prenom or locataire.prenom
    locataire.adresse = nouvelle_adresse or locataire.adresse

    return "✅ Locataire mis à jour avec succès."

