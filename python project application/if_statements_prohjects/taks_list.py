# Task list manager : 
tasks = []
done_status = []
print("-------------------------------------")
print("----> TASK MANAGER <----")
print("-------------------------------------")

while True:
    print("----> Menu <---")
    print("--> 1. ADD task <--")
    print("--> 2. mark task as done <--")
    print("--> 3. show  tasks <--")
    print("--> 0. Exit <--")
    choice = int(input(">>> enter your choice : "))
    match choice :
        case 1:
            print("-------------------------------------")
            task = input(">>> enter a new task : ")
            done = False
            print(f"---> Task [{task}] is added to your tasks <---")

            tasks.append(task)
            done_status.append(done)
            print("-------------------------------------")
        case 2:
            print("-------------------------------------")
            print("---> mark task as done <---")
            if len(tasks) > 0: 
               choice = int(input(">>> enter the number of : "))
               while choice > len(tasks) or choice < 1:
                   print("??? wrong input , Try again") 
                   choice = int(input(">>> enter your choice : "))
               if done_status[choice - 1]:
                   print(f"---> Task : {tasks[choice - 1]} <----")
                   print(f"--> This task is already done <---") 
               else:
                  print(f"---> Task : {tasks[choice - 1]} <----")
                  choice_c = input(">>> are you sure about marking this task as done (Y/N) ?  : ").lower().strip() == "y"
                  if choice_c:
                     done_status[choice - 1] = True
                     print(f"---> [{tasks[choice - 1]}] is marked as done <---")
            else:
                print("---> you don t have any tasks yet <---")
            print("-------------------------------------")
        case 3:
            print("-------------------------------------")
            if len(tasks) > 0:
              print("---> Task Menu <---")
              print("--> 1.show All tasks <--")
              print("--> 2.show completed task only <--")
              print("--> 3.show not completed tasks only <---")
              choice = int(input(">>> enter your choice : "))
              match choice:
                case 1:
                    print("-------------------------------------")
                    print("----> Show All Tasks <----")
                    print()
                    for i ,task in enumerate(tasks, start= 1):
                        print(f"---> Task {i} : {tasks} - done : {done_status[i - 1]} <---")

                    print("-------------------------------------")
                case 2:
                     print("-------------------------------------")
                     print("----> Show Completed tasks <----")
                     count = 0
                     for i in range(len(tasks)):
                        if done_status[i]:
                            print(f"---> task {i} : {tasks[i]} - done : {done_status[i]} <---")
                            count += 1
                     if count == 0:
                         print("---> There s no completed tasks <---")
                     print("-------------------------------------")

                    
            else:
                print("??? You don t have tasks yet ???")
            print("-------------------------------------")
                        
