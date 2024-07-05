nums = [1,2,3,1,2,3]
k = 2
dict1 = {}
for index in range(len(nums)):
    if nums[index] in dict1:
        if abs(index - dict1[nums[index]]) <= k:
            print(True)
        else:
            dict1[nums[index]] = index
        print(dict1[nums[index]],index)
    else:
        dict1[nums[index]] = index
        
print(dict1)

        

        


