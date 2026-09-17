from datetime import date, datetime
from utils.validators import InvalidSecurityNumberError


class Patient:
    def __init__(self, social_security_number, last_name, first_name, birth_date, address, phone_number):
        self._validate_ssn(social_security_number)

        self._social_security_number = social_security_number
        self._last_name = last_name
        self._first_name = first_name
        self._birth_date = datetime.strptime(birth_date, "%d-%m-%Y").date()
        self._address = address
        self._phone_number = phone_number
        self._consultations = []

    def _validate_ssn(self, ssn):
        if len(ssn) != 15:
            raise InvalidSecurityNumberError("Le numéro de sécurité sociale doit contenir 15 chiffres")
        if not ssn.isdigit():
            raise InvalidSecurityNumberError("Le numéro de sécurité sociale ne doit contenir que des chiffres")

    @property
    def age(self):
        today = date.today()
        age = today.year - self._birth_date.year

        if (today.month, today.day) < (self._birth_date.month, self._birth_date.day):
            age -= 1

        return age

    def add_consultation(self, consultation):
        self._consultations.append(consultation)