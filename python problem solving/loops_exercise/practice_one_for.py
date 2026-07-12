# loops practices:
# exercise:
"""
n = int(input(">>> entrer la taille : "))

for x in range(n):
    for y in range(n):
        if y < x:
            print(y + 1, end="")
    print()
"""
# exercise :
"""
n = int(input(">>> entrer la taill : "))

for x in range(n):
    for y in range(n - x):
        print("#", end="")
    print()
"""
# exercise :
"""
n = int(input(">>> enter the number you want to do factorial : "))

multi = 1
for x in range(2,n + 1):
   multi *= x

print(f"---> factorial of {n} is {multi} <---")
"""
# exercise : word analyser :
"""
word = input(">>> enter a sentence : ")

characters = len(word)

vowels = "aeiouAEIOU"
spaces = 0
vowels_counter = 0
uppercase_counter = 0
lowercase_counter = 0
digits_counter = 0

for char in word :
    if char == " ":
        spaces += 1
    
    if char in vowels:
        vowels_counter += 1
    
    if char.isupper():
        uppercase_counter += 1
    
    if char.islower():
        lowercase_counter += 1
    
    if char.isdigit():
        digits_counter += 1

split_words = word.split()
words_counter = 0

for word in split_words:
    words_counter += 1

print(f"---> characters : {characters} <---\n---> number of spaces : {spaces} <---\n---> vowels counter : {vowels_counter} <---\n---> upper case : {uppercase_counter} <---\n---> lower case : {lowercase_counter} <---\n---> digits counter : {digits_counter} <---\n---> number of words : {words_counter} <---")
"""
# exercise : 








