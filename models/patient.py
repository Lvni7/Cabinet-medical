class Patient:
    def __init__(
        self,
        patient_id,
        first_name,
        last_name,
        birth_date,
        phone,
        email,
        allergies=None,
    ):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.phone = phone
        self.email = email
        self.allergies = allergies or []

    def __str__(self):
        return (
            f"Patient(id={self.patient_id}, nom={self.last_name}, "
            f"prénom={self.first_name}, email={self.email})"
        )

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "phone": self.phone,
            "email": self.email,
            "allergies": self.allergies,
        }
