patient_id = input("Enter Patient ID: ")

if patient_id.startswith("HOSP"):
    print("\n Valid Patient ID")
else:
    print("\n Invalid Patient ID! (Must start with 'HOSP')")
