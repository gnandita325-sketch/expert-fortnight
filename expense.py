from datetime import datetime

FILE_NAME = "expenses.txt"

def add_expense(amount, category, note=""):
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{amount},{category},{note}\n")
    print("✅ Expense added successfully.")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            print("\nDate        Amount   Category   Note")
            print("-" * 40)
            for line in file:
                date, amount, category, note = line.strip().split(",")
                print(f"{date}   {amount}     {category}    {note}")
    except FileNotFoundError:
        print("No expenses found.")

def expense_summary():
    summary = {}
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                _, amount, category, _ = line.strip().split(",")
                summary[category] = summary.get(category, 0) + float(amount)

        print("\n📊 Expense Summary (Category-wise)")
        print("-" * 30)
        for category, total in summary.items():
            print(f"{category}: ₹{total}")
    except FileNotFoundError:
        print("No expenses to summarize.")

def main():
    while True:
        print("\n💸 Expense Analyzer")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Expense Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food, Travel, etc): ")
            note = input("Optional note: ")
            add_expense(amount, category, note)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            expense_summary()

        elif choice == "4":
            print("👋 Exiting Expense Analyzer.")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
