import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self, data_file='expenses.json'):
        self.data_file = data_file
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_expenses(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Amount must be positive.")

            expense = {
                'date': datetime.now().strftime('%Y-%m-%d'),
                'amount': amount,
                'category': category,
                'description': description
            }
            self.expenses.append(expense)
            self.save_expenses()
            print("Expense added successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def view_summary(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        summary = {}
        for expense in self.expenses:
            category = expense['category']
            summary[category] = summary.get(category, 0) + expense['amount']

        print("\nExpense Summary:")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")

    def view_monthly_summary(self, month, year):
        monthly_expenses = [
            e for e in self.expenses if e['date'].startswith(f"{year}-{str(month).zfill(2)}")
        ]

        if not monthly_expenses:
            print("No expenses for this month.")
            return

        total = sum(expense['amount'] for expense in monthly_expenses)
        print(f"\nTotal expenses for {year}-{str(month).zfill(2)}: ${total:.2f}")

    def run(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Category-wise Summary")
            print("3. View Monthly Summary")
            print("4. Exit")

            choice = input("Choose an option: ")
            
            if choice == '1':
                amount = input("Enter amount: ")
                category = input("Enter category (e.g., Food, Transport, Entertainment): ")
                description = input("Enter description: ")
                self.add_expense(amount, category, description)
            elif choice == '2':
                self.view_summary()
            elif choice == '3':
                month = input("Enter month (MM): ")
                year = input("Enter year (YYYY): ")
                self.view_monthly_summary(month, year)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == '__main__':
    tracker = ExpenseTracker()
    tracker.run()


