# Grade analyser :
"""
def calculet_average(N1,N2,N3):
    return (N1 + N2 + N3) / 3

def get_grade_status(average):
    if average >= 16:
        return "Excellent"
    elif average >= 12:
        return "Good"
    elif average >= 10:
        return "Pass"
    else:
        "Fail"
    

print("-----------------------------")
print("----> Grade analyser <----")
print("-----------------------------")
N1_grade = float(input(">>> enter the first grade : "))
N2_grade = float(input(">>> enter the second grade : "))
N3_grade = float(input(">>> enter the third grade : "))
while N1_grade < 0 or N1_grade > 20 or N2_grade < 0 or N2_grade > 20 or N3_grade < 0 or N3_grade > 20 :
    print("??? Oops ,Wrong input ???")
    N1_grade = float(input(">>> enter the first grade : "))
    N2_grade = float(input(">>> enter the second grade : "))
    N3_grade = float(input(">>> enter the third grade : "))

print(f"---> Average : {calculet_average(N1_grade,N2_grade,N3_grade)} <---")
print(f"---> Status : {get_grade_status(calculet_average(N1_grade,N2_grade,N3_grade))} <---")
"""
# Mood transltor:
"""
positive_words = ["happy", "safe", "calm", "good", "hopeful", "strong"]
negative_words = ["sad", "tired", "angry", "lost", "stressed", "afraid"]
def count_positive_words(sentence):
    sentence_split = sentence.split()
    count = 0
    for word in sentence_split:
        if word in positive_words:
            count += 1
    return count

def count_negative_words(sentence):
    sentence_split = sentence.split()
    count = 0
    for word in sentence_split:
        if word in negative_words:
            count += 1
    return count

def get_mood_type(positive_count, negative_count):
    if positive_count > negative_count:
        return "Positive mood"
    elif positive_count < negative_count:
        return "Nigatve mood"
    else:
        return "Mixed mood"

# programm start :
print("----------------------------------")
print("----> Mood analyser <----")
print("----------------------------------")
sentence = input(">>> enter a sentence : ").lower()

positive_word = count_positive_words(sentence)
negative_word = count_negative_words(sentence)
print(f"---> negative words {negative_word} - positive word : {positive_word} <---")
print(f"---> Your mood is : {get_mood_type(positive_word,negative_word)} <---")
"""
# Mini Drive - Thru Order system:
"""
order = []
total = []
def Welcome():
    print("--------------------------------")
    print("----> Mallaz Noise <----")
    print("--------------------------------")

def Menu():
    print("---> Menu <---")
    print("--> 1. Burger - 40 MAD <--")
    print("--> 2. Fries - 15 MAD <--")
    print("--> 3. Soda - 10 MAD <--")
    print("--> 4. Ice Cream - 12 MAD <---")
    print("--> 5. Chicken Wrap - 35 MAD <--")

def take_order(item_name,price):
    print("-----------------------------------------------------")
    print("---> Taking order <---")
    print(f"---> Item : {item_name} - price : {price} <---")
    items = int(input(">>> enter how many item you want to take : "))
    while items <= 0:
        print("??? Oops , Wrong Input ???")
        items = int(input(">>> enter how many item you want to take : "))
    price_total = price * items
    if item_name in order:
        index_order = order.index(item_name)
        total[index_order] += price_total
    else:
        order.append(item_name)
        total.append(price_total)
    print(f"---> Your order was complete ${price_total} Is added <---")

    print("-----------------------------------------------------")

def show_receipt(total_order,total_prices):
    print("-----------------------------------------------------")
    print("---> Recipt <---")
    if len(total_order) == 0:
        print("---> Total items : 0 <---")
        print("---> total price : 0 <---")
    else:
        print("--> items in the recipt<--")
        print("==============================================")
        for i in range(len(total_order)):
            print(f"---> item {i + 1} : {total_order[i]} - price : {total_prices[i]} <---")
        print("==============================================")
        print(f"---> Total items : {len(total_order)} ",end="")
        print(f"- Total Price : {sum(total_prices)} <---")
    print("-----------------------------------------------------")

Welcome()
while True:
    print("---> Starting Menu <---")
    print("--> 1. Show Menu <--")
    print("--> 2. show recipt <--")
    print("--> 0. Exit <--")
    choice = int(input(">>> enter your choice : "))
    match choice:
        case 1:
            Menu()
            choice = int(input(">>> enter your choice : "))
            match choice:
                case 1:
                    item_name = "Burger"
                    item_price = 40
                    take_order(item_name,item_price)
                case 2:
                    item_name = "Fries"
                    item_price = 15
                    take_order(item_name,item_price)
                case 3:
                    item_name = "Soda"
                    item_price = 10
                    take_order(item_name,item_price)
                case 4:
                    item_name = "Ice Cream"
                    item_price = 12
                    take_order(item_name,item_price)
                case 5:
                    item_name = "Chicken Warp"
                    item_price = 40
                    take_order(item_name,item_price)
                case _:
                    print("??? Invalid Choice ???")
        case 2:
            show_receipt(order,total)
        case 0:
            print("---> Thank You <---")
            break
print("--------------------------------")
"""
        





