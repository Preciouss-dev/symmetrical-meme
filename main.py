from datetime import datetime

expenses = []
salary = 0.0

def removeExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove?")
        user_input = input("- ")
        
        if user_input.isdigit():
            expenseToRemove = int(user_input)
            if 0 <= expenseToRemove < len(expenses):
                del expenses[expenseToRemove]
                break
            else:
                print("Expense index out of range. Please try again.")
        else:
            print("Invalid input. Please enter a valid expense index.")
    
def deductFromSalary(amount):
    global salary
    salary -= amount

def addExpense(amount, category, date):
    expense = {'amount': amount, 'category': category, 'date': date}
    expenses.append(expense)
    deductFromSalary(amount)
    print("Expense added successfully!")
    calculateTotalExpenses()

def calculateTotalExpenses():
    total = sum(expense['amount'] for expense in expenses)
    print(f"Total expenses: R{total:.2f}")
    print(f"Remaining salary: R{salary:.2f}")

def printMenu():
    print("Please choose from one of the following options...")
    print("1. Add A New Expense")
    print("2. Remove An Expense")
    print("3. List All Expenses")

def listExpenses():
    print("\nHere is a list of your expenses")
    print("--------------------------------------")
    counter = 1
    for expense in expenses:
        print("*", counter, "- ", expense['amount'], " - ", expense['category'], " - ", expense['date'])
        counter += 1
    print("\n\n")
    calculateTotalExpenses()

if __name__ == "__main__":
    print("Welcome! Please input your initial salary: (R)")
    while True:
        initial_salary = input("- ")
        if initial_salary.isdigit():
            salary = float(initial_salary)
            break
        else:
            print("Invalid input. Please enter a valid amount.")

    while True:
        # get user input
        printMenu()
        optionSelected = input("- ")

        if optionSelected == "1":
            print("How much was this expense? (R)")
            while True:
                amountToAdd = input("- ")
                if amountToAdd.isdigit():
                    break
                else:
                    print("Invalid input. Please try again.")

            print("Which category does this expense fall under?")
            while True:
                category = input("- ")
                if category:
                    break
                else:
                    print("Invalid input. Please try again.")

            print("Enter the date of the expense (YYYY-MM-DD):")
            while True:
                date_str = input("- ")
                try:
                    date = datetime.strptime(date_str, '%Y-%m-%d').date()
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")

            addExpense(float(amountToAdd), category, date)
        elif optionSelected == "2":
            removeExpense()
        elif optionSelected == "3":
            listExpenses()
        else:
            print("Invalid input. Please try again.")
