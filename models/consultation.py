class Consultation:
    def __init__(self, appointment_datetime, patient, doctor, reason):
        self.__appointment_datetime = appointment_datetime
        self.__patient = patient
        self.__doctor = doctor
        self.__reason = reason
        self.__diagnosis = ""
        self.__prescriptions = []
        self.__status = "planifiée"

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
        if self.__status != "réalisée":
            raise ValueError("Le diagnostic ne peut être ajouté que pour une consultation réalisée.")
        self.__diagnosis = diagnosis

    def add_prescription(self, prescription):
        if self.__status == "annulée":
            raise ValueError("Impossible d'ajouter une prescription à une consultation annulée.")
        self.__prescriptions.append(prescription)

    def mark_as_completed(self):
        if self.__status == "annulée":
            raise ValueError("Une consultation annulée ne peut pas être réalisée.")
        elif self.__status == "réalisée":
            raise ValueError("La consultation est déjà marquée comme réalisée.")
        self.__status = "réalisée"

    def cancel(self):
        if self.__status == "réalisée":
            raise ValueError("Une consultation déjà réalisée ne peut pas être annulée.")
        self.__status = "annulée"