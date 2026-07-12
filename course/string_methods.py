# strings methodes and indexing :
"""
==> len() : gives the length of an string
==> variable.strip() : remove uselles spaces
==> variable.isdigit() : return an boolean that show if the variable have only digits
==> variable.isalpha() : return an boolean that show if the variable have only alphabets
==> variable.count(char) : return an int value that indicate how many an character has appear
==> variable.upper()/lower() : it return the string upper or lower case 
"""
#example :
"""
username = input(">>> enter your username : ")
find = username.find(" ")
if len(username) > 12:
    print("??? username is no more than 12 character ???")
elif find > 0:
    print("??? username most not contain spaces ???")
elif not username.isalpha():
    print("??? username most not containt digits ???")
else:
    print(f"---> Welcome {username} <---")
"""

# string indexing : indexing is accessing element of a sequence using [Start : end : step]
credit_number = "1122-1234-5666-7895"
# printing characters :
"""
print(credit_number[0])
print(credit_number[2])
print(credit_number[5])
print(credit_number[1])
"""
# printing from a starting point to an ending point :
"""
print(credit_number[0:4])
print(credit_number[5:9])
print(credit_number[:5]) #this form will start from zero to a point or index to the index uou want to finish at
print(credit_number[5:]) #this form will start from an index to the finish of the string
"""
# printing including steps :
"""
print(credit_number[::2])
print(credit_number[::3])
"""
# example of an useful program:
"""
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")
"""
#email_slicer_program:
"""
email = input(">>> enter your email : ")
index = email.index("@")
username = email[:index]
domain = email[index + 1:]
print("---> email important informations <---")
print(f"--> user name : {username} <--")
print(f"--> email domain : {domain} <--")
"""



