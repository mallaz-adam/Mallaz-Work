#---- Expense Tracker ----:
import csv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

file_path = BASE_DIR / "data" / "expense.csv"

def load_data(file_path):
    try:
      with open(file_path,"r",encoding="utf-8",newline="") as file:
         reader = csv.DictReader(file)
         data = []

         for expense in reader:
            expense["id"] = int(expense["id"])
            expense["amount"] = float(expense["amount"])

            data.append(expense)
      print("---> Your data is Back <---")
      return data
    except FileNotFoundError:
         print("---> Your DATA will be saved after your first exprience <---")
         return []

        
    
    

def save_data(file_path,data):
    fildes_name = ["id","category","desciption","amount"]
    with open(file_path,"w",encoding="utf-8",newline="") as file:
        writer = csv.DictWriter(file,fieldnames = fildes_name) 

        writer.writeheader()
        writer.writerows(data)



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



#----- Search by ID -----:
def find_ID(data,ID):
    for i,expense in enumerate(data):
        if expense["id"] == ID:
            return i
    return None

def search_expense(data):
    print("-"*25)
    print("---> Searching ID <---")
    while True:
        try:
          ID_find = int(input(">>> enter The expense you want to search for : "))
          index = find_ID(data,ID_find)
        except ValueError:
          print("??? Your ID must be an integer ???")
          continue

        if index is None:
            print("??? The ID is not found ???")
            continue

        print("---> ID is found <---")
        break

    expense = data[index]
    print("=" * 20)
    print(f"----> ID Expense : {expense["id"]} <----")
    print(f"---> Category : {expense["category"]} <---")
    print(f"---> Description : {expense["desciption"]} <---")
    print(f"---> Amount : {expense["amount"]} MAD <---")
    print("=" * 20)

 
    print("-"*25)

#----- Expense analysis -----:
def calculate_total(data):
    amount = [amounts["amount"] for amounts in data]
    return sum(amount)

def average_expense(data,total_expense):
    return (total_expense / len(data))

def expenses_above_average(data,average):
    expenses_above = []
    for expense in data:
        if expense["amount"] > average:
            expenses_above.append(expense["amount"])

    if not expenses_above:
        return None
    else:
        return expenses_above


def most_three_expensive(data):
    if len(data) < 3:
        return None

    list_amount = [{"id" : amount["id"] , "amount" : amount["amount"]} for amount in data]
    list_top_expenses = []

    for i in range(3):
        max_expense = list_amount[0]
        index = 0
        for i , item in enumerate(list_amount):
            if item["amount"] > max_expense["amount"]:
                max_expense = item
                index = i

        list_top_expenses.append(max_expense)
        list_amount.pop(index)


    
            
    return list_top_expenses


def analyse_Part(data):
    print("-"*25)
    print("----> Analyse Expense <----")
    if not data:
        print("--> There s no data saved Yet <---")
    else:
        print(f"---> Total spending :  {calculate_total(data)} MAD <---")
        sum_Data = calculate_total(data)
        print(f"---> Average expense : {average_expense(data,sum_Data):.2f} MAD <---")
        total = [amount["amount"] for amount in data]
        print(f"---> Highest expense amount : {max(total)} MAD <---")
        print(f"---> lowest expense amount : {min(total)} MAD <---")
        print("---> Three highest expenses <---")
        list_analyse = most_three_expensive(data)
        print("-"*15)
        if list_analyse is not None:
          for item in list_analyse:
            print(f"---> ID : {item["id"]} - amount : {item["amount"]} <---")
        else:
           print("??? there s no much expenses ???")
        print("-"*15)
        print("---> Expense amounts above average <---")
        list_above_average = expenses_above_average(data,average_expense(data,sum_Data))
        if list_above_average is not None:
            for i,item in enumerate(list_above_average,1):
                print(f"---> {i} : {item} <---")
        
        print("-"*15)
        
        print("-"*25)

#------ Program Start ------:
Menu = ["Add Expense","Display Expenses","Search Expense","Analyse Expenses","Back"]
print("="*30)
print("----> Expense Tracker <----")
print("="*30)
expenses = load_data(file_path)
while True:

    print("-" * 25)
    print("---> Menu <---")

    for i, item in enumerate(Menu, 1):
        print(f"--> [{i}] : {item} <--")

    print("-" * 25)

    while True:
        try:
            choice = int(input(">>> enter your choice : "))
        except ValueError:
            print("??? Your choice must be an int ???")
            continue

        break

    match choice:
        case 1:
            add_expense(expenses)

        case 2:
            display_expense(expenses)

        case 3:
            search_expense(expenses)

        case 4:
            analyse_Part(expenses)

        case 5:
            print("---> Your Data will be saved, See You <---")
            save_data(file_path, expenses)
            break

        case _:
            print("??? False Input, Try again ???")

print("-" * 25)