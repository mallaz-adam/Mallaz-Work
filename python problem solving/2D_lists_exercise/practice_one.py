# Student Grades Table:
"""
students = [
    ["Adam", 15, 18, 12],
    ["Sara", 10, 9, 14],
    ["Yassine", 17, 16, 19],
    ["Lina", 8, 11, 10]
]
def show_students(students_list):
    print("-"*55)
    print("----> Show students <----")
    print(f"{'name':10} {'Math':10} {'Python':10} {'Englis':10}")
    print("-" * 45)
    for i in range(len(students_list)):
        for j in range(len(students_list[i])):
            print(f"{students_list[i][j]:10}",end="")
        print()
    print("-"*55)
def average_status(average):
    if average >= 16:
        return "Excellent"
    elif average >= 12:
        return "Good"
    elif average >= 10:
        return "Pass"
    else:
        return "Fail"
def find_student(students_list):
        modules = ["Math","Python","English"]
        print("-"*55)
        print("----> Search For Student <----")
        Name = input(">>> enter name of the student you are looking for : ").title().strip()
        found = False
        for row in range(len(students_list)):
            if Name == students_list[row][0]:
                 found = True
                 index = row
        if found :
            print(f"---> Founded : {students_list[index][0]} <---")
            print("-"*30)
            while True:
              print("---> Student Menu <---")
              print("--> 1. student grades <--")
              print("--> 2. student average <--")
              print("--> 0. Exit <--")
              choice = int(input(">>> enter your choice : "))
              match choice:
                  case 1:
                      print("-"*15)
                      print("---> Grades <---")
                      for i  in range(3):
                        print(f"{modules[i]} : {students_list[index][i+1]}")
                      print("-"*15)
                  case 2:
                      print("-"*15)
                      print("---> average grades  <---")
                      average = (students_list[index][1] + students_list[index][2] + students_list[index][3]) / 3
                      print(f"--> Student average : {average:2f} <--")
                      print(f"--> Status : {average_status(average)}")
                      print("-"*15)
                  case 0:
                      break
            print("-"*30)

        else:
             print("??? Student Was Not Found ???")
            
                 

        print("-"*55)
def show_Menu():
    print("-"*55)
    print("----> System Menu <----")
    print("--> 1. Show all students <--")
    print("--> 2. Search for student <--")
    print("--> 0. Exit <--")
    print("-"*55)
print("="*45) 
print("----> Grades Analyser <----")
print("="*45) 
while True:
    show_Menu()
    choice = int(input(">>> enter your choice : "))
    match choice:
        case 1:
            show_students(students)
        case 2:
            find_student(students)
        case 0:
            print("---> Thank you for using our System <---")
            break

print("="*45)    
"""
# Cinema Seats :
seats = [
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"],
    ["O", "O", "O", "O"]
]

def show_seats(list_seats):
    print("-"*30)
    print("----> Show seats <----")
    for row in list_seats:
        for seat in row:
            print(seat,end=" ")
        print()
    print("-"*30)
show_seats(seats)

def Choose_seat(list_seats):
    print("-"*30)
    print("----> Show seats <----")
    row = int(input(">>> enter the row : "))
    col = int(input(">>> enter the Col : "))
    if list_seats[row][col] == "X":
        print("---> This Seat is already booked <---")
    elif list_seats[row][col] == "O":
        choice = input(">>> Are you sure for booking this seat (Y/N) ? : ").upper().strip() == "Y"
        if choice:
            list_seats[row][col] = "X"
        else:
            print("---> See in the next time <---")
    else:
        print("??? Oops , Wrong Input ???")
    print("-"*30)
Choose_seat(seats)
show_seats(seats)

