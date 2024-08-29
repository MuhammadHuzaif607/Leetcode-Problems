from collections import Counter
nums = [100,4,200,1,3,2]
num_count = Counter(nums)
seen = dict(num_count)
max_count = 0
for num in nums:
    if (num - 1) not in seen:
        count = 1
        el = num + 1
        while el in seen:
            count += 1
            el += 1
        max_count = max(count,max_count)

            

        
print(max_count)

        

