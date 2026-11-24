class Patient: #This line of code creates a class called "Patient"
    def __init__(self, name: str, bill_amount: float): #initializes Patient class with attributes name and bill_amount(tintamd aq sir mag full explanation)
        self.name = name #sets name with initial value
        self.bill_amount = bill_amount #sets initial value for bill_amount

    def get_name(self): #defines name as a method of the Patient class
        return self.name #returns the value of name

    def set_name(self, name): #defines a method to set the name
        self.name = name #sets the name with a new value

    def get_bill_amount(self): #defines bill_amount as a method of the Patient class
        return self.bill_amount #returns the value of bill_amount

    def set_bill_amount(self, bill_amount): #defines a method to set the bill_amount
        orig_amount = float(input("Original Bill: ")) #makes the user input the original bill amount
        if bill_amount >= 0: #ensures that the bill amount is not negative
            self.bill_amount = bill_amount #sets bill_amount with a new value
        else:
            print("Bill amount must not be a negative number. Please set a valid bill amount.") #prints a message if the bill amount is negative
    
    def calculate_bill(self): #defines a method to calculate the final bill amount
        return self.bill_amount #returns the value of bill_amount
    
    def display_patient_type(self): #defines a method to display the patient type
       display_patient_type = "Regular Patient" #sets the patient type as "Regular Patient"
       return display_patient_type #returns the value of display_patient_type as "Regular Patient"

class Senior_Patient(Patient): #creates a Senior_Patient class that inherits attributes from the Patient class
    def calculate_bill(self):#defines a calculate_bill method that overrides the calculate_bill method in the Patient class
        return self.bill_amount * 0.8 #returns the bill amount with a 20% discount

    def display_patient_type(self): #defines a method to display the patient type
        display_patient_type = "Senior Citizen" #sets the patient type as "Senior Citizen"
        return display_patient_type #returens the value of display_patient_type as "Senior Citizen"

class PhilHealthPatient(Patient): #creates a PhilHealthPatient class that inherits attributes from the Patient class
    def calculate_bill(self): #defines a calculate_bill method that overrides the calculate_bill method in the Patient class
        return self.bill_amount * 0.85 #returns the bill amount with a 15% discount

    def display_patient_type(self): #defines a method to display the patient type
        display_patient_type = "PhilHealth Member" #sets the patient type as "PhilHealth Member"
        return display_patient_type #returns the value of display_patient_type as "PhilHealth Member"

def display_patient_info(patient): #defines a function to display the patient information
    print(f"Patient Name: {patient.get_name()}") #prints the patient name
    print(f"Patient Type: {patient.display_patient_type()}") #prints the patient type
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}") #prints the original bill with 2 decimal places
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}") #prints the final bill with 2 decimal places

print("Hospital Billing System") #prints "Hospital Billing System"
print("------------------------") #prints a line of dashes to separate title from the rest of the output

Patient1 = Patient("Juan Dela Cruz", 15000.00) #creates an instance of the Patient class
display_patient_info(Patient1) #displays the information for Patient1

print() #prints a blank line

Patient2 = Senior_Patient("Maria Santos", 15000.00) #creates an instance of the Senior_Patient class
display_patient_info(Patient2) #displays the information for Patient2

print() #prints a blank line

Patient3 = PhilHealthPatient("Pedro Reyes", 15000.00) #creates an instance of the PhilHealthPatient class
display_patient_info(Patient3) #displays the information for Patient3

