from utils.exceptions import InvalidSecurityNumberError

def verify_ssn(self, ssn):

    if len(ssn) != 15:
        raise InvalidSecurityNumberError("Le numéro de sécurité sociale doit contenir 15 chiffres")
    
    if not ssn.isdigit():
        raise InvalidSecurityNumberError("Le numéro de sécurité sociale ne doit contenir que des chiffres")

    return ssn