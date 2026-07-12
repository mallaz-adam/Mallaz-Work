#if statement and how to use it :
#if-else-elif : DO some code IF condition is True - Else do something else - Elife is used when we want to check another condition:
#example:
"""
age = int(input(">>> enter your age : "))
if age >= 18:
    print("---> You are signed up ! <---")
elif age < 0:
    print("---> You haven t born yet <---")
else:
    print("---> you must have be 18+ to sign up <---")
"""
# practice one :
"""
response = input(">>> Would you like food (yes/no) ? : ").lower() == "yes"
if response:
    print("---> have some fooddd <---")
else:
    print("---> There is no food for you <---")
"""
# practice third:
"""
name = input(">>> enter your name : ")

if name == "":
    print("??? you did not Type your name ???")
else:
    print(f"---> Welcome again {name} <---")
"""

