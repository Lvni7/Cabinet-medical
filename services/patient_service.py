import json
from pathlib import Path

from models.patient import Patient


class PatientService:
    def __init__(self, data_file="data/cabinet_data.json"):
        self.data_file = Path(__file__).resolve().parent.parent / data_file
        self.patients = self._load_patients()

    def _load_patients(self):
        if not self.data_file.exists():
            return {}

        with self.data_file.open("r", encoding="utf-8") as file:
            data = json.load(file)

        return {
            patient["patient_id"]: Patient(**patient)
            for patient in data.get("patients", [])
        }

    def _save_patients(self):
        self.data_file.parent.mkdir(parents=True, exist_ok=True)

        payload = {
            "patients": [patient.to_dict() for patient in self.patients.values()]
        }

        with self.data_file.open("w", encoding="utf-8") as file:
            json.dump(payload, file, ensure_ascii=False, indent=2)

    def add_patient(self, patient):
        self.patients[patient.patient_id] = patient
        self._save_patients()
        return patient

    def get_patient_by_id(self, patient_id):
        return self.patients.get(patient_id)

    def get_all_patients(self):
        return list(self.patients.values())
