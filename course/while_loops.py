#while loop:
# while loop : is to execute some code while some condition remains true
import random
import math
# example :
"""
password  = input(">>> guess the password : ")

while password != "python":
    print("Wrong, try again")
    password = input(">>> guess the password : ")

print("Correct")
"""
#example :
"""
attempt = 3
correct_password = "ADAMLAMGHAIRBAT"
while attempt > 0:
    password = input(">>> enter your password : ")
    if password == correct_password:
        print("---> Right password , Welcome <---")
        break
    
    if password != correct_password:
        attempt -= 1
        if attempt > 0:
            print(f"??? you still have {attempt} attempts ???")
        else:
            print("??? Oops you don t have enough attempts ???")
"""
# example :
"""
correct_password = "PYTHON555"
password = input(">>> enter the hidden password : ")

while password != correct_password:
    if len(password) < len(correct_password):
        print("??? the password is too small ???")
    elif len(password) > len(correct_password):
        print("??? the password is too long ???")
    else:
        print("??? the same length but wrong password ???")
    password = input(">>> enter the hidden password : ")

print(f"---> yayyyy {password} is the right password <---")
"""
# example:
"""
attempts = 3
hidden_number = random.randint(1,10)
while attempts > 0:
    number = int(input(">>> enter the hidden number : "))
    if number == hidden_number:
        print(f"---> The number you have type is right : {hidden_number} <---")
        break
        
    else:
       attempts -= 1
       if attempts > 0:
         print(f"??? you have {attempts} attempts left ???")
         if number > hidden_number:
           print("??? the number you have type is too large ???")
         elif number < hidden_number:
          print("??? the number you have type is too small ???")
print("??? Oops you don t have enough attempts ???")

"""
# practice :
"""
principale = int(input(">>> enter principale : "))
rate = int(input(">>> enter the rate : "))
time = int(input(">>> enter the time : "))

while principale <= 0 or rate <= 0 or  time <= 0:
    if principale <= 0:
        print("??? the pricnipale are below 0 ???")
        principale = int(input(">>> enter principale : "))
    if rate <= 0:
        print("??? the rate are below 0 ???")
        rate = int(input(">>> enter the rate : "))
    if time <= 0:
        print("??? the time are below 0 ???")
        time = int(input(">>> enter the time : "))
A_t = principale *  pow((1 + rate / 100),time)
print(f"---> Final amount : {A_t} <---")
"""


  



