import json
import os
from datetime import datetime
import matplotlib.pyplot as plt

file_name = "data.json"

# load existing data (if file exists)
def load_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as f:
            return json.load(f)
    return []

# save data back to file
def save_data(data):
    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

# function to add new expense
def add_expense():
    print("\n--- Add New Expense ---")
    
    date = input("Enter date (YYYY-MM-DD) or press enter for today: ")
    if date == "":
        date = str(datetime.today().date())

    category = input("Category (Food/Travel/Bills/etc): ")
    
    try:
        amount = float(input("Amount: "))
    except:
        print("Invalid amount!")
        return

    desc = input("Short description: ")

    new_entry = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": desc
    }

    data = load_data()
    data.append(new_entry)
    save_data(data)

    print("Expense saved!\n")

# monthly report
def monthly_summary(month):
    data = load_data()
    total = 0
    category_data = {}

    for item in data:
        if item["date"].startswith(month):
            total += item["amount"]

            cat = item["category"]
            if cat in category_data:
                category_data[cat] += item["amount"]
            else:
                category_data[cat] = item["amount"]

    print(f"\n--- Report for {month} ---")
    print("Total spent:", total)

    for c in category_data:
        print(c, ":", category_data[c])

    return category_data

# pie chart visualization
def show_chart(data):
    if len(data) == 0:
        print("Nothing to show")
        return

    labels = []
    values = []

    for k in data:
        labels.append(k)
        values.append(data[k])

    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title("Spending Breakdown")
    plt.show()

# find highest spending category
def show_highest(data):
    if not data:
        return

    high = max(data, key=data.get)
    print("\nMost spending on:", high, "-", data[high])

# simple suggestion logic
def suggestions(data):
    print("\nSuggestions:")
    for k in data:
        if data[k] > 5000:
            print("Try to reduce spending on", k)

# main menu
def main():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Monthly Report")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            month = input("Enter month (YYYY-MM): ")
            result = monthly_summary(month)
            show_highest(result)
            suggestions(result)
            show_chart(result)

        elif choice == "3":
            print("Bye!")
            break

        else:
            print("Wrong choice!")

# run program
main()