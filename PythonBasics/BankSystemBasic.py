
account = {}

def createAccount():
    name = input("Enter your name : ")
    if name in account:
        print("Account already exists!")
    else:
        account[name] = 0.0
        print("Account created successfully!")

def depositMoney():
    name = input("Enter your name : ")
    if name in account:
        depMoney = float(input("Enter money to be deposited : "))
        account[name] += depMoney
        print(f"${account[name]}, Money deposited successfully!")
    else:
        print("Account does not exist!")

def withdrawMoney():
    name = input("Enter your name : ")
    if name in account:
        withMoney = float(input("Enter money to be withdrawn : "))
        if 0 < withMoney < account[name]:
            account[name] -= withMoney
            print(f"${withMoney}, Money withdrawn successfully!")
        else:
            print("Insufficient balance!")
    else:
        print("Account does not exist!")

def checkBalance():
    name = input("Enter your name : ")
    if name in account:
        balance = account[name]
        print(f"${balance}, available for, {name}")
    else:
        print("Account does not exist!")

def main():
    while True:
        print("Hello, Welcome to Bank System !!!")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Please enter your choice (1-5) : ")
        if choice == "1":
            createAccount()
        elif choice == "2":
            depositMoney()
        elif choice == "3":
            withdrawMoney()
        elif choice == "4":
            checkBalance()
        elif choice == "5":
            print("Thank you for using Bank System!")
            break
        else:
            print("Invalid choice !!!!")

main()
print("I am added just to see whether, update code pushed to Remote repo.")
print("This is to avoid merge")
