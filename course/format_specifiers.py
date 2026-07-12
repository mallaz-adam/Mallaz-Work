# format specifiers :()
price = 3.14159
print(f"---> price : {price:.2f} <---") # this format {:.numberf} give us how many numbers after the deciamal
price = 55
print(f"---> price : {price:10} <---") # this format {:number} give space before printing the number
price = 66
print(f"---> price : {price:010} <---") # this format {:0number} will replace the spaces with 0
