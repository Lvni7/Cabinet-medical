Étape 0 — À faire ensemble (30 min, avant de vous séparer)
Définir les attributs exacts de Patient et Consultation (noms, types)
Définir les signatures des méthodes des services (ex: ajouter_patient(patient), planifier_consultation(...))
Définir le schéma JSON de cabinet_data.json
Créer les fichiers vides (squelettes avec pass) dans l'arborescence, pousser sur un repo Git commun

Une fois ça fait, vous pouvez coder chacun de votre côté sans vous marcher dessus.

Répartition proposée

Personne A — Côté "Patient"

models/patient.py : classe Patient (encapsulation, validation NSS 15 chiffres, calcul de l'âge)

services/patient_service.py : ajout, recherche, liste, historique

utils/validators.py : validation du NSS et autres champs patient
Exceptions : PatientNotFoundError, InvalidSecurityNumberError
Décorateur @validate_patient

Personne B — Côté "Consultation & Prescription"

models/consultation.py : classe Consultation (statuts, contraintes de modification)
models/prescription.py : classe abstraite Prescription + les 3 classes dérivées
services/consultation_service.py : planification, annulation, diagnostic, prescriptions
Exceptions : ConsultationNotFoundError, InvalidConsultationStatusError
Décorateur @log_action

À faire ensemble à la fin

main.py (le menu console qui appelle les deux services)
La persistance JSON (sauvegarde/chargement) — comme elle touche les deux modèles, c'est plus simple de la faire à deux ou de la confier à celui qui a le plus avancé
Pourquoi ce découpage
Chaque personne a une classe modèle + son service + ses exceptions + un décorateur → travail équilibré et testable indépendamment
Consultation dépend de Patient seulement par référence (pas par héritage), donc tant que l'attribut patient est défini dès le départ, vous n'êtes pas bloqués l'un par l'autre
Les Prescription sont autonomes, donc B peut les développer et les tester sans attendre A
Conseil pratique

Utilisez des branches Git (feature/patient, feature/consultation) et faites un merge à mi-parcours pour tester l'intégration avant la deadline de dimanche — ça évite les mauvaises surprises de dernière minute.

Voulez-vous que je vous prépare les squelettes de fichiers avec les signatures déjà posées, pour gagner du temps sur l'étape 0 ?