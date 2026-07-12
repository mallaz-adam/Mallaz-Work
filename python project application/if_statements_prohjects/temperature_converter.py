# Python temperature converter:
print("---> Temperature converter <---")
unit = input(">>> Unit of the temperature (C / F) ? : ").lower()
temp = float(input(">>> enter the temperature : "))

if unit == 'c':
    result = (temp * 9/5) + 32
    print(f"---> The temperature in Fahrenheit is : {result} F <---")
elif unit == 'f':
    result = (temp - 32) * 9/5
    print(f"---> The temperature in Celsuis is : {result} C <---")
else:
    print(f"---> {unit} is an invalide unit of measurement <---")