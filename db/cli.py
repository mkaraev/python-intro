from db.app import Patient, PatientsDb
from format import BaseFormat


def dump(db):
    db.dump()


def add(db):
    print("Enter patient's data.")
    last_name = input("Please enter last name: ")
    first_name = input("Please enter first name: ")
    age = int(input("Please enter age: "))
    address = input("Please enter address: ")

    patient = Patient(last_name=last_name, first_name=first_name, age=age, address=address)
    db.add_patient(patient)


def list_patient(db):
    # plain, json
    format = input("Please enter output format: ")
    formatter = BaseFormat.from_format(format)
    print("List of patients:")
    print(formatter.format(patients=db.get_patients()))


def get_by_id(db):
    patient_id = int(input("Enter patient id: "))
    patient = db.get_patient_by_id(patient_id)
    if not patient:
        print(f"Patient with id {patient_id} not found")
    else:
        print(patient.id, patient.last_name, patient.first_name, patient.age, patient.address)


def search(db):
    # last_name=Ivanov, age=27, first_name=Ivan
    query = input("Enter search params: K").split(",")
    format = input("Please enter output format: ")
    formatter = BaseFormat.from_format(format)
    params = {}
    for param in query:
        field, value = param.split("=")
        if field == "age":
            value = int(value)
        params[field] = value

    print("Filtered list of patients:")
    print(formatter.format(patients=db.search(**params)))


def main():
    db = PatientsDb()
    commands = {
        "add": add,
        "list": list_patient,
        "get_by_id": get_by_id,
        "dump": dump,
        "search": search
    }

    while True:
        command = input("Enter command: ")
        if command == "stop":
            break

        func = commands.get(command)
        func(db)


if __name__ == '__main__':
    main()
