import uuid
from datetime import datetime
import json

expenses = []


def add_expense():
    '''
    This function will add the expense to the data structure.
    '''
    amount = float(input("Please enter the amount of the expense: \n"))
    category = input("Enter the category of the expense: \n")
    current_date = datetime.today().strftime("%d/%m/%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    expense = {
        "id": str(uuid.uuid4()),
        "amount": amount,
        "category": category,
        "date": current_date,
        "time": current_time
    }
    expenses.append(expense)
    print("Expense Added!")


def view_expenses():
    all_expenses = load_data()
    print("\n ---- ALL EXPENSES ---- \n")
    for i, expense in enumerate(all_expenses):
        amount = expense["amount"]
        category = expense["category"]
        print(f"--- Expense - {i+1} ---")
        print(f"Category of expense: {category}")
        print(f"Amount of expense: £{amount:.2f}\n")

    return all_expenses


def calculate_expenses():
    '''
    Function -> Iterates through the expenses amount and adding the total expenses
    '''
    all_expenses = load_data()
    total = 0
    for expense in all_expenses:
        total += expense["amount"]

    total = round(total, 2)

    print(f"Total Expenses: £{total:.2f}")


def inspect_expense():
    all_expenses = view_expenses()

    select_index = int(input("Select an Expense To Investigate: \n"))
    try:
        amount = all_expenses[select_index-1]["amount"]
        category = all_expenses[select_index-1]["category"]
        date = all_expenses[select_index-1]["date"]
        time = all_expenses[select_index-1]["time"]
        print(f"Category of expense: {category}")
        print(f"Amount of expense: £{amount:.2f}")
        print(f"Date of when expense occurred: {date}")
        print(f"Time of when expense occurred: {time}")
    except IndexError:
        print("Invalid Expense")


def save_data(expenses):
    '''
    Function saves the data and keeps add new expenses to the expenses.json file
    '''
    # Loads the JSON data
    current_expenses = load_data()

    # Combines the old expense with the new expenses
    all_expenses = current_expenses + expenses

    # Saves all expenses
    with open('expenses.json', 'w') as file:
        json.dump(all_expenses, file, indent=4)

    print("Data Saved")


def load_data():
    '''
    Function loads the data into the program
    '''
    try:
        with open('expenses.json', 'r') as file:
            try:
                expenses = json.load(file)
                return expenses
            except json.JSONDecodeError:
                print("You have no saved expenses")
                expenses = []
            return expenses
    except FileNotFoundError:
        print("We cannot find the file sorry")
        return []


while True:
    print("\n Expense Tracking Application \n")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Inspect An Expense")
    print("5. Load Data")
    print("6. Save Data")
    print("7. Quit")

    choice = input("Please enter choice: ")

    if (choice == "1"):
        add_expense()
    elif (choice == "2"):
        view_expenses()
    elif (choice == "3"):
        calculate_expenses()
    elif (choice == "4"):
        inspect_expense()
    elif (choice == "5"):
        load_data()
    elif (choice == "6"):
        save_data(expenses)
    elif (choice == "7"):
        print("Program has ended")
        break
