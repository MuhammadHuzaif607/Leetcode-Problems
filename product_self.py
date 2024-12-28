nums = [-1,1,0,-3,3]
prefix = []
suffix = []
out = []
pr = 1
sr = 1
for num in nums:
    pr *= num
    prefix.append(pr)
    
for num in nums[::-1]:
    sr *= num
    suffix.append(sr)
    
suffix.reverse()

out.append(suffix[1])
for i in range(1,len(nums) - 1):
    pr = prefix[i - 1]
    sr = suffix[i + 1]
    out.append(pr*sr)
    
out.append(prefix[-2])
print(out)
    
    
    
    

    
    
    