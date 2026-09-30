#----- DATA -----:
import csv
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
TASKS_FILE = BASE_DIR / "tasks.csv"


def load_data(file_path):
    try:
      with open(file_path,"r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        data = []

        for line in reader:
           line["task_id"] = int(line["task_id"])
           line["status"] = line["status"] == "True"

           data.append(line)

        print("---> Data is returned <---")
        return data

    except FileNotFoundError:
       print("---> Your Data will be saved after your first Usage <---")
       return []

def save_tasks(file_path,tasks):
   fields_name = ["task_id", "title", "status", "priority"]
   with open(file_path,"w",encoding="utf-8",newline="") as file:
      writer = csv.DictWriter(file,fieldnames = fields_name)

      writer.writeheader()
      writer.writerows(tasks)



def find_task_title(task_title,data):
   for i,task in enumerate(data):
      if task["title"].lower() == task_title.lower():
         return i
   return None



def find_ID(id_f,data):
   for i,task in enumerate(data):
      if id_f == task["task_id"]:
         return i
   return None



def Searching_ID(data):
   print("-"*25)
   print("---> Searching by ID <---")
   while True:
      try: 
         id_ = int(input(">>> Enter the Id you are looking for : "))
      except ValueError:
         print("??? Your Id must be an INT ???")
         continue

      index = find_ID(id_,data)

      if index is None:
         print("??? ID is Not Founded ???")
         continue

      print("---> Id is Founded <---")
      break
   user = data[index]
   print("===== Result =====")
   print(f"---> Task Id : {user["task_id"]} <---")
   print(f"--> Task title : {user["title"]} <--")
   print(f"--> Task priority : {user["priority"]} <--")
   print(f"--> Task Status : {"Y" if user["status"] else "N"} <--")

   print("-"*25)

def Searching_title(data):
   print("-"*25)
   print("---> Searching by title <---")
   while True:
       title = input(">>> Enter the title you are looking for : ").strip()
       index = find_task_title(title,data)

       if index is None:
            print("??? Title is not found ???")
            continue

       print("---> The title has been founded <---")
       break

   user = data[index]
   print("==== Result ===")
   print(f"---> Task Id : {user["task_id"]} <---")
   print(f"--> Task title : {user["title"]} <--")
   print(f"--> Task priority : {user["priority"]} <--")
   print(f"--> Task Status : {"Y" if user["status"] else "N"} <--")

   print("-"*25)
   


def all_tasks_completed(data):
    for task in data:
        if not task["status"]:
            return False

    return True

priority = {"1" : "High", "2" : "Meduim", "3" : "Weak"}

def add_task(tasks):
   print("-"*25)
   print("---> Add Task <---")
   while True:
    title = input(">>> Enter New title : ").strip()

    if not title:
        print("??? Title cannot be empty ???")
        continue

    task_found = find_task_title(title, tasks)

    if task_found is not None:
        print("??? This Title is already used ???")
        continue

    print("---> Title Accepted <---")
    break

   print("---> Prioprity <---")

   print("-"*15)
   for i , item in priority.items():
      print(f"---> {i} : {item} <---")
   print("-"*15)

   while True:
     choice = input(">>> Enter the priority : ").strip()
     if choice not  in priority:
       print("??? The choice is not in the list ???")
       continue
     
     print("---> Priority is accepted  <---")
     priority_f = priority[choice]
     break

   ids = [item["task_id"] for item in tasks]
   if ids:
      new_id = max(ids) + 1
   else:
      new_id = 1

   new_task = {
      "task_id" : new_id,
      "title" : title,
      "status" : False,
      "priority" : priority_f
   }

   tasks.append(new_task)
   save_tasks(TASKS_FILE,tasks)

   print("-"*25)


def Display_tasks(tasks):
    print("-"*25)
    print("---> Display Tasks <---")
    print("-"*50)
    for task in tasks:
       print(f"---> ID [{task["task_id"]}] - Title [{task["title"]}] - Prioprity [{task["priority"]}] - Status [{"Completed" if task["status"] else "Pending"}] <---")
    print("-"*50)
    print("-"*25)

def showing_high_prioprity(data):
   print("-"*30)
   for task in data:
      if task["priority"].lower() == "high" :
         print(f"---> Task id : {task["task_id"]} - Task title : {task["title"]} - Task Priority : {task["priority"]} <---")
   print("-"*30)
   
def Remove_task(tasks):
   print("-"*25)
   print("---> Display Tasks <---")
   while True:
      try:
        id_ = int(input(">>> Enter ID of the task you want to remove : "))
       
      except ValueError:
        print("??? Your ID must be an int ???")
        continue

      index = find_ID(id_,tasks)

      if index is None:
         print("??? Index is Not Found ???")
         continue

      print("---> Index Is Found <---")
      break

   choice = input(">>> Are you sure about removing this Task [Y/N] ?  : ").strip().upper() == "Y"

   if choice:
      print("---> the task was removed <---")
      tasks.pop(index)
      save_tasks(TASKS_FILE,tasks)
   else:
      print("---> The task was not Removed <---")
   

      
   print("-"*25)

def complete_task(tasks):
   print("-"*25)
   print("---> Complete a task <---")
   all_task_accepted = all_tasks_completed(tasks)
   if not all_task_accepted:
     while True:
       try:  
         id_ = int(input(">>> Enter ID of the task you want to complete : "))
       except ValueError:
         print("??? The id most be an Int ???")
         continue

       index = find_ID(id_,tasks)

       if index is None:
          print("??? Index is Not found ???")
          continue
       task = tasks[index]

       if task["status"]:
          print("??? This task is already accepted , try again ???")
          continue

       print("---> Task is Founded <---")
       break

     choice = input(">>> Are you sure about Compeleting this Task [Y/N] : ").upper().strip() == "Y"
     if choice:
        print(f"---> You have completed task with ID [{task["task_id"]}] <---")
        task["status"] = True
        save_tasks(TASKS_FILE,tasks)
     else:
        print("---> NO tasks has been completed , See You <---")
   else:
      print("---> All Tasks is completed <---")


   print("-"*25)

Menu = ["Search by ID","Search by Title","Back"]
def Search(tasks):
   print("-"*25)
   print("----> Searching for Task <----")
   while True:
      print("-"*30)
      print("---> Menu <---")
      for i, item in enumerate(Menu,1):
         print(f"--> {i} : {item} <--")
      print("-"*30)
      while True:
         try:
            choice = int(input(">>> Enter your choice : "))
         except ValueError:
            print("??? Your choice most be an INT ???")
            continue

         break
      match choice:
         case 1:
            Searching_ID(tasks)
         case 2:
            Searching_title(tasks)
         case 3:
            print("---> See You , next time <---")
            break
         case _:
            print("??? Wrong Input , try again ???")
            continue
   print("-"*25)
   

menu = [
    "Add Task",
    "Display Tasks",
    "Complete Task",
    "Remove Task",
    "Search Task",
    "Show High Priority Tasks",
    "Exit"
]
tasks = load_data(TASKS_FILE)
print("="*30)
print("-----> TO DO <-----")
print("="*30)
print("----> Tasks with priority <----")
showing_high_prioprity(tasks)
while True:
  print("-"*40)
  print("---> Menu <---")
  for i,item in enumerate(menu,1):
     print(f"--> [{i}] : {item} <--")
   
  print("-"*40)
  while True:
     try:
       choice = int(input(">>> Enter your choice : "))
     except ValueError:
        print("??? Must be an INT , try again ???")
        continue

     break
  match choice:
     case 1:
        add_task(tasks)
     case 2:
        Display_tasks(tasks)
     case 3:
        complete_task(tasks)
     case 4:
        Remove_task(tasks)
     case 5:
        Search(tasks)
     case 6:
        print("---> Thank you for using Our application <---")
        break
     case _:
        print("??? Wrong Input , try again ???")
        continue
print("="*30)      
   

    