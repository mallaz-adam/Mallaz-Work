# coder and decoder
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("===================================")
print("===== Coder and decoder systeme ====")
print("===================================")
while True :
    print("--------------------------------------------")
    print("---> Menu <---")
    print("--> 1. coder <--")
    print("--> 2. decoder <--")
    print("--> 0. exit <--")
    choice = int(input(">>> enter your choice : "))
    if choice == 1:
        words = input(">>> enter a word : ").lower()

        coder = ""
        for word in words:
          if word in alphabet: 
             index = alphabet.find(word)
             if word == "z":
               new_word = "a"
             else:
               new_word = alphabet[index + 1]
               coder += new_word + "_"
          elif word == " ":
             coder += "/"
          else:
             coder += word

        print(f"---> The new code : {coder} <---")
    elif choice == 2:
        words = input(">>> enter the world you want to decode : ").lower()
        decoder = "" 

        for word in words:
           if word in alphabet:
             index = alphabet.find(word)
             if word == "a":
               new_word = "z"
             else:
               new_word = alphabet[index - 1]
    
             decoder += new_word
           elif word == "/":
              decoder += " "
           else:
              continue
         
        print(f"---> decoded code is : {decoder} <---")
    elif choice == 0:
        print("----> Thank you for using our systeme <----")
        break
print("--------------------------------------------")
print("===================================")
"""
# revese odd positions :
"""
words = input(">>> enter a sentence : ")
splited_words = words.split()
new_word = ""
for i in range(len(splited_words)):
    word = splited_words[i]
    if i % 2 != 0:
        reversed_word = word[::-1]
        new_word += reversed_word + " "
    else:
        new_word += word + " "
print(f"---> The new word : {new_word} <---")
"""

   
