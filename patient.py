class Patient:
    nbr_of_patients = 0

    def __init__(self, id, name, diagnosis, gender, age):
        self.id = id
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age

    def __str__(self):
        result = f"{self.id:<5}{self.name:<10s}{self.diagnosis:<12s}{self.gender:<10s}{self.age:<10}"
        # print(self.id)
        return result

    def formatPatientInfo(self):
        added = f"{self.id}_{self.name}_{self.diagnosis}_{self.gender}_{self.age}\n"
        return added
        