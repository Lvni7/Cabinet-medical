class Prescription:
    """Classe de base des prescriptions médicales."""

    def __init__(self, treatment_name, dosage, duration):
        """Initialise le traitement, son dosage et sa durée."""
        self._treatment_name = treatment_name
        self._dosage = dosage
        self._duration = duration

    @property
    def treatment_name(self):
        return self._treatment_name

    @property
    def dosage(self):
        return self._dosage

    @property
    def duration(self):
        return self._duration

    def afficher_details(self):
        """Décrit la prescription dans les classes spécialisées."""
        raise NotImplementedError("Cette méthode doit être redéfinie")


class PrescriptionMedicamenteuse(Prescription):
    """Prescription concernant un médicament."""

    def __init__(self, treatment_name, dosage, duration, medication_name, frequency):
        """Initialise le médicament, son dosage, sa fréquence et sa durée."""
        super().__init__(treatment_name, dosage, duration)
        self._medication_name = medication_name
        self._frequency = frequency

    @property
    def medication_name(self):
        return self._medication_name

    @property
    def frequency(self):
        return self._frequency

    def afficher_details(self):
        """Retourne les détails de la prescription médicamenteuse."""
        return (
            f"Médicament : {self._medication_name}\n"
            f"Dosage : {self._dosage}\n"
            f"Fréquence : {self._frequency}\n"
            f"Durée : {self._duration}"
        )


class PrescriptionExamen(Prescription):
    """Prescription concernant un examen médical."""

    def __init__(self, treatment_name, dosage, duration, exam_type, recommended_laboratory):
        """Initialise le type d'examen et le laboratoire recommandé."""
        super().__init__(treatment_name, dosage, duration)
        self._exam_type = exam_type
        self._recommended_laboratory = recommended_laboratory

    @property
    def exam_type(self):
        return self._exam_type

    @property
    def recommended_laboratory(self):
        return self._recommended_laboratory

    def afficher_details(self):
        """Retourne les détails de la prescription d'examen."""
        return (
            f"Type d'examen : {self._exam_type}\n"
            f"Laboratoire recommandé : {self._recommended_laboratory}\n"
            f"Durée : {self._duration}"
        )


class PrescriptionKinesitherapie(Prescription):
    """Prescription concernant des séances de kinésithérapie."""

    def __init__(self, treatment_name, dosage, duration, session_count, area_to_treat):
        """Initialise le nombre de séances et la zone à traiter."""
        super().__init__(treatment_name, dosage, duration)
        self._session_count = session_count
        self._area_to_treat = area_to_treat

    @property
    def session_count(self):
        return self._session_count

    @property
    def area_to_treat(self):
        return self._area_to_treat

    def afficher_details(self):
        """Retourne les détails de la prescription de kinésithérapie."""
        return (
            f"Nombre de séances : {self._session_count}\n"
            f"Zone à traiter : {self._area_to_treat}\n"
            f"Durée : {self._duration}"
        )