class Consultation:
    def __init__(
        self,
        consultation_id,
        patient_id,
        doctor_name,
        date,
        diagnosis,
        notes="",
    ):
        self.consultation_id = consultation_id
        self.patient_id = patient_id
        self.doctor_name = doctor_name
        self.date = date
        self.diagnosis = diagnosis
        self.notes = notes

    def __str__(self):
        return (
            f"Consultation(id={self.consultation_id}, patient_id={self.patient_id}, "
            f"docteur={self.doctor_name}, diagnostic={self.diagnosis})"
        )

    def to_dict(self):
        return {
            "consultation_id": self.consultation_id,
            "patient_id": self.patient_id,
            "doctor_name": self.doctor_name,
            "date": self.date,
            "diagnosis": self.diagnosis,
            "notes": self.notes,
        }
