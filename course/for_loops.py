# for loops :
# for loos : execute a block of code a fixed number of time , you can iterate a range ,string, squence etc...
# example :
"""
for x in range(1,5):
    print(f"---> iterate : {x} <---")
"""
"""
for x in range(1,10):
    print(x)
print("---> Happy New Year <---")
"""
#example : 
"""
for x in range(3):
    for y in range(1,10):
        print(y, end = "")
    print("\n")
"""
# example :
"""
rows = int(input(">>> enter the number of rows : "))
columns = int(input(">>> enter the number of columns : "))
symbole = input(">>> enter a symbole : ")

for x in range(rows):
    for y in range(columns):
        print(symbole, end = "")
    print()
"""

