# variables :
"""
variables are containers for values [strings , float ,boolean , int]
"""
"""
# strings : 
first_name = "adam"
second_name = "lamghairbat"
#float:
student_GPA = 5.5
#int:
student_age = 14
#boolean:
student_pass = True
## output:
print(f"---> student name : {first_name} - {second_name} <---\n")
print(f"---> student age : {student_age} <---\n")
print(f"---> student gpa : {student_GPA} - {student_pass} <---\n")
"""
# User_input :
"""
---> to accept an user input we use {input("")} fonction to accept it 
---> be aware when you want to have an int or float value you must use 
{int(input()) or float(input())}
"""
#examples :
"""
name = input(">>> enter your name : ")
age = int(input(">>> enter your age : "))

print(f"---> name : {name} - age : {age} <---")
"""
# mad libs practice 1:
"""
adjecti = input(">>> enter adejctive : ")
noun = input(">>> enter a noun :  ")
adjectiv = input(">>> enter adejective  : ")
verb = input(">>> enter a verb : ")
adjective = input(">>> enter adejctive : ")

print(f"Today I went to a {adjecti} Zoo")
print(f"in a exhibit , I saw {noun}")
print(f"{noun} was {adjectiv} and {verb}ing")
print(f"I was {adjective}")
"""
# area practice 2:

print("---> Area calcultor <---")
length = float(input(">>> enter length : "))
Width = float(input(">>> enter the width : "))
area = length * Width
print(f"---> The area is {area} <---\n")

