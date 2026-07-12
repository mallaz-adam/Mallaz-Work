# practice string indexing :
# practice 1:
"""
word = "   hEllo,,,   my NAME is Adam!!! i love   Python???   "
new_word = word.strip()
new_word = new_word.replace("  "," ")
new_word = new_word.title()
print(new_word)
separated_words = new_word.split()
# character count :
count_char = 0
count_word = 0
count_special_char = 0
for char in new_word:
    if char != " ":
        count_char+= 1
    if char in [".","?",",","!"]:
        count_special_char += 1
for word in separated_words:
    count_word += 1

print(f"---> new word : {new_word} <---")
print(f"---> Number of characters : {count_char} <---")
print(f"---> Number of words : {count_word} <---")
print(f"---> sepcial characters : {count_special_char} <---")
"""
# practice 2:
"""
user_name = input(">>> enter a user name : ")

print(f"---> first character : {user_name[0]} <---")
print(f"---> last character : {user_name[-1]} <---")
print(f"---> first character is an letter : {"Yes" if user_name[0].isalpha() else "No"} <---")
print(f"---> last character is an digit : {"Yes" if user_name[-1].isdigit() else "No"} <---")
print(f"---> the username contain [ _ ] ? : {"Yes" if "_" in user_name else "No"} <---")
print(f"---> first three characters : {user_name[:4]} <---")
print(f"---> last three characters : {user_name[-3:]} <---")
print(f"---> revesed word : {user_name[::-1]} <---")
"""
# practice 3:
"""
email = "mallazadam64@gmail.com"

char_index = email.index("@")
print(f"---> Name in email : {email[:char_index]} <---")
print(f"---> Domain in email : {email[char_index + 1:]} <---")
print(f"---> first character : {email[0]} <---")
print(f"---> last character : {email[-1]} <---")
for i in range(len(email)):
    if i == 0 or i == len(email) - 1:
        print(email[i],end="")
    else:
        print("*",end="")
"""
# practice 4 [small project : Hidden Word]:
"""
secret_word = "python"
count = 0
char_found = ""
max_attempts = 6
while max_attempts > 0:
    user_hint_char = input(">>> enter a character in the hind word : ").lower().strip()
    if user_hint_char in char_found:
        print("---> this character was already founded <---")
        continue

    if user_hint_char in secret_word:
        print("---> Correct <---")
        char_found += user_hint_char
    else:
        max_attempts -= 1
        print("---> This character is not found <---")
        print(f'--> attempts left : {max_attempts} <--')
        

    all_found = True

    for word in secret_word:
        if word in char_found:
            print(word,end="")
        else:
            print("_",end="")
            all_found = False
    print("\n")
    
    if all_found:
        print(f"---> founded !! Correct word : {secret_word} <---")
        break
if max_attempts == 0:
    print("??? Oops , you don t have enough attempts ???")
"""

