# rock paper sicssors game :
import random
print("---------------------------------------")
print("---> Rock , paper , sicssors <---")
win = 0
lose = 0
draw = 0
while True :
  list_symbols = ["👊","🫲","✌️"]
  user_input = input(">>> enter (✌️, 🫲 ,👊) ? : ")
  computer_choice = random.choice(list_symbols)
  if user_input == "✌️" and computer_choice == "👊":
    print("---> You lose <---")
    print(f"---> user choose : {user_input} <---")
    print(f"---> computer choose : {computer_choice} <---")
    lose += 1
  elif user_input == "✌️" and computer_choice == "🫲":
    print("---> You Win <---")
    print(f"---> user choose : {user_input} <---")
    print(f"---> computer choose : {computer_choice} <---")
    win += 1
  elif user_input == "✌️" and computer_choice == "✌️":
    print("---> Draw <---")
    print(f"---> user choose : {user_input} <---")
    print(f"---> computer choose : {computer_choice} <---")
    draw += 1
  elif user_input == "👊" and computer_choice == "👊":
    print("---> Draw <---")
    print(f"---> user choose : {user_input} <---")
    print(f"---> computer choose : {computer_choice} <---")
    draw += 1
  elif user_input == "👊" and computer_choice == "🫲":
    print("---> You Lose <---")
    print(f"---> user choose : {user_input} <---")
    print(f"---> computer choose : {computer_choice} <---")
    lose += 1
  elif user_input == "👊" and computer_choice == "✌️":
    print("---> You Win <---")
    print(f"---> user choose : {user_input} <---")
    print(f"---> computer choose : {computer_choice} <---")
    win += 1
  elif user_input == "🫲" and computer_choice == "👊":
    print("---> You Win <---")
    print(f"---> user choose : {user_input} <---")
    print(f"---> computer choose : {computer_choice} <---")
    win += 1
  elif user_input == "🫲" and computer_choice == "🫲":
    print("---> Draw <---")
    print(f"---> user choose : {user_input} <---")
    print(f"---> computer choose : {computer_choice} <---")
    draw += 1
  elif user_input == "🫲" and computer_choice == "✌️":
    print("---> You lose <---")
    print(f"---> user choose : {user_input} <---")
    print(f"---> computer choose : {computer_choice} <---")
    lose += 1
  else:
    print("---> false input <---")
  choice = input(">>> Do You want to playe the game again (Y/N) :  ").upper() == "Y"
  if not choice :
    break
print("=================================")
print("---> Result : <---")
print(f"--> Win : {win} <--")
print(f"--> lose : {lose} <--")
print(f"--> draw : {draw} <--")
if win > lose:
  print("---> final result : The user win <---")
elif lose > win:
  print("---> final result : The computer win <---")
else:
  print("---> final result : Draw <---")
print("=================================")
print("---------------------------------------")
  
  
