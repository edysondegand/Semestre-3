from equipement import EquipementReseau


class GestionnaireParc:

    def __init__(self, nom_parc: str):
        self.nom_parc = nom_parc
        self.equipements = []

    def ajouter_equipement(self, equipement: EquipementReseau) -> None:
        if not isinstance(equipement, EquipementReseau):
            raise TypeError("L'objet ajouté doit être une instance de EquipementReseau.")
        self.equipements.append(equipement)

    def lister_equipements(self) -> None:
        print(f"--- Équipements du parc « {self.nom_parc} » ---")
        for eq in self.equipements:
            print(eq)

    def rechercher_par_hostname(self, hostname: str):
        for eq in self.equipements:
            if eq.hostname == hostname:
                return eq
        return None

    def statistiques(self) -> None:
        total = len(self.equipements)
        actifs = sum(1 for eq in self.equipements if eq.est_actif)
        inactifs = total - actifs
        print(f"Total: {total}, Actifs: {actifs}, Inactifs: {inactifs}")


# --- Tests à valider ---

# 1. Création des équipements
r1 = EquipementReseau(hostname="R1-Paris", ip_address="192.168.1.1")
s1 = EquipementReseau(hostname="S1-Lille", ip_address="192.168.1.10")
r2 = EquipementReseau(hostname="R2-Lyon", ip_address="10.0.0.1")

assert r1.id == 0 and s1.id == 1, "Les IDs doivent être uniques et séquentiels."
assert r1.statut == 'inactif', "Le statut initial doit être 'inactif'."

# 2. Activation et test de la propriété
r1.activer()
assert r1.est_actif is True, "La propriété est_actif doit refléter le statut."
print(r1)

# 3. Création du gestionnaire et ajout d'équipements
parc_nord = GestionnaireParc("Parc-Nord-France")
parc_nord.ajouter_equipement(r1)
parc_nord.ajouter_equipement(s1)

# 4. Lister et rechercher
print("\n--- Liste des équipements du parc ---")
parc_nord.lister_equipements()

print("\n--- Recherche de 'S1-Lille' ---")
equipement_trouve = parc_nord.rechercher_par_hostname("S1-Lille")
assert equipement_trouve is s1
print(f"Trouvé : {equipement_trouve}")

# 5. Statistiques
print("\n--- Statistiques du parc ---")
s1.activer()
parc_nord.statistiques()  # Affiche : Total: 2, Actifs: 2, Inactifs: 0

s1.desactiver()
print("\n--- Statistiques après désactivation ---")
parc_nord.statistiques()  # Affiche : Total: 2, Actifs: 1, Inactifs: 1

print("\nTests du mini-projet passés avec succès !")