# Assignment: Classes (Individual)
# Edward Magtoto 000816021

# Assignment
# Alberta Rural Patient Care (ARPC) is a new healthcare provider in Alberta. To complement the existing large-scale hospitals located in urban settings, ARPC is building a network of smaller scale mini-hospitals which target underserved rural populations. ARPC has hired your company to create a management system which is customized to meet their unique operational needs. (only for the patients section of the project)

# Table of Contents
#   IMPORTS
#   LISTS
#   READ FILE
#   WRITE IN FILE
#   ID DETERMINER
#   EDIT PATIENT
#   ADD PATIENT
#   SEARCH PATIENT
#   DISPLAY PATIENTS
#   OPTIONS
#   MENU

#   IMPORTS
import patient

#   LISTS
p_list = [] # List for Patients
id_list = [] # List for ID's

#   READ FILE
def readPatientsFile():
    p_list = []
    with open("patients.txt", "r") as i:  # Opens File
        file = i
        l = 1
        for line in file:
            if l == 1: # To skip the first line
                l += 1
                continue
            items = line.rstrip().split("_")
            person = patient.Patient(int(items[0]), items[1], items[2], items[3], int(items[4]))
            p_list.append(str(person)) # Puts Patients into a list
            iD = int(items[0])
            id_list.append(iD) # Puts ID into list
        i.close()   # Closes File
        return p_list

#   WRITE IN FILE
def writePatientsListToFile():
    addPatient = addPatientToList()
    writeList = open("patients.txt", "a")
    writeList.write(addPatient) # Writes into list
    writeList.close

#   ID DETERMINER
def determineID(x, patientID):
    for i in range(len(x)):
        if x[i] == patientID:
            return True # When user input matches existing ID
    return False # When user input does not match existing ID

#   EDIT PATIENT
def editPatientInfo():
    patientRead = readPatientsFile()
    patientID = int(input("\nEnter the Patient ID: "))
    if determineID(id_list, patientID): # If ID exists
        index = id_list.index(patientID) # Counts Posistion of list
        print(patientRead[index])   # Uses index as position for already existent patient list
        patientName = str(input("Enter Patient Name: "))
        patientDiagnosis = str(input("Enter Patient Diagnosis: "))
        patientGender = str(input("Enter Patient Gender: "))
        patientAge = int(input("Enter Patient Age: "))
        person = patient.Patient(str(patientID), patientName, patientDiagnosis, patientGender, str(patientAge))
        newPerson = person.formatPatientInfo() # Formats into proper arrangement
        with open("patients.txt", "r") as file:
            data = file.readlines() # Puts each line as a list item
        data[index+1] = newPerson # Replaces with new line
        with open("patients.txt", "w") as file:
            file.writelines(data) # Overwrites file
        displayPatientsList()
    else:
        print("Patient with ID ", patientID," not in patient file") # ERROR if ID does not exist
          
#   ADD PATIENT
def addPatientToList():
    for l in readPatientsFile():
        patientID = int(input("\nEnter Patient ID: "))
        if determineID(id_list, patientID): # ERROR if ID exists
            print("ID already exists")
            continue
        else: # Making new ID
            patientName = str(input("Enter Patient Name: "))
            patientDiagnosis = str(input("Enter Patient Diagnosis: "))
            patientGender = str(input("Enter Patient Gender: "))
            patientAge = int(input("Enter Patient age: "))
            person = patient.Patient(str(patientID), patientName, patientDiagnosis, patientGender, str(patientAge))
            newPerson = person.formatPatientInfo()  # Formats into proper arrangement
            return newPerson

#   SEARCH PATIENT
def searchPatientById():
    patientRead = readPatientsFile()
    patientID = int(input("\nEnter the Patient ID: "))
    if determineID(id_list, patientID): # If ID Exists
        print('{:<4} {:<9s} {:<11s} {:<9s} {:<9}'.format("ID", "Name", "Diagnosis", "Gender", "Age"))
        index = id_list.index(patientID)
        print(patientRead[index])
    else: # ERROR if ID does not exist
        print("Patient with ID ", patientID," not in patient file") # ERROR if ID does not exist

#   DISPLAY PATIENTS
def displayPatientsList():
    patientRead = readPatientsFile()
    print('\n')
    print('{:<4} {:<9s} {:<11s} {:<9s} {:<9}'.format("ID", "Name", "Diagnosis", "Gender", "Age"))
    print('\n'.join(patientRead)) # Displays list of Patients

#   OPTIONS
def option1():
    displayPatientsList()
    menuPatient()
def option2():
    searchPatientById()
    menuPatient()
def option3():
    writePatientsListToFile()
    menuPatient()
def option4():
    editPatientInfo()
    menuPatient()

#   MENU
def menuPatient():
    print("\nPatient Menu\n0 - Return to Main Menu\n1 - Display patient's list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit Patient info") # Patient Menu
    option = int(input("Please Enter option: ")) # Option Selection
    if option == 1:
        option1()
    if option == 2:
        option2()
    if option == 3:
        option3()
    if option == 4:
        option4()
    if option == 0:
        return

if __name__ == "__main__":
    menuPatient()