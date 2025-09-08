def calculate_average(grades):
    """Calculate the average of a list of grades"""
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def determine_letter_grade(average):
    """Determine letter grade based on average"""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def collect_grades():
    """Collect grades from user input"""
    grades = []
    subjects = ["Subject 1", "Subject 2", "Subject 3"]
    
    for subject in subjects:
        while True:
            try:
                grade = float(input(f"Enter grade for {subject}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
    
    return grades

def display_results(grades, average, letter_grade):
    """Display the results"""
    print("\n--- Grade Report ---")
    for i, grade in enumerate(grades, 1):
        print(f"Subject {i}: {grade}")
    print(f"\nAverage Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")

def main():
    print("=== Grade Calculator ===")
    
    grades = collect_grades()
    
    average = calculate_average(grades)
    
    letter_grade = determine_letter_grade(average)
    
    display_results(grades, average, letter_grade)

if __name__ == "__main__":
    main()