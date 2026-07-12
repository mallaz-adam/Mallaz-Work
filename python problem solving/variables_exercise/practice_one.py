#Signal Card :
sender_name = input(">>> enter sender name : ")
year = int(input(">>> enter the year of the message : "))
urgency = input(">>> enter the urgency : ")
message = input(">>> enter the message : ")
years_difference = year - 2026
print("---------------------------------------")
print(f"---> sender name : {sender_name} - year : {year} <---\n")
print(f"---> urgency : {urgency} <---")
print("---> Message <---")
print(message)
print("\n")
print(f"---> years difference ( 2026 - {year} ) : {years_difference} <---")


