import os
import datetime

# Function to take user input for daily expenses
def add_expense(expense_data):
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the expense category (e.g., food, transportation, entertainment): ")

    # Get current date
    now = datetime.datetime.now()
    month, year = now.month, now.year

    expense_data.append({
        'amount': amount,
        'description': description,
        'category': category,
        'month': month,
        'year': year
    })

# Function to save expenses to a file
def save_expenses_to_file(expense_data, filename='expenses.txt'):
    with open(filename, 'w') as file:
        for expense in expense_data:
            file.write(f"{expense['amount']},{expense['description']},{expense['category']},{expense['month']},{expense['year']}\n")

# Function to load expenses from a file
def load_expenses_from_file(filename='expenses.txt'):
    expense_data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                amount, description, category, month, year = line.strip().split(',')
                expense_data.append({
                    'amount': float(amount),
                    'description': description,
                    'category': category,
                    'month': int(month),
                    'year': int(year)
                })
    except FileNotFoundError:
        pass  # Handle the case where the file doesn't exist
    return expense_data

# Function to get total expenses for a specific category
def get_category_total(expense_data, category):
    return sum(expense['amount'] for expense in expense_data if expense['category'] == category)

# Function to generate a monthly summary
def generate_monthly_summary(expense_data, month, year):
    monthly_expenses = [expense for expense in expense_data if expense['month'] == month and expense['year'] == year]
    total_monthly_expenses = sum(expense['amount'] for expense in monthly_expenses)
    return total_monthly_expenses

# Simple command-line interface
def main():
    expenses = load_expenses_from_file()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year: "))
            monthly_total = generate_monthly_summary(expenses, month, year)
            print(f"Total expenses for {month}/{year}: ${monthly_total}")
        elif choice == '3':
            save_expenses_to_file(expenses)
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

