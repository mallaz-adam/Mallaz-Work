# Python Calcultor :
X = float(input(">>> enter first num : "))
Y = float(input(">>> enter second num : "))
operator = input(">>> enter operator (+,-,/,*) : ")
if operator == '+':
    result = X + Y
    print(f"---> {X} + {Y} = {result} <---")
elif operator == '-':
    result = X - Y
    print(f"---> {X} - {Y} = {result} <---")
elif operator == '/':
    if Y == 0:
        print("??? false Math calculs ???")
    else:
        result = X / Y
        print(f"---> {X} / {Y} = {result} <---")
elif operator == '*':
    result = X * Y
    print(f"---> {X} * {Y} = {result} <---")
else:
    print("---> See You fausse answer... <---")