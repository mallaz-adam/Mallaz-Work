# racping old :
"""
sentence = input(">>> enter a sentence : ").lower()
sentence_splited = sentence.split()

# mood checker :
for word in sentence_splited:
    if word == "happy" or word == "good" or word == "amazing":
        print(f"---> great to hear that and see that you are feeling {word} <---")
    
    if word == "sad" or word == "bad" :
        print(f"---> Hope that you will be good soon , and try to fill your time that you enjoy <---")
# analyse the sentence :
print(f"---> your sentence has : {len(sentence)} character <---")
count = 0
for word in sentence_splited:
    count += 1
print(f"---> your sentence has : {count} word <---")
"""
# list practices :
# practice 1 :
"""
scores = [10, 15, 20, 15, 12, 15, 9]
count_15 = scores.count(15)
index_first_20 = scores.index(20)
find_18 = True if 18 in scores else False
print(f"---> number of 15 is : {count_15} <---")
print(f"---> first index of 20 : {index_first_20} <---")
print(f"---> theres any 18 in list ? : {find_18} <---")
"""
# practice 2:
"""
cart = ["milk", "bread", "eggs"]
cart.append("chesse")
cart.remove("bread")
cart.pop()
print("---> Items in cart <---")
count = 0
for i , item in enumerate(cart, start = 1) :
    print(f"---> item {i} : {item} <---")
    count += 1
print(f"---> Items left in cart are : {count} <---")
"""
# practice 3:
"""
grades = [8, 14, 17, 20, 11, 6, 19]
grades.sort()
print(f"---> Highest grade : {max(grades)} <---")
print(f"---> lowest grade : {min(grades)} <---")
print(f"---> Top three grades : {grades[-3:]} <---")
print(f"---> lowest three grades : {grades[:3]} <---")
"""
# exercise 4:
"""
temps = [18, 20, 21, 19, 23, 25, 22]
temps.sort()
average = sum(temps) / len(temps)
print(f"---> highest temprature : {temps[-1]} <---")
print(f"---> lowest temprature : {temps[0]} <---")
print(f"---> last three days temprature : {temps[-3:]} <---")
print(f"---> first three days temprature : {temps[:3]} <---")
print(f"---> revesed temperature : {temps[::-1]} <---")
"""
