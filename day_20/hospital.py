import csv
import os

FILE_NAME = "patients.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["patient_id", "name", "age", "gender", "disease"])  # header row


def add_patient():
    patient_id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender (M/F): ")
    disease = input("Enter Disease/Problem: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([patient_id, name, age, gender, disease])

    print("\n Patient added successfully!\n")


def display_patients():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        if not rows:
            print("\n No patient records found.\n")
            return
        print("\n Patient Records:")
        print("-" * 70)
        for row in rows:
            print(f"ID: {row['patient_id']} | Name: {row['name']} | Age: {row['age']} | Gender: {row['gender']} | Disease: {row['disease']}")
        print("-" * 70)


def search_patient():
    patient_id = input("Enter Patient ID to Search: ")
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['patient_id'] == patient_id:
                print(f"\n🔎 Found: ID: {row['patient_id']}, Name: {row['name']}, Age: {row['age']}, Gender: {row['gender']}, Disease: {row['disease']}\n")
                return
    print("\n Patient not found.\n")


def update_patient():
    patient_id = input("Enter Patient ID to Update: ")
    updated = False
    rows = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['patient_id'] == patient_id:
                print("\nEnter new details (leave blank to keep unchanged):")
                new_name = input("New Name: ") or row['name']
                new_age = input("New Age: ") or row['age']
                new_gender = input("New Gender (M/F): ") or row['gender']
                new_disease = input("New Disease: ") or row['disease']
                row = {"patient_id": patient_id, "name": new_name, "age": new_age, "gender": new_gender, "disease": new_disease}
                updated = True
            rows.append(row)

    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["patient_id", "name", "age", "gender", "disease"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n Patient updated successfully!\n")
    else:
        print("\n Patient not found.\n")


def delete_patient():
    patient_id = input("Enter Patient ID to Delete: ")
    deleted = False
    rows = []

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['patient_id'] == patient_id:
                deleted = True
            else:
                rows.append(row)

    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["patient_id", "name", "age", "gender", "disease"])
            writer.writeheader()
            writer.writerows(rows)
        print("\n Patient deleted successfully!\n")
    else:
        print("\n Patient not found.\n")


def menu():
    init_file()
    while True:
        print("\n====== Hospital Management System (CSV) ======")
        print("1. Add Patient")
        print("2. Display Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            display_patients()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            update_patient()
        elif choice == '5':
            delete_patient()
        elif choice == '6':
            print("\n Exiting... Data saved in patients.csv\n")
            break
        else:
            print("\n Invalid choice! Please try again.\n")


if __name__ == "__main__":
    menu()
