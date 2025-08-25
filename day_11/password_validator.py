def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    # Check for uppercase letter
    has_upper = any(c.isupper() for c in password)
    if not has_upper:
        return False, "Password must contain at least one uppercase letter"
    
    # Check for lowercase letter
    has_lower = any(c.islower() for c in password)
    if not has_lower:
        return False, "Password must contain at least one lowercase letter"
    
    # Check for digit
    has_digit = any(c.isdigit() for c in password)
    if not has_digit:
        return False, "Password must contain at least one digit"
    
    return True, "Password is valid"

def main():
    print("=== Password Validator ===")
    print("Password must meet the following criteria:")
    print("- At least 8 characters long")
    print("- Contains at least one uppercase letter")
    print("- Contains at least one lowercase letter")
    print("- Contains at least one digit")
    
    while True:
        password = input("\nEnter a password (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        is_valid, message = validate_password(password)
        print(message)
        
        if is_valid:
            print("Congratulations! Your password meets all criteria.")
            break

if __name__ == "__main__":
    main()