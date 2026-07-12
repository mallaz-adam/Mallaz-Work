# random python:
# for using module we import like this :
import random
# example of usage : random int :
"""
number = random.randint(1,10)
print(f"---> number : {number} <---")
# this will give us a random number between 1 and 10 including 1 & 10:
"""
# example of usage : random float :
"""
number = random.random()
print(f"---> random float number : {number} <---")
# this give us a random float number between 0.0 and 1.0
"""
# advanced case [lists] : random from a list :
"""
moods = ["happy", "sad", "calm", "angry", "tired"]
random.shuffle(moods)
mood = random.choice(moods)
print(mood)
# this give is a random choice from moods : (ramdom.choice(lisr))
# this shuffle the list giving : (random.shuffle(list))
"""
#exercise : random number guessing game (meed to be improved in loops file) :
"""
print("---> guessing <---")
number_computer = random.randint(1,10)
user_guess = int(input(">>> enter a guess between (1 and 10) : "))
if number_computer == user_guess:
    print("---> You WIN that s the right guess <---")
    print(f"--> user guess : {user_guess} <--")
    print(f"--> computer number : {number_computer} <--")
else:
    print("---> You LOSE that s not the right guess <---")
    print(f"--> user guess : {user_guess} <--")
    print(f"--> computer number : {number_computer} <--")
"""
# random daily question :
"""
print("---> ECHO chamber <---")
questions = [
    "What did I learn today?",
    "What emotion did I feel the most today?",
    "What should I forgive myself for?",
    "What is one thing I want to improve tomorrow?"
]

question = random.choice(questions)
print(f"--> Today question : {question} <--")
answer = input(">>> enter your answer : ")
print("\n")
print("---> Today result <---")
print(f"--> Question : {question} <--")
print(f"--> answer : {answer} <--")
"""
# random quest generator :
"""
actions = ["Read", "Write", "Practice", "Review"]
topics = ["Python", "Math", "English", "Psychology"]
times = [10, 20, 30, 45]
action = random.choice(actions)
topic = random.choice(topics)
time = random.choice(times)
print(f"---> {action}  {topic} for {time} min <---")
"""
# Snapple facts :
"""
number = random.randint(1,6)
snapple = ['Flamingos turn pink by eating shrimp.','Honey never goes bad.','Shrimp can only swim backwards.','A taste bud s life is about 10 days.','You cant sneeze while sleeping.','Tiny pocket in jeans was for watches.']
print(f"---> fact snapple : {snapple[number]} <---")
"""
# Seasons of the year:
"""
month = int(input(">>> enter the month : "))
if month == 1 or month == 2 or month == 3:
    print("Winter 🌨️")
elif month == 4 or month == 5 or month == 6:
    print("Spring 🌱")
elif month == 7 or month == 8 or month == 9 :
    print("Summer 🌻")
elif month == 10 or month == 11 or month == 12 :
    print("Autumn 🍂")
else:
    print("Invlid")
"""


