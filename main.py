import sqlite3
import datetime

connc = sqlite3.connect("expenses.db")
cur = connc.cursor()

while True:
    print("Select an option:")
    print("1. Enter a new expense")
    print("2. View expenses summary")

    choice = int(input())

    if choice == 1:
        date = input("Enter the date (YYY-MM-DD): ")
        description = input("Enter the description of the expense: ")

        cur.execute("SELECT DISTINCT category FROM expenses")

        categories = cur.fetchall()

        print("Select a category by number:")
        for idx, category in enumerate(categories):
            print(f"{idx + 1}. {category[0]}")
        print(f"{len(categories) +1}. Create a new category")

        category_choice = int(input())
        if category_choice == len(categories) + 1:
            category = input("Enter the new category name: ")

        else:
            category = categories[category_choice - 1][0]

    elif choice == 2:
        pass
    else:
        exit()