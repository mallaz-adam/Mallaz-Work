#---- Expense Tracker ----:
import csv
from pathlib import Path

def load_data(file_path):
    pass

def save_data(file_path):
    pass

#------ DATA -------:
expenses = [
    {
        "id": 1,
        "category": "Food",
        "desciption": "Lunch",
        "amount": 45.50
    },
    {
        "id": 2,
        "category": "Transport",
        "desciption": "Taxi",
        "amount": 30.00
    },
    {
        "id": 3,
        "category": "Study",
        "desciption": "Notebook",
        "amount": 22.75
    },
    {
        "id": 4,
        "category": "Food",
        "desciption": "Coffee",
        "amount": 18.00
    },
    {
        "id": 5,
        "category": "Entertainment",
        "desciption": "Cinema",
        "amount": 70.00
    },
    {
        "id": 6,
        "category": "Transport",
        "desciption": "Bus",
        "amount": 8.00
    },
    {
        "id": 7,
        "category": "Food",
        "desciption": "Dinner",
        "amount": 85.25
    },
    {
        "id": 8,
        "category": "Study",
        "desciption": "Python Book",
        "amount": 120.00
    }
]
# --------------------------------


def add_expense(data):
    print("-"*25)
    print("---> Add expense <---")
    while True:
        try:
            amount = float(input(">>> enter the amount of the expense : "))
        except ValueError:
            print("??? the amount must be an float ???")
            continue

        if amount <= 0:
            print("??? You can input an negative amount ???")
            continue

        print("---> Amount has been accepted <---")
        break

    while True:
        category = input(">>> enter expense category : ").strip()
        if len(category) == 0:
            print("??? you can t type an empty category ???")
            continue

        break 
    while True:
        description = input(">>> enter the description of the expense : ").strip()
        if len(description) == 0:
            print("??? you can t type an empty category ???")
            continue
        break

    ids = [ idse["id"] for idse in data]
    new_id = max(ids) + 1 if ids else 1

    data.append({
        "id" : new_id,
        "category" : category,
        "desciption" : description,
        "amount" : amount

    })
    print("-"*25)



def display_expense(data):
    print("-"*25)
    print("---> Displaying All expense <---")
    print("-"*20)
    print(f"{'ID':<5}{'CATEGORY':<15}{'DESCRIPTION':<12}{'AMOUNT':>12}")
    print("-"*20)
    for expense in data:
        print(f"{expense["id"]:<5} {expense["category"]:<15} {expense["desciption"]:<12} {expense["amount"]:>12}")
    print("-"*25)


def calculate_total(data):
    amount = [amounts["amount"] for amounts in data]
    return sum(amount)

#----- Search by ID -----:
def find_ID(data,ID):
    for i,expense in enumerate(data):
        if expense["id"] == ID:
            return i
    return None

def search_expense(data):
     print("-"*25)
     print("---> Searching ID <---")
     
     print("-"*25)



def main_menu():
    pass