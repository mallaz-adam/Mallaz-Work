# the door of maybe :

courage = int(input(">>> enter the level of courage (0 - 10) : "))
while courage < 0 or courage > 10:
    print("??? the value is not correct ???")
    courage = int(input(">>> enter the level of courage (0 - 10) : "))

curiostiy = int(input(">>> enter the level of curiostiy (0 - 10) : "))
while curiostiy < 0 or curiostiy > 10:
    print("??? the value is not correct ???")
    curiostiy = int(input(">>> enter the level of curiositiy (0 - 10) : "))

hours = int(input(">>> enter the number of hours : "))
while  hours < 0 or hours > 23:
    print("??? the value is not right ???")
    hours = int(input(">>> enter the number of hours : "))

if courage <= 3:
    print("---> Door stays closed because is too low <---")
elif courage >= 8 and hours >= 20:
    print("---> Iron door opens <---")
elif curiostiy >= 8:
    print("---> Blue Door opens <---")
elif courage >= 6 and curiostiy >= 6:
    print("---> Golden door opens <---")
elif hours < 6:
    print("---> Shadow door opens <---")
else:
    print("---> Wooden door opens <---")

