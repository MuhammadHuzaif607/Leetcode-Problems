nums = [0,1,2,4,5,7]
ranges = []
first = nums[0]
passed = 0
for el in range(len(nums) - 1):
   if nums[el] == nums[el+1] - 1:
      passed += 1
   elif nums[el] != nums[el+1] - 1 and passed > 1:
      ele = str(first) + "->" + str(nums[el])
      ranges.append(ele)
      first = nums[el+1]
      passed = 0
   elif nums[el] != (nums[el+1] - 1)  and passed == 0:
      ranges.append(str(nums[el+1]))
print(ranges,passed)      
   



      
      
      
        
     
    


