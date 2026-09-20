import json
import os
from datetime import datetime

from models.consultation import Consultation
from models.patient import Patient
from models.prescription import (
	PrescriptionExamen,
	PrescriptionKinesitherapie,
	PrescriptionMedicamenteuse,
)
from services import patient_service
from services.consultation_service import ConsultationService
from utils.exceptions import (
	ConsultationNotFoundError,
	DuplicatePatientError,
	InvalidConsultationStatusError,
	InvalidSecurityNumberError,
	PatientNotFoundError,
)
from utils.validators import verify_ssn


DATA_FILE = os.path.join("data", "cabinet_data.json")


def consultation_to_dictionary(consultation):
	"""
	Transforme une consultation en dictionnaire enregistrable en JSON.

	Args:
		consultation (Consultation): Consultation à transformer.

	Returns:
		dict: Données simples de la consultation.
	"""
	return {
		"appointment_datetime": consultation.appointment_datetime.strftime("%d-%m-%Y %H:%M"),
		"patient_social_security_number": consultation.patient.social_security_number,
		"doctor": consultation.doctor,
		"reason": consultation.reason,
		"diagnosis": consultation.diagnosis,
		"prescriptions": [
			prescription_to_dictionary(prescription)
			for prescription in consultation.prescriptions
		],
		"status": consultation.status,
	}


def prescription_to_dictionary(prescription):
	"""Transforme une prescription en dictionnaire JSON simple."""
	if isinstance(prescription, PrescriptionMedicamenteuse):
		return {
			"type": "medication",
			"treatment_name": prescription.treatment_name,
			"dosage": prescription.dosage,
			"duration": prescription.duration,
			"medication_name": prescription.medication_name,
			"frequency": prescription.frequency,
		}
	if isinstance(prescription, PrescriptionExamen):
		return {
			"type": "exam",
			"treatment_name": prescription.treatment_name,
			"dosage": prescription.dosage,
			"duration": prescription.duration,
			"exam_type": prescription.exam_type,
			"recommended_laboratory": prescription.recommended_laboratory,
		}
	return {
		"type": "physiotherapy",
		"treatment_name": prescription.treatment_name,
		"dosage": prescription.dosage,
		"duration": prescription.duration,
		"session_count": prescription.session_count,
		"area_to_treat": prescription.area_to_treat,
	}


def dictionary_to_prescription(prescription_data):
	"""Reconstruit une prescription à partir de ses données JSON."""
	common_data = (
		prescription_data["treatment_name"],
		prescription_data["dosage"],
		prescription_data["duration"],
	)
	if prescription_data["type"] == "medication":
		return PrescriptionMedicamenteuse(
			*common_data,
			prescription_data["medication_name"],
			prescription_data["frequency"],
		)
	if prescription_data["type"] == "exam":
		return PrescriptionExamen(
			*common_data,
			prescription_data["exam_type"],
			prescription_data["recommended_laboratory"],
		)
	return PrescriptionKinesitherapie(
		*common_data,
		prescription_data["session_count"],
		prescription_data["area_to_treat"],
	)


def save_data(consultation_service, file_path=DATA_FILE):
	"""
	Sauvegarde les patients et consultations dans un fichier JSON.

	Args:
		consultation_service (ConsultationService): Service à sauvegarder.
		file_path (str): Chemin du fichier JSON.
	"""
	saved_patients = []
	for patient in patient_service.list_all_patients():
		saved_patients.append({
			"social_security_number": patient.social_security_number,
			"last_name": patient.last_name,
			"first_name": patient.first_name,
			"birth_date": patient.birth_date.strftime("%d-%m-%Y"),
			"address": patient.address,
			"phone_number": patient.phone_number,
		})

	saved_data = {
		"patients": saved_patients,
		"consultations": [
			consultation_to_dictionary(consultation)
			for consultation in consultation_service.list_all_consultations()
		],
	}
	with open(file_path, "w") as data_file:
		json.dump(saved_data, data_file, indent=4, ensure_ascii=False)


def load_data(consultation_service, file_path=DATA_FILE):
	"""
	Charge les patients et consultations depuis un fichier JSON.

	Args:
		consultation_service (ConsultationService): Service à remplir.
		file_path (str): Chemin du fichier JSON.
	"""
	if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
		return

	with open(file_path, "r") as data_file:
		try:
			saved_data = json.load(data_file)
		except json.JSONDecodeError:
			saved_data = {}

	patient_service.patients.clear()
	for patient_data in saved_data.get("patients", []):
		patient_service.patients.append(Patient(
			patient_data["social_security_number"],
			patient_data["last_name"],
			patient_data["first_name"],
			patient_data["birth_date"],
			patient_data["address"],
			patient_data["phone_number"],
		))

	for consultation_data in saved_data.get("consultations", []):
		patient = patient_service.find_patient(
			consultation_data["patient_social_security_number"]
		)
		appointment_datetime = datetime.strptime(
			consultation_data["appointment_datetime"], "%d-%m-%Y %H:%M"
		)
		consultation = Consultation(
			appointment_datetime,
			patient,
			consultation_data["doctor"],
			consultation_data["reason"],
			consultation_data.get("diagnosis", ""),
			[
				dictionary_to_prescription(prescription_data)
				for prescription_data in consultation_data.get("prescriptions", [])
			],
			status=consultation_data.get("status", "planifiée"),
		)
		consultation_service.add_consultation(consultation)
		patient.add_consultation(consultation)


def display_patients():
	"""Affiche les patients enregistrés dans le cabinet."""
	for patient in patient_service.list_all_patients():
		print(
			f"{patient.social_security_number} - "
			f"{patient.first_name} {patient.last_name} - {patient.age} ans"
		)


