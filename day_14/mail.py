email = input("Enter your email ID: ")

username, domain = email.split("@")

masked_username = username[0] + "*" * (len(username) - 1)

masked_email = masked_username + "@" + domain

print("\n" + "="*40)
print("        🔒 Masked Email ID 🔒")
print("="*40)
print(f"Original Email : {email}")
print(f"Masked Email   : {masked_email}")
print("="*40)
