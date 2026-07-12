# 2D_lists : is a collection of list that has another collection of list inside it:
# example : 2List = [list_one,list_two,list_three]
groceries = [["apple","orange","banana","coconut"],# rows 
             ["celery","carrots","potatoes"],
             ["chicken","fish","turkey"]]
              # col :
"""
print(groceries[0][0])
print(groceries[2][0])
"""
# for loops in two-D lists :
# single for loop:
"""
for collection in groceries:
    print(collection) # this will return an whole list in every row
"""
# nested for loops :
"""
for collection in groceries:
    for food in collection:
        print(food)
    print()
"""
#simple practice to undrstand :
"""
key_numbers = [[1,2,3],
               [4,5,6],
               [7,8,9],
               ["*",0,"#"]]
for numbers in key_numbers:
    for number in numbers:
        print(number, end= " ")
    print()
"""
# important operations in two_D arrays:
"""
library = [
    ["Atomic Habits", "James Clear", 12, 5],
    ["Deep Work", "Cal Newport", 8, 2],
    ["The Alchemist", "Paulo Coelho", 15, 9],
    ["1984", "George Orwell", 6, 1],
    ["The Psychology of Money", "Morgan Housel", 10, 4]
]
# access to an element : author of Deep work :
print(f"---> Deep Work author : {library[1][1]} <---")
# change an element : change borrowed copies of 1984 from 1 to 3:
library[3][3] = 3
print(f"---> copies borrowed of 1984 are : {library[3][3]} <---")
# print rows :
for book in library:
    title = book[0]
    author = book[1]
    total = book[2]
    borrowed = book[3]

    print(f"{title} - {author} - Total: {total} - Borrowed: {borrowed}")
# print all values:
print("-------------------------------")
for books in library:
    for book in books:
        print(book)
    print("-------------------------------")
# count values : 
counter = 0
for book in library:
    if book[2] > 10:
       counter += 1
print(f"---> Books with total copies more than 10 : {counter} <---")
# search for a value :
book_name = input(">>> enter book name : ")
found = False
for book in library:
    if  book[0] == book_name:
        print("---> book is found <---")
        found = True
        break
if not found:
    print("---> Book not found <---")
"""