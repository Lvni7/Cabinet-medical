from abc import ABC, abstractmethod

class Prescription(ABC):
    def __init__(self, treatment_name, dosage, frequency, duration):
        self.__treatment_name = treatment_name
        self.__dosage = dosage
        self.__frequency = frequency
        self.__duration = duration

@property
def treatment_name(self):
    return self.__treatment_name

@property
def dosage(self):
    return self.__dosage

@property
def frequency(self):
    return self.__frequency 

@property
def duration(self):    
    return self.__duration

@abstractmethod
def get_prescription_details(self):
    pass

class MedicationPrescription(Prescription):
    def __init__(self, dosage, frequency, duration, medication_name):
        super().__init__(treatment_name=None, dosage=dosage, frequency=frequency, duration=duration)
        self.__medication_name = medication_name

    @property
    def medication_name(self):
        return self.__medication_name

    def afficher_details(self):
        return (
            f"Médicament : {self.__medication_name}\n"
            f"Dosage : {self._Prescription__dosage}\n"
            f"Fréquence : {self.__frequency}\n"
            f"Durée : {self._Prescription__duration}"
        )

class ExamPrescription(Prescription):
    def __init__(self, exam_type, recommended_laboratory):
        super().__init__(treatment_name=None, dosage=None, frequency=None, duration=None)
        self.__exam_type = exam_type
        self.__recommended_laboratory = recommended_laboratory

    @property
    def exam_type(self):
        return self.__exam_type

    def afficher_details(self):
        return (
            f"Type d'examen : {self.__exam_type}\n"
            f"Laboratoire recommandé : {self.__recommended_laboratory}"
        )

class PhysiotherapyPrescription(Prescription):
    def __init__(self, frequency, area_to_be_treated):
        super().__init__(treatment_name=None, dosage=None, frequency=frequency, duration=None)
        self.__area_to_be_treated = area_to_be_treated

    @property
    def area_to_be_treated(self):
        return self.__area_to_be_treated

    def afficher_details(self):
        return (
            f"Nombre de séances : {self.__frequency}\n"
            f"Zone à traiter : {self.__area_to_be_treated}"
        )