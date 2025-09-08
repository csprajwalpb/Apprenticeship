import random

def generate_secret_number():
    """Generate a random number between 1 and 100"""
    return random.randint(1, 100)

def get_user_guess(attempt, max_attempts):
    """Get user's guess with input validation"""
    while True:
        try:
            guess = int(input(f"\nAttempt {attempt}: Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def evaluate_guess(guess, secret_number):
    """Evaluate the user's guess"""
    if guess == secret_number:
        return "correct"
    elif guess < secret_number:
        return "too_low"
    else:
        return "too_high"

def play_game():
    """Main game function"""
    secret_number = generate_secret_number()
    attempts = 0
    max_attempts = 7
    
    print("=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        guess = get_user_guess(attempts + 1, max_attempts)
        attempts += 1
        
        result = evaluate_guess(guess, secret_number)
        
        if result == "correct":
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            return True
        elif result == "too_low":
            print("Too low! Try a higher number.")
        else:  
            print("Too high! Try a lower number.")
            
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"You have {remaining} attempts left.")
    
    print(f"\nGame Over! The number was {secret_number}")
    return False

def main():
    while True:
        play_game()
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()