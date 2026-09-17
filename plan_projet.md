# Plan de répartition du projet Cabinet médical

## 1. Répartition entre toi et ton collègue

### Partie A — Ce que tu peux faire

#### 1. Modèles / entités

Tu prends les fichiers suivants :

- `models/patient.py`
- `models/consultation.py`
- `models/prescription.py`

Tu dois définir :

- la classe `Patient`

  - attributs privés
  - validation du numéro de sécurité sociale
  - calcul de l’âge
  - historique des consultations
  - méthodes utiles comme `ajouter_consultation()`
- la classe `Consultation`

  - date et heure
  - patient concerné
  - médecin
  - motif
  - diagnostic
  - prescriptions
  - statut
  - règles métier :
    - impossible de modifier si le statut est annulé ou clôturé
    - le diagnostic ne peut être ajouté que si la consultation est réalisée
- la hiérarchie des prescriptions

  - classe abstraite `Prescription`
  - classes dérivées :
    - `PrescriptionMedicamenteuse`
    - `PrescriptionExamen`
    - `PrescriptionKinesitherapie`
  - chaque classe doit implémenter `afficher_details()`

➡️ Ces fichiers servent à modéliser le domaine métier du cabinet médical.

#### 2. Validation et décorateurs

Tu peux aussi t’occuper de :

- `utils/validators.py`
- `utils/decorators.py`

Tu dois implémenter :

- validation du numéro de sécurité sociale
- décorateur `@log_action`
  - écrit dans `logs.txt`
  - format :
    - `[Date/Heure]`
    - `Action effectuée : description`
- décorateur `@validate_patient`
  - vérifie si un patient existe
  - lève `PatientNotFoundError` sinon

➡️ Ces fichiers ne doivent pas contenir la logique métier du cabinet, mais les règles transverses : sécurité, logs, validations.

---

### Partie B — Ce que ton collègue peut faire

#### 3. Services métier

Ton collègue prend :

- `services/patient_service.py`
- `services/consultation_service.py`

Ces fichiers doivent gérer les opérations suivantes :

- ajouter un patient
- rechercher un patient par numéro de sécurité sociale
- afficher tous les patients
- afficher l’historique d’un patient
- planifier une consultation
- afficher les consultations à venir
- marquer une consultation comme réalisée
- annuler une consultation
- ajouter un diagnostic
- ajouter une ou plusieurs prescriptions

➡️ Ce sont les services : ils orchestrent les objets métier et appliquent les règles.

#### 4. Persistance et données

Le fichier important est :

- `data/cabinet_data.json`

Il contient la structure JSON du système :

- liste des patients
- liste des consultations
- historique complet

Il est utilisé pour :

- charger les données au démarrage
- sauvegarder automatiquement après chaque modification

➡️ Ce fichier n’est pas la logique du projet ; c’est le stockage des données.

---

## 2. Point d’entrée de l’application

Le fichier :

- `main.py`

doit contenir :

- lancement du programme
- menu console
- appel aux services
- gestion des exceptions
- chargement des données au démarrage
- sauvegarde auto ou finale

➡️ C’est le menu principal de l’application, pas la logique métier.

---

## 3. Logique que doit contenir chaque fichier

### `models/patient.py`

Contient :

- classe `Patient`
- attributs privés
- validation du NSS
- calcul de l’âge
- méthode pour ajouter une consultation
- getters/setters si nécessaires

### `models/consultation.py`

Contient :

- classe `Consultation`
- attributs pour la date, le patient, le médecin, le motif, le diagnostic, les prescriptions et le statut
- gestion des états de consultation
- vérification avant modification
- ajout de diagnostic seulement si la consultation est réalisée

### `models/prescription.py`

Contient :

- classe abstraite `Prescription`
- méthode abstraite `afficher_details()`
- sous-classes dérivées :
  - `PrescriptionMedicamenteuse`
  - `PrescriptionExamen`
  - `PrescriptionKinesitherapie`
- implémentation spécifique de l’affichage pour chaque type

### `utils/validators.py`

Contient :

- fonctions de validation
- contrôle du format du numéro de sécurité sociale
- contrôle des données saisies
- éventuelles vérifications de dates ou de contraintes

### `utils/decorators.py`

Contient :

- `@log_action`
- `@validate_patient`
- gestion de l’écriture dans un fichier `logs.txt`

### `services/patient_service.py`

Contient :

- ajout d’un patient
- recherche par NSS
- liste de tous les patients
- historique complet d’un patient

### `services/consultation_service.py`

Contient :

- planification d’une consultation
- affichage des consultations à venir
- validation d’un statut
- annulation
- ajout de diagnostic
- ajout de prescriptions

### `main.py`

Contient :

- le menu utilisateur
- les interactions avec la console
- appels aux services
- gestion des erreurs
- démarrage de l’application

---

## 4. Idée de répartition pratique

### gabriel

- modèles
- validations
- exceptions
- décorateurs

## Leni

- services
- menu principal
- gestion JSON
- orchestration de l’application

---

## 5. Règle de séparation importante

La logique clé est la suivante :

- les modèles représentent les objets du métier
- les services traitent les opérations
- les utils contiennent les contrôles transverses
- le `main.py` pilote l’application

C’est cette séparation qui rend le projet propre, lisible et maintenable.
