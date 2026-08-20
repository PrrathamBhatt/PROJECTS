import json
import os
from datetime import datetime


FILE_NAME = "accounts.json"


def load_accounts():
    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        json.dump(accounts, file, indent=4)


def add_transaction(account, transaction_type, amount):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    account["transactions"].append(transaction)


def create_account(accounts):

    print("\n===== CREATE ACCOUNT =====")

    account_number = input("Enter account number: ")

    if account_number in accounts:
        print("Account already exists!")
        return

    name = input("Enter your name: ")

    while True:
        pin = input("Create a 4-digit PIN: ")

        if len(pin) == 4 and pin.isdigit():
            break

        print("PIN must contain exactly 4 digits.")

    accounts[account_number] = {
        "name": name,
        "pin": pin,
        "balance": 0,
        "transactions": []
    }

    save_accounts(accounts)

    print("\nAccount created successfully! 🎉")


def login(accounts):

    print("\n===== LOGIN =====")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return None

    attempts = 3

    while attempts > 0:

        pin = input("Enter PIN: ")

        if pin == accounts[account_number]["pin"]:
            print("\nLogin successful! ✅")
            print("Welcome,", accounts[account_number]["name"])

            return account_number

        attempts -= 1

        print("Incorrect PIN.")

        if attempts > 0:
            print("Attempts remaining:", attempts)

    print("Too many incorrect attempts.")

    return None


def check_balance(account):

    print("\n===== BALANCE =====")
    print("Current balance: ₹", account["balance"])


def deposit(account):

    print("\n===== DEPOSIT =====")

    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        account["balance"] += amount

        add_transaction(account, "Deposit", amount)

        print("Deposit successful! 💰")
        print("New balance: ₹", account["balance"])

    except ValueError:
        print("Please enter a valid amount.")


def withdraw(account):

    print("\n===== WITHDRAW =====")

    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > account["balance"]:
            print("Insufficient balance.")
            return

        account["balance"] -= amount

        add_transaction(account, "Withdrawal", amount)

        print("Withdrawal successful! 💸")
        print("Remaining balance: ₹", account["balance"])

    except ValueError:
        print("Please enter a valid amount.")


def transaction_history(account):

    print("\n===== TRANSACTION HISTORY =====")

    transactions = account["transactions"]

    if not transactions:
        print("No transactions yet.")
        return

    for transaction in transactions:

        print(
            transaction["date"],
            "|",
            transaction["type"],
            "| ₹",
            transaction["amount"]
        )


def change_pin(account):

    print("\n===== CHANGE PIN =====")

    old_pin = input("Enter current PIN: ")

    if old_pin != account["pin"]:
        print("Incorrect PIN.")
        return

    while True:

        new_pin = input("Enter new 4-digit PIN: ")

        if len(new_pin) == 4 and new_pin.isdigit():
            break

        print("PIN must contain exactly 4 digits.")

    account["pin"] = new_pin

    print("PIN changed successfully! 🔐")


def atm_menu(accounts, account_number):

    account = accounts[account_number]

    while True:

        print("\n==============================")
        print("        ATM MENU")
        print("==============================")

        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Change PIN")
        print("6. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            check_balance(account)

        elif choice == "2":

            deposit(account)
            save_accounts(accounts)

        elif choice == "3":

            withdraw(account)
            save_accounts(accounts)

        elif choice == "4":

            transaction_history(account)

        elif choice == "5":

            change_pin(account)
            save_accounts(accounts)

        elif choice == "6":

            save_accounts(accounts)

            print("\nLogged out successfully. 👋")

            break

        else:

            print("Invalid choice.")



def main():

    accounts = load_accounts()

    while True:

        print("\n")
        print("==============================")
        print("       ADVANCED ATM")
        print("==============================")

        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            create_account(accounts)

        elif choice == "2":

            account_number = login(accounts)

            if account_number is not None:
                atm_menu(accounts, account_number)

        elif choice == "3":

            print("\nThank you for using Advanced ATM! 👋")
            break

        else:

            print("Invalid choice.")


main()
