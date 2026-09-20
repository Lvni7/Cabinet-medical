from datetime import datetime
from functools import wraps


def validate_patient(function):
	"""
	Vérifie l'existence du patient avant l'appel de la fonction décorée.

	Args:
		function (function): Fonction recevant un numéro de sécurité sociale.

	Returns:
		function: Fonction enveloppée par la vérification.
	"""

	@wraps(function)
	def wrapper(social_security_number, *args, **kwargs):
		from services.patient_service import find_patient

		find_patient(social_security_number)
		return function(social_security_number, *args, **kwargs)

	return wrapper


def log_action(function):
	"""
	Enregistre dans logs.txt chaque appel réussi de la fonction décorée.

	Args:
		function (function): Fonction dont l'action doit être enregistrée.

	Returns:
		function: Fonction enveloppée par l'écriture du journal.
	"""

	@wraps(function)
	def wrapper(*args, **kwargs):
		result = function(*args, **kwargs)
		with open("logs.txt", "a") as log_file:
			timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
			log_file.write(f"[{timestamp}] Action effectuée : {function.__name__}\n")
		return result

	return wrapper

