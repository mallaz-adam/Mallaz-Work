#---- Data strucures ----:
from pathlib import Path
import csv
BASE_DIR = Path(__file__).resolve().parent

ACCOUNTS_FILE = BASE_DIR / "data.csv"
TRANSACTIONS_FILE = BASE_DIR / "transactions.csv"



def load_accounts(file_path):
    try:
      with open(file_path,"r",encoding="utf-8",newline="") as file:
       reader = csv.DictReader(file)
       data = []
       for line in reader:

          line["account_id"] = int(line["account_id"])
          line["balance"] = float(line["balance"])
          line["status"] = line["status"] == "True"

          data.append(line)
       print("---> ACCOUNTS : DATA IS RERUENED <---")
          
       return data
    except FileNotFoundError:
      print("??? Program need accounts to work , try again later ???")
      return None
def load_transactions(file_path):
   try:
     with open(file_path,"r",encoding="utf-8") as file:
       reader = csv.DictReader(file)
       data = []
       for line in reader:

          line["transaction_id"] = int(line["transaction_id"])
          line["account_id"] = int(line["account_id"])
          line["amount"] = float(line["amount"])

          data.append(line)
       print("---> TRANSACTIONS : DATA IS RETURNED <---")
       return data

   except FileNotFoundError:
      print("---> Transaction will be saved when someone use his account <---")
      return []
def save_accounts(file_path,data):
   fildes_name = list(data[0].keys())
   with open(file_path,"w",encoding="utf-8") as file:
      writer = csv.DictWriter(file,fieldnames=fildes_name)

      writer.writeheader()
      writer.writerows(data)

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

def lowest_account(data,max_account):
   lowest_account = (max_account[0],max_account[1])
   for account in data:
      if account["balance"] < lowest_account[1]:
         lowest_account = (account["account_id"],account["balance"])
   return lowest_account
    
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
         save_accounts(ACCOUNTS_FILE,data)
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
       save_accounts(ACCOUNTS_FILE,data)
    else:
       print("---> Nothing has been changed , See you <---")

        
    print("-"*25)

def analyse_accounts(data, transaction_data):
    print("-" * 25)
    print("---> Analyse Accounts <---")
    print("=" * 30)

    # ---------- Accounts analysis ----------
    if data:
        print(f"--> Number of accounts : {len(data)} <---")

        counter = {
            "approved": 0,
            "not_approved": 0
        }

        total_balance = 0

        for item in data:
            if item["status"]:
                counter["approved"] += 1
            else:
                counter["not_approved"] += 1

            total_balance += item["balance"]

        print(
            f"--> Approved accounts [{counter['approved']}] - "
            f"Not approved [{counter['not_approved']}] <--"
        )

        print(
            f"--> Total money across all accounts : "
            f"[{total_balance}] MAD <--"
        )

        average = total_balance / len(data)

        print(
            f"--> Average balance : "
            f"[{average:.2f}] MAD <--"
        )

        highest = highest_account(data)

        print(
            f"--> Highest ID : [{highest[0]}] - "
            f"Highest Balance : [{highest[1]}] MAD <--"
        )

        lowest = lowest_account(data, highest)

        print(
            f"--> Lowest ID : [{lowest[0]}] - "
            f"Lowest Balance : [{lowest[1]}] MAD <--"
        )

    else:
        print("??? No accounts found ???")

    # ---------- Transactions analysis ----------
    print("=" * 30)
    print("---> Transactions Analyse <---")

    if transaction_data:

        total_transaction_amount = 0
        total_deposits = 0
        total_withdrawals = 0

        for transaction in transaction_data:

            total_transaction_amount += transaction["amount"]

            if transaction["type"] == "deposit":
                total_deposits += transaction["amount"]

            elif transaction["type"] == "withdraw":
                total_withdrawals += transaction["amount"]

        print(
            f"--> Total Transaction Amount : "
            f"[{total_transaction_amount}] MAD <--"
        )

        print(
            f"--> Total Deposits : "
            f"[{total_deposits}] MAD <--"
        )

        print(
            f"--> Total Withdrawals : "
            f"[{total_withdrawals}] MAD <--"
        )

        # ---------- Largest deposit / withdrawal ----------

        all_deposits = [
            transaction["amount"]
            for transaction in transaction_data
            if transaction["type"] == "deposit"
        ]

        all_withdrawals = [
            transaction["amount"]
            for transaction in transaction_data
            if transaction["type"] == "withdraw"
        ]

        if all_deposits:
            print(
                f"---> Largest Deposit : "
                f"[{max(all_deposits)}] MAD <---"
            )
        else:
            print("---> No deposits yet <---")

        if all_withdrawals:
            print(
                f"---> Largest Withdrawal : "
                f"[{max(all_withdrawals)}] MAD <---"
            )
        else:
            print("---> No withdrawals yet <---")

        # ---------- Account with most transactions ----------

        accounts_transactions = {}

        for transaction in transaction_data:

            account_id = transaction["account_id"]

            if account_id not in accounts_transactions:
                accounts_transactions[account_id] = 1
            else:
                accounts_transactions[account_id] += 1

        largest_id = max(
            accounts_transactions,
            key=accounts_transactions.get
        )

        print(
            f"---> ID of account with most transactions : "
            f"[{largest_id}] <---"
        )

        print(
            f"---> Number of transactions : "
            f"[{accounts_transactions[largest_id]}] <---"
        )

    else:
        print("??? Transaction list is still empty for now ???")

    print("=" * 30)
    print("-" * 25)

choices = [
    "View all accounts",
    "View pending accounts",
    "Search account",
    "Approve account",
    "Remove account",
    "Analyse accounts",
    "Exit"
]
print("="*60)
print("-----> BANK MALLAZ ADMINS <-----")
print("="*60)
print("-"*25)
print("----> LOADING DATA <----")

accounts = load_accounts(ACCOUNTS_FILE)

if accounts is not None:
   transactions = load_transactions(TRANSACTIONS_FILE)
   print("-"*25)
   while True:
      print("---> ADMINS MENU <---")
      for i,item in enumerate(choices,1):
         print(f"--> {i} : {item} <---")
      


      print("-"*25)
      while True:
         try:
            choice = int(input(">>> enter your choice : "))
         except ValueError:
            print("??? Your choice must be an INT ???")
            continue
         break
      match choice:
         case 1:
            view_accounts(accounts)
         case 2:
            view_not_accepted_account(accounts)
         case 3:
            search_account(accounts)
         case 4:
            approve_account(accounts)
         case 5:
            remove_account(accounts)
         case 6:
            analyse_accounts(accounts,transactions)
         case 7:
            print("---> Thank YOU for working with us <---")
            break
         case _:
            print("??? Wrong Input , Try again ???")
            continue
   
else:
  print("---> Re use it when there s enough DATA to work with <---")
  print("-"*25)


print("="*60)
