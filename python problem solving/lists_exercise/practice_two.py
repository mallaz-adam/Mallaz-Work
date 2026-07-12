# exercise 1:
"""
topics = ["psychology","python","astronomy"]

print("---------------------------------------")
print("---> Smart Favorite list <---")
print("---------------------------------------")
while True:
    print("---> Menu <---")
    print("--> 1.Add topic <--")
    print("--> 2.Remove a topic <--")
    print("--> 3.showing the topics <--")
    print("--> 4.sort topics <--")
    print("--> 0.exit <--")
    choice = int(input(">>> enter your choice : "))
    match choice:
        case 1:
            print("---> Add a topic <---")
            topic = input(">>> enter the topic you want to add : ").strip().lower()
            while len(topic) <= 0:
                print("??? you can t type an empty topic ???")
                topic = input(">>> enter the topic you want to add : ").strip().lower()
            if topic in topics:
                print("??? Oops this topic is already in the topics ???")
                continue
            
            topics.append(topic)
            print(f"---> the topic is added : {topic} <---")
        case 2:
            print("---> Remove a topic <---")
            topic = input(">>> enter the topic you want to remove : ").strip().lower()
            while len(topic) <= 0:
                print("??? you can t type an empty topic ???")
                topic = input(">>> enter the topic you want to add : ").strip().lower()
            if topic not in topics:
                print("??? This topics is already not in the list ???")
                continue
            else:
                topic_index = topics.index(topic)
                choice = input(f">>> are you sure about removing {topic} (Y/N) ? : ").lower() == "y"
                if choice:
                    print(f"---> {topic} is removed <---")
                    topics.remove(topic_index)
        case 3:
            print("---> showing topics <---")
            print(f"--> all topics : {topics} <--")
            print(f"--> first topic : {topics[0]} <--")
            print(f"--> last topic : {topics[-1]} <--")
        case 4:
            topics.sort()
            print("---> the last has been sorted <---")
        case 0:
            print("---> Thank you for using our programm <---")
            break
print("---------------------------------------")      
"""
# exercise 2:
print("-----> Grade Filter System <-----")
grades = [12, 17, 9, 15, 19, 7, 14]
print(f"--> All grades : {grades} <---")
print("----> Show passed grades <----")
for grade in grades:
    if grade >= 10:
        print(grade,end = " ")
print()
print("----> Show failed grades <----")
for grade in grades:
    if grade < 10:
        print(grade,end = " ")
print()

average = sum(grades) / len(grades)
print("----> Grades above the average <----")
for grade in grades:
    if grade > average:
        print(grade,end=" ")
print()
print("----> Grades below the average <----")
for grade in grades:
    if grade < average:
        print(grade,end=" ")
print()
print(f"---> highest grade : {max(grades)} <---")
print(f"---> lowest grade : {min(grades)} <---")
# important method : show top three :
grades_copy = grades.copy()
top_three = []
count = 0
for i in range(3):
    highest_in_copy = max(grades_copy)
    top_three.append(highest_in_copy)
    grades_copy.remove(highest_in_copy)
top_three.sort()
print(top_three)
# show lowest three :
grades_copy_two = grades.copy()
lowest_three = []

for i in range(3):
    lowest_in_copy = min(grades_copy_two)
    lowest_three.append(lowest_in_copy)
    grades_copy_two.remove(lowest_in_copy)
lowest_three.sort()
print(lowest_three)



        
