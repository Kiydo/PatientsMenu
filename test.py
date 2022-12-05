import patient
import os

# path = "SAIT ITSD\Object Orientation\projects\project_individual"
# cwd = os.getcwd(path)
# except StopIteration:

# print("Current working directory: {0}".format(os.getcwd()))
p_list = []
id_list = []
name_list = []
diagnosis_list = []
gender_list = []
age_list = []
def readPatientsFile():
    with open("patients.txt", "r") as i:
        # p = patient.Patient()
        file = i
        # print(i)
        l = 1
        for line in file:
            # print(line)
            if l == 1:
                l += 1
                # print(l)
                continue
            items = line.rstrip().split("_")
            person = patient.Patient(int(items[0]), items[1], items[2], items[3], int(items[4]))
            p_list.append(str(person))

            # iD = int(items[0])
            # id_list.append(iD)

            # name = items[1]
            # name_list.append(name)

            # diagnosis = items[2]
            # diagnosis_list.append(diagnosis)

            # gender = items[3]
            # gender_list.append(gender)

            # age = int(items[4])
            # age_list.append(age)
            # print(id_list)
            
            # print(p_list)
        i.close()
        # p.set_id(id_list)
        # p.set_name(name_list)
        # p.set_diagnosis(diagnosis_list)
        # p.set_gender(gender_list)
        # p.set_age(age_list)
        return p_list
            # if patient.Patient.nbr_of_patients > 0:
            #     return person
        # last = i.read().splitlines()
        # print(last)
        # last_line = last[-1]
        # print(last_line)
    
def searchPatientById():
    patientRead = readPatientsFile()
    print(patientRead)
    

def displayPatientsList():
    patientRead = readPatientsFile()
    # print(patientRead[1])
    print('\n')
    print('{:<4} {:<9s} {:<11s} {:<9s} {:<9}'.format("ID", "Name", "Diagnosis", "Gender", "Age"))
    print('\n'.join(patientRead))
    # print(patientRead)



def menuPatient():
    # import os

    # print(os.listdir('.'))
    print("Patient Menu")
    print("0 - Return to Main Menu")
    print("1 - Display patient's list")
    print("2 - Search for patient by ID")
    print("3 - Add patient")
    print("4 - Edit Patient info")
    option = int(input("Please Enter option: "))
    if option == 1:
        displayPatientsList()
        option = int(input("Please Enter option: "))
    if option == 2:
        searchPatientById()
    # if option == 3:
    # if option == 4:
    # if option == 0:





if __name__ == "__main__":
    menuPatient()