from collections import defaultdict

nums = [2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2]
k = 3
dict1 = defaultdict(int)
pairs = 0

for el in nums:
    diff = k - el
    if dict1[diff] > 0:
        pairs += 1
        dict1[diff] -= 1
    else:
        dict1[el] += 1

print(pairs)
