# lists_arrays : is a collections of value that can be stored in one varibale:
# Syntak : list_name = [item_one , item_two , item_three, item_four]
# example :
"""
names = ["adam","ahmed","amina","manar"]
for name in names:
    print(name, end=" ")
"""
#list indexing : list items are changeable , meaning we can update individual item within a list use indexs
# an index is an items position in a list , and python is 0-indexed , meaning indexs starts at 0:
#example :
#vowels = ["a","i","o","e","u"]
# indexes 0 , 1 , 2, 3 , 4
# n_index -5 , -4 , -3 , -2, -1
# !! important notes : indexes could be negative and it start from -1
# slicing : insted of printing one item a time using index like this : name[index] , we can use slicing so we can choose where to start and where to finish as this : name[start,end]
# example : 
"""
vowels = ["a","i","o","e","u"]
print(vowels[0:3])
print(vowels[1,3])
"""
# for-in in list : we can loop through a list with different methods : range_len() or enumerate():
"""
playlist = [
  'Porches - rangerover',
  'Mount Eerie - You Swan, Go On',
  'Hank Heaven - Threads',
  'Pinegrove - Darkness',
  'LVL UP - Spirit Was',
  'Mitski - First Love / Late Spring'
]
# methode 1: 
for i in range(len(playlist)):
  print(playlist[i])
# methode 2:
for i , song in enumerate(playlist, start = 1):
  print(f"song {i} : {song}")
"""

# practices : 
# exercise  1:
"""
numbers = [5, -2, 0, 9, -8, 3, -1]
count_positive = 0
count_negative = 0
count_zero = 0

for number in numbers:
    if number > 0:
     count_positive += 1
    elif number < 0:
       count_negative += 1
    else:
       count_zero += 1

print(f"---> positive : {count_positive} <---")
print(f"---> negative : {count_negative} <---")
print(f"---> Zero : {count_zero} <---")
"""
# exercise 2:
"""
names = ["Adam", "Sara", "Youssef", "Lina", "Omar"]
for name in names:
    print(name)
"""
# exercise 3:
"""
names = ["adam","sara","ahmed","adam","sara","karim","ahmed"]
new_name_list = []

for name in names:
    if name not in new_name_list:
        new_name_list.append(name)
    else:
        continue

print("---> New list of names : <---")

for  name in new_name_list:
    print(f"---> name : {name} <---")
"""
# exercise 4:
"""
books = ['Harry Potter','1984','The Fault in Our Stars','The Mom Test','Life in Code']
books.append("Pachinko")
books.remove('The Fault in Our Stars')
index_re = books.index('1984')
books.pop(index_re)
print(books)
"""
# exercise 5:
"""
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(f"---> even values : {numbers[::2]} <---")
print(f"---> ODD values : {numbers[1::2]} <---")
"""
# exercise 6:
"""
grades = [12, 17, 9, 14, 18, 20, 11]
print(f"---> number of grades : {len(grades)} <---")
print(f"---> highest grade : {max(grades)} <---")
print(f"---> lowest grade : {min(grades)} <---")
average = sum(grades) / len(grades)
print(f"---> average of grades : {average:2f} <---")
"""


