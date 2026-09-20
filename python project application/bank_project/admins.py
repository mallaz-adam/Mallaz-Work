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
        "status": True
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

search_account(accounts)

def approve_account():
    pass

def remove_account():
    pass

def analyse_accounts():
    pass



