# functions : is a reusable block of code that can be re-used :
import random
"""
def happy_birthday():
    print("Happy birthday to you")
    print("You are old")
    print("Happy birthdat")
    print()
happy_birthday()
happy_birthday()# you can even re use it multiple time without a problem
"""
# parametres and arguments:
"""
def happy_birthday(name,age): # those are parametres
    print(f"Happy birthday to {name}")
    print(f"You are {age} years old Now")
    print("Happy birthdat")

happy_birthday("adam",55) # here we are using arguments:
"""
# first practice :
"""
def display_invoice(user_name,amount,due_date):
    print(f"---> Hello {user_name} <---")
    print(f"---> your bill of ${amount} is due to {due_date} <---")

user_name = input(">>> enter your user name : ")
amount = random.randint(100,500)
day = random.randint(1,15)
month = random.randint(1,12)
year = 2027
due_date = f"{day} / {month} / {year}"
display_invoice(user_name,amount,due_date)
"""




