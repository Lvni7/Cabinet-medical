class PatientNotFoundError(Exception):
    """Signale qu'un patient demandé n'existe pas."""

    pass


class ConsultationNotFoundError(Exception):
    """Signale qu'une consultation demandée n'existe pas."""

    pass


class InvalidSecurityNumberError(Exception):
    """Signale qu'un numéro de sécurité sociale est invalide."""

    pass


class InvalidConsultationStatusError(Exception):
    """Signale une action impossible pour le statut d'une consultation."""

    pass


class DuplicatePatientError(Exception):
    """Signale qu'un patient existe déjà dans le cabinet."""

    pass