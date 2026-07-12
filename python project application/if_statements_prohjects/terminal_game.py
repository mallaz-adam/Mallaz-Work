import random
# RPG GAME :

print("====================================")
print("---> MALLAZ RPG GAME <---")
print("====================================")
# player informations :
print("----> Player informations <----")
name = input(">>> enter player name : ").strip().lower()
while len(name) == 0:
    print("??? You can t type an empty name ???")
    name = input(">>> enter player name : ").strip().lower()

player_attack = 15
player_HP = 100 
postions = 3
potion_heal = 25
XP_player = 0
player_Gold = 0
print(f"---> Player name  {name} is stored !! <---")
# enimes important skills :
# Slime :
Name_enemy_one = "Slime"
slime_HP = 30
difficulty = "Easy"
slime_attack = 6
# Dark wolf :
Name_enemy_two = "Dark Wolf"
Wolf_HP = 60
difficulty = "Meduim_HARD"
Wolf_attack = 12
# skeleton_knight :
Name_enemy_three = "Skeleton knight"
skeleton_HP = 75
difficulty = "HARD"
sekeleton_attack = 15
# Game Menu and game start :
while True:
    player_HP = 100
    print("----> Menu <----")
    print("--> 1.Player state <--")
    print("--> 2.Adventure <--")
    print("--> 3.positions Shop <--")
    print("--> 4.Exit <--")
    choice = int(input(">>> enter your choice : "))
    if choice == 1:
        print("-----------------------------------")
        print("---> Player State <---")
        print(f"--> Player name : {name} <--")
        print(f"--> Player Positions : {postions} <---")
        print(f"--> Player Gold : {player_Gold} <---")
        print("-----------------------------------")
    elif choice == 2:
        print("-----------------------------------")
        print("----> Adventure part : <----")
        print("--->  Adventure Menu <---")
        print("--> 1. forest <--")
        print("--> 2. cave <--")
        print("--> 3. Village ")
        print("--> 4. Exit <--")
        choice = int(input(">>> enter your adventure : "))
        if choice == 1:
            slime_HP = 30
            print("---> enemey choosen : Slime <---")
            while player_HP > 0 and slime_HP > 0:
                print(f"===> Player HP : {player_HP} <===")
                print(f"===> Slime HP : {slime_HP} <===")
                #player Menu :
                print("---> player Menu <---")
                print("--> 1. Attack <--")
                print("--> 2. healing <--")
                print("--> 3. exit the game <--")
                choice = int(input(">>> enter your RPG choice : "))
                if choice == 1:
                    print('---> player attack -15 monster HP <---')
                    slime_HP -= player_attack
                    if slime_HP <= 0 :
                       print("---> The Player Win <---")
                       player_Gold += 25
                       print("---> The player Gained : + 25 Gold <---")
                       break
                elif choice == 2:
                    if postions > 0:
                        print("---> You have healed with 25 Hp point <---")
                        player_HP += 25
                        postions -= 1
                        if player_HP > 100:
                            player_HP = 100
                            print("??? next time do attention with your Hp level ???") 
                    else:
                       print("??? You don't have potions ???")
                elif choice == 3:
                    print("---> You escaped the fight <---")
                    break
                else:
                    print("??? wrong input , try again ???")
                    continue
                # monster part :
                monster_choice = random.randint(1,3)
                if monster_choice == 1:
                    print(f"---> The monster attack an normal attatck , - {slime_attack} Player HP <---")
                    player_HP -= slime_attack
                elif monster_choice == 2:
                     print(f"---> The monster attack an hard attatck , - {slime_attack + 4} Player HP <---")
                     player_HP -= slime_attack + 4
                else:
                    print("---> The monster miss the attack , - 0 HP player <---")
                if player_HP <= 0:
                    print("---> Game over , Player lose <---")
                    break
                else:
                    print("---> Game continue <---")
        elif choice == 2:
            Wolf_HP = 60
            print(f"---> enemey choosen : {Name_enemy_two} <---")
            while player_HP > 0 and Wolf_HP > 0:
                print(f"===> Player HP : {player_HP} <===")
                print(f"===> Wolf HP : {Wolf_HP} <===")
                #player Menu :
                print("---> player Menu <---")
                print("--> 1. Attack <--")
                print("--> 2. healing <--")
                print("--> 3. exit the game <--")
                choice = int(input(">>> enter your RPG choice : "))
                if choice == 1:
                    print('---> player attack -15 monster HP <---')
                    Wolf_HP -= player_attack
                    if Wolf_HP <= 0 :
                       print("---> The Player Win <---")
                       player_Gold += 50
                       print("---> The player Gained : + 50 Gold <---")
                       break
                elif choice == 2:
                    if postions > 0:
                        print("---> You have healed with 25 Hp point <---")
                        player_HP += 25
                        postions -= 1
                        if player_HP > 100:
                            player_HP = 100
                            print("??? next time do attention with your Hp level ???") 
                    else:
                       print("??? You don't have potions ???")
                elif choice == 3:
                    print("---> You escaped the fight <---")
                    break
                else:
                    print("??? wrong input , try again ???")
                    continue
                # monster part :
                monster_choice = random.randint(1,3)
                if monster_choice == 1:
                    print(f"---> The monster attack an normal attatck , - {Wolf_attack} Player HP <---")
                    player_HP -= Wolf_attack
                elif monster_choice == 2:
                     print(f"---> The monster attack an hard attatck , - {Wolf_attack + 4} Player HP <---")
                     player_HP -= Wolf_attack + 4
                else:
                    print("---> The monster miss the attack , - 0 HP player <---")
                if player_HP <= 0:
                    print("---> Game over , Player lose <---")
                    break
                else:
                    print("---> Game continue <---")
        elif choice == 3:
            skeleton_HP = 75
            print(f"---> enemey choosen : {Name_enemy_three} <---")
            while player_HP > 0 and skeleton_HP > 0:
                print(f"===> Player HP : {player_HP} <===")
                print(f"===> skeleton HP : {skeleton_HP} <===")
                #player Menu :
                print("---> player Menu <---")
                print("--> 1. Attack <--")
                print("--> 2. healing <--")
                print("--> 3. exit the game <--")
                choice = int(input(">>> enter your RPG choice : "))
                if choice == 1:
                    print('---> player attack -15 monster HP <---')
                    skeleton_HP -= player_attack
                    if skeleton_HP <= 0 :
                       print("---> The Player Win <---")
                       player_Gold += 75
                       print("---> The player Gained : + 75 Gold <---")
                       break
                elif choice == 2:
                    if postions > 0:
                        print("---> You have healed with 25 Hp point <---")
                        player_HP += 25
                        postions -= 1
                        if player_HP > 100:
                            player_HP = 100
                            print("??? next time do attention with your Hp level ???") 
                    else:
                       print("??? You don't have potions ???")
                elif choice == 3:
                    print("---> You escaped the fight <---")
                    break
                else:
                    print("??? wrong input , try again ???")
                    continue
                # monster part :
                monster_choice = random.randint(1,3)
                if monster_choice == 1:
                    print(f"---> The monster attack an normal attatck , - {sekeleton_attack} Player HP <---")
                    player_HP -= sekeleton_attack
                elif monster_choice == 2:
                     print(f"---> The monster attack an hard attatck , - {sekeleton_attack + 4} Player HP <---")
                     player_HP -= sekeleton_attack + 4
                else:
                    print("---> The monster miss the attack , - 0 HP player <---")
                if player_HP <= 0:
                    print("---> Game over , Player lose <---")
                    break
                else:
                    print("---> Game continue <---")
               
        print("-----------------------------------")
    elif choice == 3:
          print("-----------------------------------")
          print("---> Position Shop <---")
          print("--> position : 15 Gold <--")
          number_positions = int(input(">>> enter how much positions you want to buy :  "))
          price = number_positions * 15
          if price > player_Gold:
              print(f"---> Total price : {price} <---")
              print(f"??? You don t have enough Gold to buy {number_positions} positions ???")
              print("---> See You Next time <---")

          else:
              print(f"---> Total price {price} <---")
              choice = input(f">>> are sure about completing this purchase (Y/N) ? : ").lower() == "y"
              if choice :
                  print(f"---> you have purchase {number_positions} position with {price} Gold <---")
                  player_Gold -= price
                  postions += number_positions
          print("-----------------------------------")
    elif choice == 4:
        print("---> Thank you for using our Game <---")
        break
    else:
        print("??? Wrong Input ???")
print("====================================")