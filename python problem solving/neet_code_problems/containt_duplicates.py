# first method : [my answer] :
"""
--------------------------------------------------------------
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
--------------------------------------------------------------

nums = list

new = []
found = True
for num in nums:
    if num not in new:
        new.append(num)
    else:
        found = False
print(found)

"""