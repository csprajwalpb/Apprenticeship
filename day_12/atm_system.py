class ATM:
    def __init__(self, initial_balance=0):
        """Initialize ATM with an initial balance"""
        self.balance = initial_balance
    
    def check_balance(self):
        """Display current balance"""
        print(f"Your current balance is: ${self.balance:.2f}")
    
    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully!")
            self.check_balance()
        else:
            print("Deposit amount must be positive!")
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully!")
            self.check_balance()
    
    def get_amount(self, operation):
        """Get amount for deposit or withdrawal with validation"""
        while True:
            try:
                amount = float(input(f"Enter {operation} amount: $"))
                return amount
            except ValueError:
                print("Please enter a valid amount!")
    
    def run(self):
        """Run the ATM system"""
        print("=== Welcome to Simple ATM ===")
        
        while True:
            print("\n=== ATM Menu ===")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ")
            
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = self.get_amount("deposit")
                self.deposit(amount)
            elif choice == '3':
                amount = self.get_amount("withdrawal")
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using our ATM. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1-4.")

def main():
    atm = ATM(1000)
    atm.run()

if __name__ == "__main__":
    main()