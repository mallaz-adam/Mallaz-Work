nums = [4,5,6]
target = 10

found_pair = []

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            found_pair.append(i)
            found_pair.append(j)
            break
print(found_pair)
print(f"{nums[found_pair[0]]} + {nums[found_pair[1]]} = {nums[found_pair[0]] + nums[found_pair[1]]}")