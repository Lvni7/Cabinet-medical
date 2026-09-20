from datetime import datetime

from models.consultation import Consultation
from utils.decorators import log_action
from utils.exceptions import ConsultationNotFoundError


class ConsultationService:
    """Gère les consultations enregistrées dans le cabinet."""

    def __init__(self):
        """Initialise une liste vide de consultations."""
        self.__consultations = []

    @log_action
    def add_consultation(self, consultation):
        """Enregistre une consultation dans le service."""
        self.__consultations.append(consultation)

    def get_consultations(self, patient):
        """Retourne les consultations associées à un patient."""
        return [consultation for consultation in self.__consultations if consultation.patient == patient]

    @log_action
    def create_consultation(self, appointment_datetime, patient, doctor, reason):
        """
        Planifie une consultation en créant une instance de la classe Consultation.

        Args:
            appointment_datetime (datetime): La date et l'heure de la consultation.
            patient (Patient): L'objet représentant le patient.
            doctor (str): Le nom du médecin.
            reason (str): Le motif de la consultation.

        Returns:
            Consultation: Une instance de la classe Consultation représentant la consultation planifiée.
        """
        consultation = Consultation(appointment_datetime, patient, doctor, reason)
        self.add_consultation(consultation)
        patient.add_consultation(consultation)
        return consultation

    def add_consultation_to_patient(self, patient, consultation):
        """
        Ajoute une consultation à la liste des consultations d'un patient.

        Args:
            patient (Patient): L'objet représentant le patient.
            consultation (Consultation): L'objet représentant la consultation à ajouter.
        """
        patient.add_consultation(consultation)

    def get_consultations_by_patient(self, patient):
        """
        Récupère toutes les consultations d'un patient donné.

        Args:
            patient (Patient): L'objet représentant le patient.

        Returns:
            list: Une liste contenant toutes les consultations du patient.
        """
        return self.get_consultations(patient)

    def get_upcoming_consultations(self):
        """Retourne les consultations planifiées à partir de maintenant."""
        current_datetime = datetime.now()
        return [
            consultation for consultation in self.__consultations
            if consultation.status == "planifiée"
            and consultation.appointment_datetime >= current_datetime
        ]

    def find_consultation(self, consultation_index):
        """
        Recherche une consultation par sa position dans la liste du service.

        Args:
            consultation_index (int): Position de la consultation recherchée.

        Returns:
            Consultation: Consultation trouvée.

        Raises:
            ConsultationNotFoundError: Si la position est invalide.
        """
        try:
            return self.__consultations[consultation_index]
        except IndexError:
            raise ConsultationNotFoundError("Consultation introuvable")

    def list_all_consultations(self):
        """Retourne toutes les consultations du service."""
        return self.__consultations

    @log_action
    def mark_consultation_as_completed(self, consultation_index):
        """Marque une consultation existante comme réalisée."""
        consultation = self.find_consultation(consultation_index)
        consultation.mark_as_completed()

    @log_action
    def cancel_consultation(self, consultation_index):
        """Annule une consultation existante."""
        consultation = self.find_consultation(consultation_index)
        consultation.cancel()

    @log_action
    def add_diagnosis(self, consultation_index, diagnosis):
        """Ajoute un diagnostic à une consultation réalisée."""
        consultation = self.find_consultation(consultation_index)
        consultation.add_diagnosis(diagnosis)

    @log_action
    def add_prescription(self, consultation_index, prescription):
        """Ajoute une prescription à une consultation non annulée."""
        consultation = self.find_consultation(consultation_index)
        consultation.add_prescription(prescription)
    