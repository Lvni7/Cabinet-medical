class Prescription:
    def __init__(
        self,
        prescription_id,
        consultation_id,
        medicine,
        dosage,
        duration_days,
        instructions="",
    ):
        self.prescription_id = prescription_id
        self.consultation_id = consultation_id
        self.medicine = medicine
        self.dosage = dosage
        self.duration_days = duration_days
        self.instructions = instructions

    def __str__(self):
        return (
            f"Prescription(id={self.prescription_id}, medicament={self.medicine}, "
            f"dosage={self.dosage}, durée={self.duration_days} jours)"
        )

    def to_dict(self):
        return {
            "prescription_id": self.prescription_id,
            "consultation_id": self.consultation_id,
            "medicine": self.medicine,
            "dosage": self.dosage,
            "duration_days": self.duration_days,
            "instructions": self.instructions,
        }
