from models.consultation import Consultation
class ConsultationService:
    def __init__(self):
        self.__consultations = []

    def add_consultation(self, consultation):
        self.__consultations.append(consultation)

    def get_consultations(self):
        return self.__consultations
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