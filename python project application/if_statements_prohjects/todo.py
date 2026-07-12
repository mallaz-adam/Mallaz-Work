# TODO project : ()
tasks = []
done_tasks = []

def Add_task(tasks,done_tasks):
    print("-"*30)
    print("----> Add task <---")
    while True : 
      task = input(">>> enter new task : ").capitalize()
      while len(task) == 0:
        print("??? Oops , you can type empty task ???")
      tasks.append(task)
      done_tasks.append(False)
      print("---> The task has been added to the list <---")
      choice = input(">>> do you want to add another task (Y/N) ? : ").upper().strip() == "N"
      if choice:
         break
    print("-"*30)

def show_tasks(tasks,done_tasks):
      print("-"*30)
      print("----> Show Task <---")
      if len(tasks) > 0:
        for i in range(len(tasks)):
          print(f"---> Task {i+1} : {tasks[i]} - finished : {"Done" if done_tasks[i] else "Not Yet"} <---")
      else:
          print("??? The list of tasks is empty ???")
      print("-"*30)

def mark_task_done(tasks,done_tasks):
    print("-"*30)
    print("----> Mark Task as Done <---")
    while True:
        task = int(input(">>> enter the number of the task : "))
        while task < 1 or task > len(tasks):
            print("??? Oops , Wrong input ???")
            task = int(input(">>> enter the number of the task : "))
        print(f"---> Task found : {tasks[task - 1]} <---")
        if done_tasks[task - 1]:
            print("---> This is already done , try another task <---")
        else:
            choice = input(">>> you wanna mark this task as done (Y/N) ? :  ").upper().strip() == "Y"
            if choice:
                done_tasks[task - 1] = True
                print(f"---> The task {tasks[task - 1]} is marked as done <---")
            else:
                print("---> See you , nothing has been updated <---")
        choice = input(">>> do you want to mark another task as done (Y/N) ?: ").upper().strip() == "N"
        if choice:
            break
    print("-"*30)

def delete_tasks(tasks,done_tasks):
      print("-"*30)
      print("----> Delete a task <---")
      if len(tasks) > 0:
        task = int(input(">>> enter the number of the task you want to delete : "))
        if task > len(tasks) or task < 1:
          print("??? Wrong Input , Try again ???")
          task = int(input(">>> enter the number of the task you want to delete : "))
        print(f"---> Task found : {tasks[task - 1]} <---")
        choice = input(">>> Are you sure about removing this task (Y/N) ? : ").upper().strip() == "Y"
        if choice :
          print(f"---> The {tasks[task - 1]} has been deleted <---")
          tasks.remove(tasks[task - 1])
          done_tasks.remove(done_tasks[task - 1])
      else:
          print("??? the list of tasks is empty ???")
      print("-"*30)
      
def search_by_keyword(tasks,done_tasks):
       print("-"*30)
       print("----> search a task by keywords <---")
       if len(tasks) > 0:
           key_words = input(">>> enter a key word : ").lower().strip()
           # searching for tasks that has the same keyword :
           found = False
           for i in range(len(tasks)):
               if key_words in tasks[i].lower():
                   print(f"---> Task {i + 1} : {tasks[i]} - finished : {"Done" if done_tasks[i] else "Not yet"} <---")
                   found = True
           if not found:
               print("??? There s no task that match this key word ???")
       else:
           print("??? The list of tasks is empty ???")

       print("-"*30)

Add_task(tasks,done_tasks)
search_by_keyword(tasks,done_tasks)
mark_task_done(tasks,done_tasks)
delete_tasks(tasks,done_tasks)
show_tasks(tasks,done_tasks)