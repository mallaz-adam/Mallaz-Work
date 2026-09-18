#----- Data strucure -----:
import csv 
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

ACCOUNTS_FILE = BASE_DIR / "data.csv"
TRANSACTIONS_FILE = BASE_DIR / "transactions.csv"

file_path = "accounts.csv"
file_path_transactions = "transactions.csv"
accounts = [
    {
        "account_id": 1001,
        "name": "Adam",
        "email": "adam@gmail.com",
        "password": "1234",
        "balance": 2500,
        "status": True
    },
    {
        "account_id": 1002,
        "name": "Sara",
        "email": "sara@gmail.com",
        "password": "5678",
        "balance": 1200,
        "status": False
    },
    {
        "account_id": 1003,
        "name": "Omar",
        "email": "omar@gmail.com",
        "password": "9999",
        "balance": 5000,
        "status": True
    },
    {
        "account_id": 1004,
        "name": "Lina",
        "email": "lina@gmail.com",
        "password": "4321",
        "balance": 0,
        "status": False
    },
    {
        "account_id": 1005,
        "name": "Youssef",
        "email": "youssef@gmail.com",
        "password": "1111",
        "balance": 800,
        "status": True
    }
]
def returning_data(file_path):
    try:
     with open(file_path,"r",encoding="utf-8",newline="") as file:
       reader = csv.DictReader(file)
       data = []

       for item in reader:
          item["status"] = item["status"] == "True"
          item["account_id"] = int(item["account_id"])
          item["balance"] = float(item["balance"])

          data.append(item)
       print("----> DATA is Back <----")
       return data
    except FileNotFoundError:
       print("??? The DATA will Be Saved after your first use ???")
       return []
    
          
def save_data(file_path):
    pass

def returning_transactions_data(file_path_two):
   try:
     with open(file_path_two,"r",encoding="utf-8") as file:
       reader = csv.DictReader(file)
       data = list(reader)
   except FileNotFoundError:
      print("---> File Not Found , new list was created  <---")
      data = []
   return data
       
#---- creating account ----:

def finding_name(accounts,name):
   for i , account in enumerate(accounts):
      if account["name"].lower() == name.lower():
         return i
   return None

def create_account(accounts):
    print("-"*25)
    print("---> Creat account <---")
    while True:
      name = input(">>> enter name of the account : ").strip()
      if finding_name(accounts,name) is not None:
         print("??? this name is already there ???")
         continue

      print("---> name is accepted <---")
      break
    
    while True:
      try:
        email = input(">>> enter your email : ").strip()
        index = email.index("@")
      except ValueError:
          print("??? incorrect email ???")
          continue

      print("---> email is accepted <---")
      break

    while True:
      password = input(">>> enter the PIN : ").strip()

      if len(password) != 4:
         print("??? Password must be 4 digits ???")
         continue

      if not password.isdigit():
         print("??? Password must just be numbers ???")
         continue

      print("---> Password accepted <---")
      break

    ids = [int(value["account_id"]) for value in accounts]
    new_id = max(ids) + 1 if ids else 1
    accounts.append({
               "account_id": new_id,
               "name": name,
               "email": email,
               "password": password,
               "balance": 0,
               "status": False
    })
    print("---> We will review request it most take a while <---")
    print("-"*25)

def login(accounts):
    print("-"*25)
    print("---> Login <---")
    while True:
       name = input(">>> enter account name or (Q to quit) : ").strip().upper()
       if name == "Q":
          return None
       index = finding_name(accounts,name)
       if index is None:
          print("??? Name is Not found , try again ???")
          continue

       print("---> account Name is found <---")
       break
    #---- Checking password ----:
    attempts = 3
    password = accounts[index]["password"]
    while attempts > 0:
       password_at = input(">>> enter your password : ").strip()
       if password_at == password:
          print("---> Password accepted <---")
          return index

       else:
          attempts -= 1
          if attempts > 0:
             print(f"---> You still have {attempts} attempts <--")
          else:
             print("??? Oops you don t have enough attempts ???")  
    return None     



def withdraw(account):
    print("-"*25)
    print("---> Withdraw <---")
    while True:
      try:
        amount = float(input(">>> enter the amount you want to withdraw : "))
      except ValueError:
         print("??? the amount must be an number ???")
         continue
      
      if amount <= 0:
         print("??? must be greater than 0 ???")
         continue

      break
    if account["balance"] < amount:
         print("??? You don t have enough balance for withdrawing this amount of money ???")
    else:
         print(f"---> You withdraw {amount} MAD  <---")
         account["balance"] -= amount
         transactions_saving("withdraw",account["account_id"],amount)

    print("-"*25)

def deposit(account):
    print("-"*25)
    print("---> Deposit <---")
    while True:
       try:
          amount = float(input(">>> enter the amount you want to deposit to your account : "))
       except ValueError:
          print("??? The amount must be Float ???")
          continue

       if amount <= 0:
          print("??? Amount must be positive and greater than 0 ???")
          continue

       break

    account["balance"] += amount
    print(f"---> You have deposit {amount} MAD to your account <---")
    transactions_saving("deposit",account["account_id"],amount)
    print("-"*25)
    

def view_balance(account):
    pass

def transactions_saving(type,id,amount):
   transactions = returning_transactions_data(TRANSACTIONS_FILE)

   ids = [int(idss["transaction_id"]) for idss in transactions]

   New_id = max(ids) + 1 if ids else 1

   transaction = {
      "transaction_id" : New_id,
      "account_id" : id,
      "type" : type,
      "amount" : amount
   }

   transactions.append(transaction)
   fildes_name = ["transaction_id","account_id","type","amount"]
   with open(TRANSACTIONS_FILE,"w",encoding="utf-8",newline="") as file:
      Writer = csv.DictWriter(file,fieldnames = fildes_name)
      Writer.writeheader()
      Writer.writerows(transactions)
   
#---- Program start ----:
first_Menu = ["Creat account","login","Back"]
second_Menu = ["withdraw","deposit","view balance","Back"]
print("=" * 30)
print("-----> MALLAZ BANK <-----")
print("=" * 30)
while True:
   print("----> Menu <----")
   for i , item in enumerate(first_Menu,1):
      print(f"---> {i} : {item} <---")
   while True:
     try:
      choice = int(input(">>> enter your choice : "))

     except ValueError:
        print("??? Your choice must be an int ???")
        continue

     break

   match choice:
      case 1:
         create_account(accounts)
         continue
      case 2:
          index = login(accounts)
          if index is None:
             continue
      case 3:
         print("---> Thank you , for using our service <---")
         break
      case _:
         print("??? Wrong Input , try again ???")

   user = accounts[index]
   print(f"----> Welcome to your account again {user["name"]} <----")
   while True:
      print("----> Menu <----")
      for i , item in enumerate(second_Menu,1):
         print(f"---> {i} : {item} <---")
      while True:
         try:
          choice = int(input(">>> enter your choice : "))
         except ValueError:
           print("??? your choice must be int ???")
           continue
         break
      
      match choice:
         case 1:
            pass
         case 2:
            pass
         case 3:
            pass
         case 4:
            pass
         case _:
            pass
         
      

      
      

      
   
print("=" * 30)