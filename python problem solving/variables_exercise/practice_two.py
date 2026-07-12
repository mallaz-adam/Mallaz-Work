#Mood Currency exchange :
print("---> Mood Currency exchange <---")
energy = float(input(">>> enter level of your energie : "))
calm = float(input(">>> enter level of your calm : "))
curiosity = float(input(">>> enter level of your curiosity  : "))
courage = float(input(">>> enter level of your courage : "))
score = 0
score += 0.3 * energy
score += 0.3 * calm
score += 0.3 * curiosity
score += 0.3 * courage
token_balance = int(score)
print(f"---> the wighted score : {score} <---")
print(f"---> the token balance : {token_balance} <---")