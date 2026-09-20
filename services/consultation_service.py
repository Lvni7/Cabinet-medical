from datetime import datetime

from models.consultation import Consultation
from utils.decorators import log_action
from utils.exceptions import ConsultationNotFoundError


class ConsultationService:

    def __init__(self):
        """Initialise la liste des consultations et le prochain numéro."""
        self.__consultations = []
        self.__next_consultation_number = 1

    @log_action
    def add_consultation(self, consultation):
        """Ajoute une consultation et met à jour le prochain numéro disponible."""
        self.__consultations.append(consultation)
        if consultation.consultation_number >= self.__next_consultation_number:
            self.__next_consultation_number = consultation.consultation_number + 1

    def get_consultations(self, patient):
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
        consultation = Consultation(
            self.__next_consultation_number,
            appointment_datetime,
            patient,
            doctor,
            reason,
        )
        self.__next_consultation_number += 1
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

    def find_consultation(self, consultation_number):
        """
        Recherche une consultation par sa position dans la liste du service.

        Args:
            consultation_number (int): Numéro de la consultation recherchée.

        Returns:
            Consultation: Consultation trouvée.

        Raises:
            ConsultationNotFoundError: Si la position est invalide.
        """
        for consultation in self.__consultations:
            if consultation.consultation_number == consultation_number:
                return consultation
        raise ConsultationNotFoundError("Consultation introuvable")

    def list_all_consultations(self):
        """Retourne toutes les consultations enregistrées."""
        return self.__consultations

    @log_action
    def mark_consultation_as_completed(self, consultation_number):
        """Marque une consultation identifiée comme réalisée."""
        consultation = self.find_consultation(consultation_number)
        consultation.mark_as_completed()

    @log_action
    def cancel_consultation(self, consultation_number):
        """Annule une consultation identifiée."""
        consultation = self.find_consultation(consultation_number)
        consultation.cancel()

    @log_action
    def add_diagnosis(self, consultation_number, diagnosis):
        """Ajoute un diagnostic à une consultation identifiée."""
        consultation = self.find_consultation(consultation_number)
        consultation.add_diagnosis(diagnosis)

    @log_action
    def add_prescription(self, consultation_number, prescription):
        """Ajoute une prescription à une consultation identifiée."""
        consultation = self.find_consultation(consultation_number)
        consultation.add_prescription(prescription)
    