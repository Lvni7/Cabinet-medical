from datetime import date, datetime
from utils.validators import verify_ssn


class Patient:
    """Représente un patient et l'historique de ses consultations."""

    def __init__(self, social_security_number, last_name, first_name, birth_date, address, phone_number):
        """Initialise les informations personnelles et un historique vide."""

        self._social_security_number = verify_ssn(social_security_number)
        self._last_name = last_name
        self._first_name = first_name
        self._birth_date = datetime.strptime(birth_date, "%d-%m-%Y").date()
        self._address = address
        self._phone_number = phone_number
        self._consultations = []

    @property
    def social_security_number(self):
        """Retourne le numéro de sécurité sociale du patient."""
        return self._social_security_number

    @property
    def last_name(self):
        """Retourne le nom du patient."""
        return self._last_name

    @property
    def first_name(self):
        """Retourne le prénom du patient."""
        return self._first_name

    @property
    def birth_date(self):
        """Retourne la date de naissance du patient."""
        return self._birth_date

    @property
    def address(self):
        """Retourne l'adresse du patient."""
        return self._address

    @property
    def phone_number(self):
        """Retourne le numéro de téléphone du patient."""
        return self._phone_number

    @property
    def consultations(self):
        """Retourne la liste des consultations du patient."""
        return self._consultations

    @property
    def age(self):
        """Calcule l'âge du patient à partir de la date du jour."""
        today = date.today()
        age = today.year - self._birth_date.year

        if (today.month, today.day) < (self._birth_date.month, self._birth_date.day):
            age -= 1

        return age

    def add_consultation(self, consultation):
        """Ajoute une consultation à l'historique du patient."""
        self._consultations.append(consultation)