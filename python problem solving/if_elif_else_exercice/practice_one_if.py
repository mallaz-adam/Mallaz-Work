# rating: 
print("----> Rating <----")
rating = float(input(">>> enter a rating (0-5) : "))

if rating > 4.5:
    print("Perfection")
elif rating > 4:
    print("Excellent")
elif rating > 3:
    print("Good")
elif rating > 2:
    print("Fair")
else:
    print("Poor")


