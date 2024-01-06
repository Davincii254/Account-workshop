from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

# Prompt user to enter name
while True:
    name = input("Enter name to register: ")
    if len(name) > 10:
        print("Maximum number of name character should be 10 characters")
    elif len(name) == 0:
        print("Please provide a name")
    else:
        break

# Prompt user to enter PIN
while True:
    pin = input("Enter PIN: ")
    if len(pin) > 4 or len(pin) < 4:
        print("Pin must be 4 characters")
    else:
        break

# Initialize balance to 0
balance = 0

# Echo back the entered values
print("Name:", name)
print("Balance:", str(balance))


# Login loop
while True:
    name_to_validate = input("Enter your name: ")
    pin_to_validate = input("Enter your PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")


# Assuming you have imported the necessary functions:
# from banking_pkg.account import show_balance, deposit, withdraw, logout

while True:
    # Display ATM menu and get user input for option
    atm_menu(name)
    option = input("Choose an option: ")

    if option == "1":
        account.show_balance(balance)

    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)

    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)

    elif option == "4":
        # Option 4: Logout
        account.logout(name)
        break

    else:
        # Invalid option
        print("Invalid option. Please choose a valid option.")
