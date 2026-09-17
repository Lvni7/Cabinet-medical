<<<<<<< HEAD
﻿
=======
﻿from models.consultation import Consultation
class ConsultationService:
    def __init__(self):
        self.__consultations = []

    def add_consultation(self, consultation):
        self.__consultations.append(consultation)

    def get_consultations(self, patient):
        return [consultation for consultation in self.__consultations if consultation.patient == patient]

    def create_consultation(appointment_datetime, patient, doctor, diagnosis, prescriptions, status):
        """
        Planifie une consultation en créant une instance de la classe Consultation.

        Args:
            appointment_datetime (datetime): La date et l'heure de la consultation.
            patient (Patient): L'objet représentant le patient.
            doctor (str): Le nom du médecin.
            diagnosis (str): Le diagnostic de la consultation.
            prescriptions (list): La liste des prescriptions associées à la consultation.
            status (str): Le statut de la consultation.

        Returns:
            Consultation: Une instance de la classe Consultation représentant la consultation planifiée.
        """
        return Consultation(appointment_datetime, patient, doctor, diagnosis, prescriptions, status)

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
    