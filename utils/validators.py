from utils.exceptions import InvalidSecurityNumberError


def verify_ssn(ssn):
    """
    Vérifie qu'un numéro de sécurité sociale contient quinze chiffres.

    Args:
        ssn (str): Numéro à vérifier.

    Returns:
        str: Le numéro vérifié.

    Raises:
        InvalidSecurityNumberError: Si le format est incorrect.
    """

    if len(ssn) != 15:
        raise InvalidSecurityNumberError("Le numéro de sécurité sociale doit contenir 15 chiffres")
    
    if not ssn.isdigit():
        raise InvalidSecurityNumberError("Le numéro de sécurité sociale ne doit contenir que des chiffres")

    return ssn