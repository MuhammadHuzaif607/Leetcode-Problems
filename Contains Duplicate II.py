nums = [1,0,1,1]
k = 1
dict1 = {}
for el in range(len(nums)):
    if nums[el] in dict1:
        if (abs(dict1[nums[el]] -  el) <= k) and (nums[el] == nums[dict1[nums[el]]]):
            print(True)
        
    else:
        dict1[nums[el]] = el