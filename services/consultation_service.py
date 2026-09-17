import json
from pathlib import Path

from models.consultation import Consultation


class ConsultationService:
    def __init__(self, data_file="data/cabinet_data.json"):
        self.data_file = Path(__file__).resolve().parent.parent / data_file
        self.consultations = self._load_consultations()

    def _load_consultations(self):
        if not self.data_file.exists():
            return {}

        with self.data_file.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return {
            consultation["consultation_id"]: Consultation(**consultation)
            for consultation in data.get("consultations", [])
        }

    def _save_consultations(self):
        self.data_file.parent.mkdir(parents=True, exist_ok=True)

        existing_data = {}
        if self.data_file.exists():
            with self.data_file.open("r", encoding="utf-8") as file:
                existing_data = json.load(file)

        existing_data["consultations"] = [
            consultation.to_dict() for consultation in self.consultations.values()
        ]

        with self.data_file.open("w", encoding="utf-8") as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=2)

    def add_consultation(self, patient_id, doctor_name, date, diagnosis, notes=""):
        consultation_id = f"C{len(self.consultations) + 1:03d}"
        consultation = Consultation(
            consultation_id=consultation_id,
            patient_id=patient_id,
            doctor_name=doctor_name,
            date=date,
            diagnosis=diagnosis,
            notes=notes,
        )
        self.consultations[consultation_id] = consultation
        self._save_consultations()
        return consultation

    def get_consultations_by_patient(self, patient_id):
        return [
            consultation
            for consultation in self.consultations.values()
            if consultation.patient_id == patient_id
        ]
