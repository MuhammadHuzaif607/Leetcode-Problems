height = [1,1]
i = 0
j = len(height) - 1

def area(lst1,lst2):
    width = abs(lst2[0] - lst1[0])
    height = min(lst1[1],lst2[1])
    
    return width * height

max_area = 0
while i < j :
    cur_area = area([i,height[i]],[j,height[j]])
    max_area = max(max_area,cur_area)
    if height[i] < height[j]:
        i += 1
    elif height[i] > height[j]:
        j -= 1
    elif height[i] == height[j]:
        i += 1
        j -= 1
        
        
print(max_area)
    
    
    