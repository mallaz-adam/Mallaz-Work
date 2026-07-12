# lists projects :
# project one :
"""
grades = []
print("=====================================================")
print("----> Grades analyser <----")
print("---> fill the grades notes : <---")
n_g = int(input(">>> enter the number of grades : "))
while n_g <= 0:
    print("??? that below the normal try again ???")
    n_g = int(input(">>> enter the number of grades :  "))
for i in range(n_g):
    grade = float(input(f">>> enter grade {i + 1} : "))
    while grade < 0 or grade > 20  or grade in grades:
        print("??? false input try again ???")
        grade = float(input(f">>> enter grade {i + 1} : ")) 
    grades.append(grade)

print("---> program start <---")
while True :
    print("---> Menu <---")
    print("--> 1. Add grade <--")
    print("--> 2. remove grade <--")
    print("--> 3. analyse grades <--")
    print("--> 4. sort grades <--")
    print("--> 0. exit <--")
    choice = int(input(">>> enter your choice : "))
    match choice :
        case 1:
            print("----> Add grade <----")
            grade_add = float(input(">>> enter the new the grade : "))
            while grade_add < 0 or grade_add > 20 or grade_add in grades : 
                print("??? false input try again ???")
                grade_add = float(input(">>> enter the new grade : "))
            grades.append(grade_add)
            n_g += 1
        case 2:
            print("----> Remove grade <----")
            grade_remove = float(input(">>> enter the grade you want to remove : "))
            while grade_remove < 0 or grade_remove > 20:
                print("??? false input , try again ???")
                grade_remove = float(input(">>> enter the grade you want to remove : "))
            if grade_remove in grades:
                grade_index = grades.index(grade_remove)
                print("---> The grade is in the list <---")
                choice = input(">>> are you sure about removing the grade (Y/N) ? : ").upper() == "Y"
                if choice :
                    grades.pop(grade_index)
                    n_g -= 1
            else:
                print("??? Oops grade not found ???")
        case 3:
            print("----> Grade analyser <----")
            print("---> Grades : <---")
            print("----------------------------------------")
            for i in range(n_g):
                print(f"--> grade {i} : {grades[i]}")
            print("----------------------------------------")
            print(f"--> Highest grade : {max(grades)} <---")
            print(f"--> lowest grade : {min(grades)} <---")
            average = sum(grades) / n_g
            print(f"--> average of grades : {average} <--")
            # top three : methode !!!:
            if n_g >= 6:
              copy_grades = grades.copy()
              top_three = []
              lowest_three = []
              for i in range(3):
                highest = max(copy_grades)
                top_three.append(highest)
                copy_grades.remove(highest)
              for i in range(3):
                   lowest = min(copy_grades)
                   lowest_three.append(lowest)
                   copy_grades.remove(lowest)
              print(f"---> Top three grades : {top_three} <---")
              print(f"---> lowest three grades : {lowest_three} <---")
            else:
                print("??? Oops actions of top three and lowest three can t be completed ???")
        case 4:
            grades.sort()
            print("---> the grades are sorted <---")
        case 0:
            print("---> Thank you for using our Application <---")
            break
print("=====================================================")
"""
# project two :
name_items = []
price_items = []
print("=============================================")
print("----> Shopping cart <----")
print("---> Filling the the cart <---")
n = int(input(">>> enter the number of items in the cart : "))
while n <= 0:
    print("??? Oops wrong input , try again ???")
    n = int(">>> enter the number of items in the cart : ")
    print("-------------------------------------------------")
    for i in range(n):
        name = input(f">>> enter item {i} name : ").lower()
        price = float(input(f">>> enter item {i} price : "))
        name_items.append(name)
        price_items.append(price)
    print("-------------------------------------------------")
    while True:
        print("----> Menu <----")
        print()


