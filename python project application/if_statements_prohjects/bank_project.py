# bank project :
print("====================================")
print("----> Bank Systeme <----")
# password systeme :
print("--------------------------------- ")
attempt = 3
correct_password = "Adam55Mallaz"
print("--> logain check : <--")
print("---> Welcome Adam , Type your password <---")
while attempt > 0:
   password = input(">>> enter your password : ")
   if password == correct_password:
      print("---> The password is correct <---")
      break
   else:
       attempt -= 1
       if attempt > 0:
          print(f"??? You still {attempt} attempts ???")
       else:
          print("??? Oops you don t have enough attempts ???")

if attempt == 0:
   print("====================================")
   exit()
# Bank systeme start :
balance = 1000
deposit = 0
withdraw = 0
print("--------------------------------- ")
while True :
   print("----> Menu <----")
   print("--> 1. Check balance <--")
   print("--> 2. Withdraw balance <--")
   print("--> 3. Deposit balance <--")
   print("--> 0. Exit <--")
   choice = int(input(">>> enter your choice : "))
   if choice == 1:
      print("---> Balance check <---")
      print(f"--> Balance : {balance} MAD <--")
      print(f"--> deposit : + {deposit} MAD <--")
      print(f"--> Withdraw : - {withdraw} MAD <--")
   elif choice == 2:
      print("---> Withdraw <---")
      amount = float(input(">>> enter the amount of money you want to enter : "))
      if amount > balance :
         print("??? You don t have enough balance to withdraw ???")
      else:
         balance -= amount
         withdraw += amount
         print(f"---> You have withdraw {amount} MAD <---")
   elif choice == 3:
      print("---> Deposit <---")
      amount = float(input(">>> enter the amount of money you want to deposit : "))
      balance += amount 
      deposit += amount
      print(f"---> you have deposit {amount} MAD <---")
   elif choice == 0:
      print("---> Thank you for using our Bank <---")
      break
   else:
      print("---> Wrong Input , try again <---")
print("====================================")
   