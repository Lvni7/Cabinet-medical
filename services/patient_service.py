from utils.exceptions import PatientNotFoundError
from utils.exceptions import DuplicatePatientError
from utils.decorators import validate_patient
from utils.decorators import log_action

patients = []


@log_action
def add_patient(patient):
    """
    Ajoute un patient après avoir vérifié son unicité.

    Args:
        patient (Patient): Patient à enregistrer.

    Raises:
        DuplicatePatientError: Si le numéro existe déjà.
    """

    for existing_patient in patients:

        if existing_patient.social_security_number == patient.social_security_number:
            raise DuplicatePatientError("Patient déjà existant")
        
    patients.append(patient)


def find_patient(social_security_number):
    """
    Recherche un patient par son numéro de sécurité sociale.

    Args:
        social_security_number (str): Numéro du patient recherché.

    Returns:
        Patient: Patient correspondant au numéro.

    Raises:
        PatientNotFoundError: Si aucun patient ne correspond.
    """
    for patient in patients:
        if patient.social_security_number == social_security_number:
            return patient

    raise PatientNotFoundError("Patient introuvable")



def list_all_patients():
    """Retourne la liste des patients enregistrés."""
    return patients


@validate_patient
def get_patient_history(social_security_number):
    """
    Retourne l'historique des consultations d'un patient existant.

    Args:
        social_security_number (str): Numéro du patient recherché.

    Returns:
        list: Consultations du patient.
    """
    patient = find_patient(social_security_number)
    return patient.consultations