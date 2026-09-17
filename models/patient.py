from datetime import date, datetime
from utils.exceptions import InvalidSecurityNumberError
from utils.validators import verify_ssn


class Patient:
    def __init__(self, social_security_number, last_name, first_name, birth_date, address, phone_number):

        self._social_security_number = verify_ssn(social_security_number)
        self._last_name = last_name
        self._first_name = first_name
        self._birth_date = datetime.strptime(birth_date, "%d-%m-%Y").date()
        self._address = address
        self._phone_number = phone_number
        self._consultations = []

    @property
    def social_security_number(self):
        return self._social_security_number

    @property
    def last_name(self):
        return self._last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def birth_date(self):
        return self._birth_date

    @property
    def address(self):
        return self._address

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def consultations(self):
        return self._consultations

    @property
    def age(self):
        today = date.today()
        age = today.year - self._birth_date.year

        if (today.month, today.day) < (self._birth_date.month, self._birth_date.day):
            age -= 1

        return age

    def add_consultation(self, consultation):
        self._consultations.append(consultation)