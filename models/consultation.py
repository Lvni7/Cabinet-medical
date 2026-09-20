from utils.exceptions import InvalidConsultationStatusError


class Consultation:
    """Représente un rendez-vous médical et son suivi."""

    def __init__(self, appointment_datetime, patient, doctor, reason,
                 diagnosis="", prescriptions=None, status="planifiée"):
        """Initialise une consultation planifiée par défaut."""
        self.__appointment_datetime = appointment_datetime
        self.__patient = patient
        self.__doctor = doctor
        self.__reason = reason
        self.__diagnosis = diagnosis
        self.__prescriptions = prescriptions if prescriptions is not None else []
        self.__status = status

    @property
    def appointment_datetime(self):
        return self.__appointment_datetime

    @property
    def patient(self):
        return self.__patient

    @property
    def doctor(self):
        return self.__doctor

    @property
    def reason(self):
        return self.__reason

    @property
    def diagnosis(self):
        return self.__diagnosis

    @property
    def prescriptions(self):
        return self.__prescriptions

    @property
    def status(self):
        return self.__status

    def add_diagnosis(self, diagnosis):
        """Ajoute un diagnostic uniquement après la réalisation du rendez-vous."""
        if self.__status != "réalisée":
            raise InvalidConsultationStatusError(
                "Le diagnostic ne peut être ajouté que pour une consultation réalisée."
            )
        self.__diagnosis = diagnosis

    def add_prescription(self, prescription):
        """Ajoute une prescription si la consultation n'est pas annulée."""
        if self.__status == "annulée":
            raise InvalidConsultationStatusError(
                "Impossible d'ajouter une prescription à une consultation annulée."
            )
        self.__prescriptions.append(prescription)

    def mark_as_completed(self):
        """Marque la consultation comme réalisée si elle peut encore évoluer."""
        if self.__status == "annulée":
            raise InvalidConsultationStatusError(
                "Une consultation annulée ne peut pas être réalisée."
            )
        elif self.__status == "réalisée":
            raise InvalidConsultationStatusError(
                "La consultation est déjà marquée comme réalisée."
            )
        self.__status = "réalisée"

    def cancel(self):
        """Annule une consultation qui n'a pas encore été réalisée."""
        if self.__status == "réalisée":
            raise InvalidConsultationStatusError(
                "Une consultation déjà réalisée ne peut pas être annulée."
            )
        self.__status = "annulée"