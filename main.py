import sheety

print("Welcome to Francisco's Flight Club!\nWe find the best flight deals and email you.\n")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
# email = input("What is you email?\n").title()
# email_check = input("Type your email again.\n").title()

email1 = "email1"
email2 = "email2"

while email1 != email2:
    email1 = input("What is your email?\n")

    if email1.lower() == "quit" or email1.lower() == "exit":
        exit()

    email2 = input("Please verify your email:\n")

    if email2.lower() == "quit" or email2.lower() == "exit":
        exit()

print("Ok. You're in the club!")

sheety.post_new_row(first_name, last_name, email1)
