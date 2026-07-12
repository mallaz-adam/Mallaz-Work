#mini logain systeme:
import random
"""
correct_username = "adam"
correct_password = "growth123"
print("---> logain <---")
user_name = input(">>> enter your username : ").lower().strip()
password = input(">>> enter your password : ").strip()

if user_name == correct_username and password == correct_password:
    print(f"---> Welcome {user_name} Again <---")
else:
    if user_name != correct_username and password != correct_password:
        print("??? Access denied ???")
    elif user_name != correct_username:
        print("??? you have type an wrong userame ???")
    elif password != correct_password:
        print("??? you have type an wrong password ???")
"""
# name cleaner :
"""
name = input(">>> enter your name : ").strip()
name = name.title()
name = name.replace("-"," ")
print(f"---> clean name : {name} <---")
"""
# Sentence Mood detector:
"""
sentence = input(">>> enter a sentence : ").lower()

if "happy" in sentence or "good" in sentence or "great" in sentence:
    print("---> this a positive sentence <---")
elif "sad" in sentence or "tired" in sentence or "bad" in sentence:
    print("---> this is a negative sentence <---")
else:
    print("---> No clear mood detected <---")

if "?" in sentence:
    print("---> this is a question <---")
if "!" in sentence:
    print("---> Strong emotion detected <---")
"""
# Identity Card generator :
"""
print("---> Identity Card generator <---")
first_name = input(">>> enter your first name : ").strip().title()
last_name =  input(">>> enter your last name : ").strip().title()
city = input(">>> enter your City : ").strip().title()
Favorit_skill = input(">>> enter a random skill : ").strip().lower()
ID_Identity = random.randint(1000,9999)
user_name = first_name.lower() +"_"+last_name.lower()
print("---------------------------------")
print(f"---> ID :{ID_Identity} <---")
print(f"---> first name : {first_name} <---")
print(f"---> last name : {last_name} <---")
print(f"---> city : {city} <---")
print(f"---> SKILL : {Favorit_skill} <---")
print(f"---> suggested username : {user_name} <---")
print("---------------------------------")
"""



