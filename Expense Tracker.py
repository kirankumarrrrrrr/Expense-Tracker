import json
from datetime import datetime
from collections import defaultdict

DATA_FILE = "expenses.json"

# Load existing expenses or initialize an empty list
def load_expenses():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save expenses to a file
def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        category = input("Enter category (e.g., Food, Transportation): ")
        date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
        date = date_str if date_str else datetime.now().strftime('%Y-%m-%d')

        expense = {"amount": amount, "description": description, "category": category, "date": date}
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!\n")
    except ValueError:
        print("Invalid input. Please enter numeric values for the amount.\n")

# View expenses summary
def view_summary(expenses):
    monthly_summary = defaultdict(float)
    category_summary = defaultdict(float)

    for expense in expenses:
        month = expense['date'][:7]
        monthly_summary[month] += expense['amount']
        category_summary[expense['category']] += expense['amount']

    print("\nMonthly Expense Summary:")
    for month, total in monthly_summary.items():
        print(f"{month}: ${total:.2f}")

    print("\nCategory-wise Expense Summary:")
    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")
    print()

# Display menu and handle user choices
def main():
    expenses = load_expenses()

    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expense Summary")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_summary(expenses)
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if _name_ == "_main_":
    main()
