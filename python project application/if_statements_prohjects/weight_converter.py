#Python weight converter :
print("---> Weight converter <---")
weight = float(input(">>> enter your weight : "))
unit = input(">>> enter the unit you are using (K/P) : ").lower()
if unit == 'k':
    result =  weight * 2.205
    unit = 'lbs'
elif unit == 'p':
    result = weight / 2.205
    unit = 'Kgs'
else:
    print(f"??? False Unit {unit} ???")
    result = 0


print(f"---> Your weight is {round(result)} {unit} <---")


