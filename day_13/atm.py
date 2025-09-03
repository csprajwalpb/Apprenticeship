correct_pin = "1234"
balance = 5000  
attempts = 0

while attempts < 3:
    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:
        print("\n PIN Accepted!")
        amount = float(input("Enter amount to withdraw: ₹ "))

        if amount <= balance:
            balance -= amount
            print("\n" + "="*40)
            print("           ATM Transaction ")
            print("="*40)
            print(f"Withdrawal Amount : ₹ {amount:.2f}")
            print(f"Remaining Balance : ₹ {balance:.2f}")
            print("="*40)
            print("Transaction Successful ")
        else:
            print("\n Insufficient Balance!")
        break
    else:
        attempts += 1
        print(f"Wrong PIN! Attempts left: {3 - attempts}")

        if attempts == 3:
            print("\n Card Blocked! Too many wrong attempts.")
