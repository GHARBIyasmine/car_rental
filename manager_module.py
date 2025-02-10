from voiture_module import Voiture, ajouter_voiture, supprimer_voiture, rechercher_voiture, modifier_voiture, verifier_statut_voiture
from locataire_module import Locataire, ajouter_locataire, supprimer_locataire, rechercher_locataire_par_id, \
    modifier_locataire, sort_list_locataire, rechercher_locataire_par_nom


class LocationManager:
    def __init__(self):
        self.liste_voitures = []
        self.liste_locataires = []

    # 🚗 Manage Voitures
    def ajouter_voiture(self, num_imma, marque, modele, kilometrage, prix_location):
        """Ajoute une nouvelle voiture."""
        ajouter_voiture(self.liste_voitures, num_imma, marque, modele, kilometrage, prix_location)
        return "✅ Voiture ajoutée."

    def supprimer_voiture(self, num_imma):
        """Supprime une voiture par numéro d'immatriculation."""

        if supprimer_voiture(self.liste_voitures, num_imma):
            return "✅ Voiture supprimée."
        return "❌ Voiture introuvable."

    def modifier_voiture(self, num_imma, marque, model, kilometrage, prix):
        """Modifie une voiture via user input."""
        return modifier_voiture(self.liste_voitures, num_imma, marque, model, kilometrage, prix)

    def verifier_statut_voiture(self, num_imma):
        """Vérifie le statut actuel d'une voiture."""
        return verifier_statut_voiture(self.liste_voitures, num_imma)

    # 👥 Manage Locataires
    def ajouter_locataire(self, id_loc, nom, prenom, adresse):
        """Ajoute un locataire."""
        ajouter_locataire(self.liste_locataires, id_loc, nom, prenom, adresse)
        return "✅ Locataire ajouté."

    def supprimer_locataire(self, id_loc):
        """Supprime un locataire."""
        if supprimer_locataire(self.liste_locataires, id_loc):
            return "✅ Locataire supprimé."
        return "❌ Locataire introuvable."

    def modifier_locataire(self, id_loc, nom, prenom, adresse):
        """Modifie un locataire."""
        return modifier_locataire(self.liste_locataires, id_loc, nom, prenom, adresse)

    def recherche_locataire_par_id(self, id):
        """Recherche par id """
        return rechercher_locataire_par_id(self.liste_locataires,id)

    def rechercher_locataire_par_nom(self, nom):
        """Recherche par nom"""
        return rechercher_locataire_par_nom(self.liste_locataires, nom)


    def louer_voiture(self, num_imma: int, id_loc: int) -> str:
        """Assigne une voiture à un locataire si disponible."""
        voiture = rechercher_voiture(self.liste_voitures, num_imma)
        locataire = rechercher_locataire_par_id(self.liste_locataires, id_loc)

        if not voiture:
            return "❌ Voiture introuvable."
        if not locataire:
            return "❌ Locataire introuvable."
        if voiture.status != "Disponible":
            return "❌ Voiture déjà louée."

        voiture.status = "Loué"
        voiture.current_owner = id_loc
        locataire.voitures.append(voiture)
        return f"✅ {voiture.marque} {voiture.modele} louée à {locataire.nom} {locataire.prenom}."

    def rendre_voiture(self, num_imma: int, id_loc) -> str:
        """Libère une voiture et met à jour le locataire."""
        voiture = rechercher_voiture(self.liste_voitures, num_imma)
        if not voiture:
            return "❌ Voiture introuvable."
        if voiture.status == "Disponible":
            return "❌ La voiture est déjà disponible."

        if voiture.current_owner != id_loc:
            return "❌ Vous n'étes pas le locataire de cette voiture"


        locataire = rechercher_locataire_par_id(self.liste_locataires, voiture.current_owner)
        if locataire:
            locataire.voitures.remove(voiture)

        voiture.status = "Disponible"
        voiture.current_owner = None
        return f"✅ {voiture.marque} {voiture.modele} est maintenant disponible."

    def afficher_parc_voitures(self):
        """Affiche l'état de toutes les voitures."""

        print("\n🚗 État du parc automobile:")

        if len(self.liste_voitures) == 0:
            return None
            # print(f"❌ il n'y a pas encore de voitures enregistrées. \n",
            #         f"⭐ Enregistrez votre première voiture pour commencer! ")

        else :
            kilometrage_total = 0
            for voiture in self.liste_voitures:
                kilometrage_total += voiture.kilometrage

            print(" Nombre total de voiture est {} \n Kilometrage moyen est de {} "
                  .format(len(self.liste_voitures), kilometrage_total / len(self.liste_voitures)))

            return {
                "nbr_voiture": len(self.liste_voitures),
                "kilometrage_moyen": kilometrage_total / len(self.liste_voitures)
            }



    def afficher_locataires(self):
        """Affiche les locataires triés par nom."""

        if len(self.liste_locataires) == 0:
            print("❌ Aucun locataire pour le moment")
            return None

        else:
            sorted_locataires = sort_list_locataire(self.liste_locataires)
            print("\n👥 Liste des locataires par ordre alphabetique:")
            return sorted_locataires