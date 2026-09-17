from utils.exceptions import PatientNotFoundError
from utils.exceptions import DuplicatePatientError

patients = []

def add_patient(patient):

    for p in patients:

        if p.social_security_number == patient.social_security_number:
            raise DuplicatePatientError("Patient déja existant")
        
    patients.append(patient)


def find_patient(social_security_number):
    for patient in patients:
        if patient.social_security_number == social_security_number:
            return patient

    raise PatientNotFoundError("Patient introuvable")



def list_all_patients():
    return patients


def get_patient_history(social_security_number):
    patient = find_patient(social_security_number)
    return patient.consultations