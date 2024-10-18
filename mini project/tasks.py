import csv
import datetime
import os

# Initialize expense data as a list of dictionaries
expenses = []

# Define the relative path for the CSV file
csv_file_path = os.path.join('data', 'expenses.csv')

def load_expenses(filename):
    """Load expenses from a CSV file"""
    global expenses
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            expenses = [row for row in reader]
    except FileNotFoundError:
        print("No previous expenses found. Starting fresh!")

def save_expenses(filename):
    """Save expenses to a CSV file"""
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['amount', 'category', 'date'])
        writer.writeheader()
        writer.writerows(expenses)

def add_expense():
    """Add a new expense"""
    amount = float(input("Enter amount: $"))
    category = input("Enter category: ")
    date = input("Enter date (or press Enter for today's date): ")
    if not date:
        date = datetime.date.today().isoformat()
    expense = {'amount': amount, 'category': category, 'date': date}
    expenses.append(expense)
    save_expenses(csv_file_path)

def view_summary():
    """View expense summaries"""
    print("Summary:")
    categories = {}
    total_spending = 0
    for expense in expenses:
        category = expense['category']
        amount = float(expense['amount'])  # Convert amount to float for calculations
        if category not in categories:
            categories[category] = 0
        categories[category] += amount
        total_spending += amount
    print("Total spending by category:")
    for category, amount in categories.items():
        print(f"  {category}: ${amount:.2f}")
    print(f"Total overall spending: ${total_spending:.2f}")

def main():
    # Ensure the data directory exists
    os.makedirs('data', exist_ok=True)
    load_expenses(csv_file_path)
    while True:
        print("Menu:")
        print("  1. Add an expense")
        print("  2. View summaries")
        print("  3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == '__main__':
    main()