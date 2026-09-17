from models.patient import Patient
from services.patient_service import PatientService
from services.consultation_service import ConsultationService


if __name__ == "__main__":
    patient_service = PatientService()
    consultation_service = ConsultationService()

    patient = Patient(
        patient_id="P001",
        first_name="Alice",
        last_name="Martin",
        birth_date="1990-05-14",
        phone="0123456789",
        email="alice.martin@email.com",
        allergies=["Pénicilline"],
    )

    patient_service.add_patient(patient)
    print(patient_service.get_patient_by_id("P001"))

    consultation = consultation_service.add_consultation(
        patient_id="P001",
        doctor_name="Dr. Dumas",
        date="2026-09-17",
        diagnosis="Grippe",
        notes="Patient se sent fatigué et fiévreux.",
    )

    print(consultation)
