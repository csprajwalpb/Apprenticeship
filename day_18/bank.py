class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" ₹{amount} deposited. New Balance: ₹{self.balance}")
        else:
            print(" Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(" Insufficient balance!")
        elif amount <= 0:
            print(" Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f" ₹{amount} withdrawn. New Balance: ₹{self.balance}")

    def check_balance(self):
        print(f" Current Balance: ₹{self.balance}")


account = BankAccount("Prajwal", 1000)

account.check_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)  
account.check_balance()
