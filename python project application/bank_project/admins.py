#---- Data strucures ----:
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

ACCOUNTS_FILE = BASE_DIR / "data.csv"
TRANSACTIONS_FILE = BASE_DIR / "transactions.csv"

accounts = [
    {
        "account_id": 1001,
        "name": "Adam",
        "email": "adam@gmail.com",
        "password": "1234",
        "balance": 2500.0,
        "status": False
    },
    {
        "account_id": 1002,
        "name": "Sara",
        "email": "sara@gmail.com",
        "password": "5678",
        "balance": 1200.0,
        "status": False
    },
    {
        "account_id": 1003,
        "name": "Omar",
        "email": "omar@gmail.com",
        "password": "9999",
        "balance": 5000.0,
        "status": True
    },
    {
        "account_id": 1004,
        "name": "Lina",
        "email": "lina@gmail.com",
        "password": "4321",
        "balance": 0.0,
        "status": False
    },
    {
        "account_id": 1005,
        "name": "Youssef",
        "email": "youssef@gmail.com",
        "password": "1111",
        "balance": 800.0,
        "status": True
    },
    {
        "account_id": 1006,
        "name": "Nora",
        "email": "nora@gmail.com",
        "password": "2222",
        "balance": 3500.0,
        "status": False
    }
]

def load_accounts(file_path):
    pass

def view_not_accepted_account(data):
    print("-"*25)
    print("---> Not accepted Accounts <---")
    for item in data:
        if not item["status"]:
            print(f"---> ID {item["account_id"]} - name {item["name"]} - status : {item["status"]} <---")
    print("-"*25)


def view_accounts(data):
    print("-"*25)
    print("---> All Accounts <---")
    print("-"*50)
    print(f"{"ID":<10} {"Name":<15} {"Email":<12} {"Balance":<15} {"Status":<12}")
    print("-"*50)
    for item in data:
        print(f"{item["account_id"]:<10} {item["name"]:<15} {item["email"]:<12} {item["balance"]:<15} {"True" if item["status"] else "False":<12}")
        print("-"*50)
    print("-"*25)

#------ Searching and pending -----:

def search_ID(Id,data):
    for i,item in enumerate(data):
        if item["account_id"] == Id:
            return i
    return None

def all_accounts_approved(data):
    for item in data:
        if not item["status"]:
            return False
    return True

def highest_account(data):
   max_account = (data[0]["account_id"],data[0]["balance"])
   for item in data:
      if item["balance"] > max_account[1]:
         max_account = (item["account_id"],item["balance"])
   return max_account

def lowest_account(data):
    pass
def search_account(data):
    print("-"*25)
    print("---> Search account <---")
    while True:
        Id = int(input(">>> enter the ID you are looking for : "))
        index_id = search_ID(Id,data)

        if index_id is None:
            print("??? ID Not Founded , Try again ???")
            continue

        print("---> ID account founded <---")
        break

    user = data[index_id]
    print("="*15)
    print("----> Account informations <----")
    print("="*15)
    print(f"---> ID : {user["account_id"]} <---")
    print(f"---> Name : {user["name"]} <---")
    print(f"---> Email : {user["email"]} <---")
    password = "*" * (len(user["password"]) - 1) + user["password"][-1]
    print(f"---> Password : {password} <---")

    print("-"*25)



def approve_account(data):
    print("-"*25)
    print("---> Approve account <---")
    if not all_accounts_approved(data):
     while True:
         try:
          Id = int(input(">>> enter the ID you want to approve their request : "))
          index = search_ID(Id,data)
         except ValueError:
          print("??? The Id must be an int , try again ???")
          continue

         if index is None:
            print("??? This is not found , Try again ???")
            continue

         if data[index]["status"]:
            print("??? This acocunt is already , search for another Account ???")
            continue
         break
     user = data[index]
     choice = input(f">>> Are you sure about approving account with ID [{user['account_id']}] [Y/N] ? : ").strip().upper() == "Y"
     if choice:
         user["status"] = True
         #----- DATA SAVING -----:
         print("---> This account was approved <---")
     else:
        print("---> Nothing has been changed , See you <---")
      
    else:
        print("---> All accounts are approved , See you <---")

    print("-"*25)

def remove_account(data):
    print("-"*25)
    print("---> Remove Account <---")
    while True :
        try:
          Id = int(input(">>> enter the ID you want to remove : "))
          index = search_ID(Id,data)
        except ValueError:
          print("??? ID must be an int , try again ???")
          continue

        if index is None:
           print("??? Index is Not found , try againn ???")
           continue

        break
    user = data[index]
    Id_ = user["account_id"]
    choice = input(f">>> Are you sure about removing account with ID [{Id_}] [Y/N] ? : ").strip().upper() == "Y"
    if choice:
       data.pop(index)
       print(f"---> account with ID [{Id_}] is removed <---")
       #----- DATA SAVING -----:
    else:
       print("---> Nothing has been changed , See you <---")

        
    print("-"*25)

def analyse_accounts(data):
    print("-"*25)
    print("---> Analyse Accounts <---")
    print(f"--> Number of accounts : {len(data)} <---")
    #----- calcul how many accounts are approved and not ----:
    counter = {"approved" : 0,
               "not_approved" : 0}
    
    total_balance = 0
    for item in data:
       if item["status"]:
          counter["approved"] += 1
       else :
          counter["not_approved"] += 1
       total_balance += item["balance"]

    print(f"--> approved accounts  [{counter['approved']}] - Not aprproved  [{counter['not_approved']}] <--")
    print(f"--> total money across all accounts : {total_balance} <--")
    average = total_balance / len(data)
    print(f"--> Average of total balance : {average:.2f} <--")
    account = highest_account(data)
    print(f"--> Highest Id : {account[0]} - Highest balance : {account[1]} <---")
    
    print("-"*25)

