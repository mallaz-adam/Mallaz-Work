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
   fildes_name = ["task_id,title","status","priority"]
   with open(file_path,"w",encoding="utf-8",newline="") as file:
      writer = csv.DictWriter(file,fieldnames = fildes_name)

      writer.writeheader()
      writer.writerows(tasks)

tasks = load_data(TASKS_FILE)

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



   

    