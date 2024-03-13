import csv
import os

def display_menu():
    print("\nBudget Tracker Menu:")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. Analyze Expenses")
    print("5. Exit")

def add_income():
    amount = float(input("Enter income amount: "))
    with open('transactions.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Income', amount])

def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    with open('transactions.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([category, -amount])

def calculate_budget():
    total_income = 0
    total_expense = 0
    with open('transactions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if float(row[1]) > 0:
                total_income += float(row[1])
            else:
                total_expense += float(row[1])
    remaining_budget = total_income + total_expense
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Remaining Budget: {remaining_budget}")

def analyze_expenses():
    expense_data = {}
    with open('transactions.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            if float(row[1]) < 0:
                if row[0] in expense_data:
                    expense_data[row[0]] += abs(float(row[1]))
                else:
                    expense_data[row[0]] = abs(float(row[1]))
    print("Expense Analysis:")
    for category, amount in expense_data.items():
        print(f"{category}: {amount}")

def main():
    if not os.path.exists('transactions.csv'):
        with open('transactions.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Category', 'Amount'])
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            calculate_budget()
        elif choice == '4':
            analyze_expenses()
        elif choice == '5':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
