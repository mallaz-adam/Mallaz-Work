# Logical operators = Used on conditional statements 
#      and : checks two or more conditions if true
#      OR : checks if at least on condition is true
#      not :  True if condition is false , and vice versa
#example:
"""
temp = -55

if temp > 0 and temp < 30:
    print("---> The temperature is good <---")
else :
    print("---> the temperature is Bad <---")
"""
# conditional expression : A one-Line shortcut for the if-else statement:
#example :
"""
num = int(input(">>> enter a number : "))
print(f"---> result : {"Positive num" if num > 0 else "Negative num"} <---")
"""
#example :
num = int(input(">>> enter a number : "))
result = "Even number" if num % 2 == 0 else "ODD number"
print(f"---> the number {num} is : {result} <---")

