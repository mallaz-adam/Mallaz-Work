# sequence :
"""
prv1 = 0
prv2 = 1
print(prv1)
print(prv2)

for i in range(18):
    new_num = prv1 + prv2
    print(new_num)
    prv1 = prv2
    prv2 = new_num
"""
# exercise :
"""
n = int(input(">>> enter a number : "))
prv1 = 0
prv2 = 1
sum = 0

for i in range(n - 1):
    sum += prv1 + prv2
    prv1 = prv2
    prv2 = sum
print(sum)
"""

