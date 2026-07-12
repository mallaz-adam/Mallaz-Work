# Echo Pattern Decoder :
word = input(">>> enter a random password : ")

cleaned = ""
vowels = "aeiouAEIOU"
vowels_counter = 0
digits = 0
letters = 0
unusual = 0

for char in word:
    if char in vowels:
        vowels_counter += 1
        cleaned += char

    
    elif char.isdigit():
        digits += 1
        cleaned += char
    
    elif  char.isalpha():
        letters += 1
        cleaned += char
    else:
        unusual += 1
    
print(f"Original: {word}")
print(f"Vowels: {vowels_counter}")
print(f"Digits: {digits}")
print(f"Letters: {letters}")
print(f"Unusual: {unusual}")
print(f"Cleaned: {cleaned}")
    