def read_patient():
	"""
		Demande les informations d'un patient en répétant les saisies invalides.

		Returns:
			Patient: Patient construit avec des informations valides.
	"""
	while True:
		social_security_number = input("Numéro de sécurité sociale : ")
		try:
			verify_ssn(social_security_number)
			break
		except InvalidSecurityNumberError as error:
			print(f"Erreur : {error}")

	last_name = input("Nom : ")
	first_name = input("Prénom : ")

	while True:
		birth_date = input("Date de naissance (JJ-MM-AAAA) : ")
		try:
			datetime.strptime(birth_date, "%d-%m-%Y")
			break
		except ValueError:
			print("Erreur : la date doit respecter le format JJ-MM-AAAA.")

	address = input("Adresse : ")
	phone_number = input("Téléphone : ")
	return Patient(
		social_security_number,
		last_name,
		first_name,
		birth_date,
		address,
		phone_number,
	)


def read_existing_patient():
	"""
		Recherche un patient et répète la saisie si le numéro est inconnu.

		Returns:
			Patient: Patient trouvé dans la liste du cabinet.
	"""
	while True:
		social_security_number = input("Numéro du patient : ")
		try:
			return patient_service.find_patient(social_security_number)
		except PatientNotFoundError as error:
			print(f"Erreur : {error}")


def read_appointment_datetime():
	"""Demande une date de consultation jusqu'à obtenir le bon format."""
	while True:
		appointment_text = input("Rendez-vous (JJ-MM-AAAA HH:MM) : ")
		try:
			return datetime.strptime(appointment_text, "%d-%m-%Y %H:%M")
		except ValueError:
			print("Erreur : la date doit respecter le format JJ-MM-AAAA HH:MM.")


def read_consultation_index(consultation_service):
	"""
		Demande le numéro d'une consultation existante.

		Args:
			consultation_service (ConsultationService): Service des consultations.

		Returns:
			int: Position valide d'une consultation.
	"""
	while True:
		try:
			consultation_index = int(input("Numéro de consultation : "))
			if consultation_index < 0:
				raise ConsultationNotFoundError("Consultation introuvable")
			consultation_service.find_consultation(consultation_index)
			return consultation_index
		except (ValueError, ConsultationNotFoundError) as error:
			if isinstance(error, ValueError):
				print("Erreur : saisissez un numéro entier.")
			else:
				print(f"Erreur : {error}")


def run_application():
	"""Lance le menu console principal et sauvegarde après chaque modification."""
	consultation_service = ConsultationService()
	load_data(consultation_service)

	while True:
		print("\n1. Ajouter un patient")
		print("2. Lister les patients")
		print("3. Planifier une consultation")
		print("4. Afficher les consultations à venir")
		print("5. Marquer une consultation comme réalisée")
		print("6. Annuler une consultation")
		print("7. Ajouter un diagnostic")
		print("8. Ajouter une prescription médicamenteuse")
		print("9. Quitter")
		choice = input("Choix : ")

		if choice == "1":
			while True:
				try:
					patient = read_patient()
					patient_service.add_patient(patient)
				except DuplicatePatientError as error:
					print(f"Erreur : {error}")
				else:
					save_data(consultation_service)
					print("Patient ajouté.")
					break
		elif choice == "2":
			display_patients()
		elif choice == "3":
			try:
				patient = read_existing_patient()
				appointment_datetime = read_appointment_datetime()
				consultation_service.create_consultation(
					appointment_datetime,
					patient,
					input("Médecin : "),
					input("Motif : "),
				)
			except ValueError as error:
				print(f"Erreur : {error}")
			else:
				save_data(consultation_service)
				print("Consultation planifiée.")
		elif choice == "4":
			for consultation in consultation_service.get_upcoming_consultations():
				print(
					consultation.appointment_datetime,
					consultation.patient.first_name,
					consultation.patient.last_name,
					consultation.reason,
				)
		elif choice == "5":
			try:
				consultation_index = read_consultation_index(consultation_service)
				consultation_service.mark_consultation_as_completed(consultation_index)
			except InvalidConsultationStatusError as error:
				print(f"Erreur : {error}")
			else:
				save_data(consultation_service)
				print("Consultation réalisée.")
		elif choice == "6":
			try:
				consultation_index = read_consultation_index(consultation_service)
				consultation_service.cancel_consultation(consultation_index)
			except InvalidConsultationStatusError as error:
				print(f"Erreur : {error}")
			else:
				save_data(consultation_service)
				print("Consultation annulée.")
		elif choice == "7":
			try:
				consultation_index = read_consultation_index(consultation_service)
				consultation_service.add_diagnosis(
					consultation_index,
					input("Diagnostic : "),
				)
			except InvalidConsultationStatusError as error:
				print(f"Erreur : {error}")
			else:
				save_data(consultation_service)
				print("Diagnostic ajouté.")
		elif choice == "8":
			try:
				consultation_index = read_consultation_index(consultation_service)
				prescription = PrescriptionMedicamenteuse(
					input("Traitement : "),
					input("Dosage : "),
					input("Durée : "),
					input("Médicament : "),
					input("Fréquence : "),
				)
				consultation_service.add_prescription(consultation_index, prescription)
			except InvalidConsultationStatusError as error:
				print(f"Erreur : {error}")
			else:
				save_data(consultation_service)
				print("Prescription ajoutée.")
		elif choice == "9":
			break
		else:
			print("Choix invalide.")


if __name__ == "__main__":
	run_application()

