def show_balance(balance):
    print(f"Your balance: ${balance:.2f}")

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return balance + amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if balance < float(amount):
        print("Unatoa kila kitu bana?!")
        return balance
    return (balance - float(amount))

def logout(name):
    print(f"Goodbye, {name}!")
