# object : A "bundle" of related attributes [varibales] and methodes [functions]:
# you need a "Class" to creat many objects 
# Class = [bleuprint] used to design the strucure and layout of an object
"""
class car:
    def __init__(self,model,year,color,sale): #this is the construcure functions , and self here is important
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = sale

car_one = car("mercedes",2022,"Blue",True)
print(car_one.for_sale)
print(car_one.model)
"""
# example one:
"""
class student:
    def __init__(self,name,age,gpa):
        self.Student_name = name
        self.Student_age = age
        self.student_GPA = gpa

student_one = student("adam lamghairbar",18,4.7)

print(student_one.Student_name)
print(student_one.Student_age)
"""
# example two :
"""
class City: 
  def __init__(self,name,country,population,landmarks): 
    self.name = name 
    self.country = country 
    self.population = population 
    self.landmarks = landmarks

tangier = City("Tangier","Morocco",1200000,"Hercules Caves")
paris = City("Paris","France",2100000,"Eiffel Tower")
tokyo = City("Tokyo","Japan",14000000,"Tokyo Tower")

print(vars(tangier))
print(vars(paris))
print(vars(tokyo))
"""
# exercise three : 
"""
class Pokemon:
  def __init__(self,entry,name,types,description,is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught
  def speak(self):
    print(f"{self.name} {self.name} !!")
  
  def display_details(self):
    print(f"Entry Number : {self.entry}")
    print(f"Name : {self.name}")
    print(f"Type : {self.types}")
    print(f"Description : {self.description}")

pokemon1 = Pokemon(
    25,
    "Pikachu",
    ["Electric"],
    "A yellow Pokémon that can generate electricity.",
    True
)

pokemon2 = Pokemon(
    6,
    "Charizard",
    ["Fire", "Flying"],
    "A powerful dragon-like Pokémon that breathes fire.",
    False
)

pokemon3 = Pokemon(
    7,
    "Squirtle",
    ["Water"],
    "A small turtle Pokémon that attacks using water.",
    True
)
pokemon1.speak()
print()
pokemon1.display_details()
print()
pokemon2.speak()
print()
pokemon2.display_details()
print()
pokemon3.speak()
print()
pokemon3.display_details()
"""
#-------------------------------------------------------------------------------
# class variable : shared varibale amoung all instances of a class , it has to be definied outrside the constructor 
# allow you to share data among all objects created from that class
"""
class student:
    class_year = 2026
    num_students = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        student.num_students += 1

student_one = student("Adam",18)
print(student_one.name)
print(student_one.class_year)
print(student.num_students)
"""
#-------------------------------------------------------------------------------
# class inheritance [nested class] : allows a class to inherit attributes and method from another class
# helps with code reusability and extensibility 
# class child(Parent)
"""
class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True
    
    def sleeping(self):
        print(f"{self.name} is sleeping")
    
    def eating(self):
        print(f"{self.name} is eating")

class dog(Animal):
    def speaks(self):
        print(f"{self.name} say WOOF WOOF")

dog_One = dog("Max")
dog_One.speaks()
"""



