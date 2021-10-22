import json
from format import JsonFormat


class Patient:
    next_id = 1

    def __init__(self, last_name, first_name, age, address, id=None):
        self.id = id or Patient.next_id
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.address = address
        Patient.next_id += 1

    def __str__(self):
        return (
            f"id={self.id} last_name={self.last_name}"
            f" first_name={self.first_name} age={self.age} address={self.address}"
        )

    def __getitem__(self, item):
        return self.__dict__[item]


class PatientsDb:
    def __init__(self):
        self.patients = self._load()

    def _load(self):
        patients_dict = {}
        try:
            with open("db.json") as f:
                patients = json.loads(f.read())
                patients = [
                    Patient(
                        last_name=patient["last_name"],
                        first_name=patient["first_name"],
                        age=patient["age"],
                        address=patient["address"],
                        id=patient["id"]
                    )
                    for patient in patients
                ]
                patients_dict = {patient.id: patient for patient in patients}

        except FileNotFoundError as error:
            print("DB dump doesn't exists")

        return patients_dict

    def add_patient(self, patient):
        self.patients.update({patient.id: patient})

    def get_patients(self):
        return list(self.patients.values())

    def get_patient_by_id(self, patient_id):
        return self.patients.get(patient_id)

    def search(self, **kwargs):
        last_name = kwargs.get("last_name")
        first_name = kwargs.get("first_name")
        age = kwargs.get("age")
        patients = self.get_patients()
        if last_name:
            patients = list(filter(lambda patient: patient.last_name == last_name, patients))
        if first_name:
            patients = list(filter(lambda patient: patient.first_name == first_name, patients))
        if age:
            patients = list(filter(lambda patient: patient.ageK == age, patients))
        return patients

    def dump(self):
        with open("db.json", mode="w") as f:
            formatter = JsonFormat()
            data = formatter.format(self.get_patients())
            f.write(data)
