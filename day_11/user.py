def collect_user_info():
    """Collect user information"""
    print("=== User Profile System ===")
    name = input("Enter your name: ")
    
    # Validate age input
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                print("Age cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for age.")
    
    # Validate height input
    while True:
        try:
            height = float(input("Enter your height (in meters): "))
            if height < 0:
                print("Height cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for height.")
    
    # Get student status
    is_student_input = input("Are you a student? (yes/no): ").lower()
    is_student = is_student_input in ['yes', 'y', 'true']
    
    return name, age, height, is_student

def display_user_profile(name, age, height, is_student):
    """Display user profile in a formatted way"""
    print("\n--- User Profile ---")
    print(f"Name: {name}")
    print(f"Age: {age} years old")
    print(f"Height: {height} meters")
    print(f"Student Status: {'Yes' if is_student else 'No'}")

def main():
    # Collect user information
    name, age, height, is_student = collect_user_info()
    
    # Display user profile
    display_user_profile(name, age, height, is_student)

if __name__ == "__main__":
    main()