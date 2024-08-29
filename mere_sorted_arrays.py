nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
i = 0
j = 0
while i < m and j < n:
    if nums1[i] == nums2[j]:
        nums1.insert(i,nums2[j])
        j += 1
        i += 2
        nums1.pop()
    elif nums1[i] > nums2[j]:
        j += 1
    elif nums1[i] < nums2[j]:
        i += 1
else:
    if j < n:
        for index in range(i+1,m+n):

            nums1[index] = nums2[j]
            j += 1
    
   
        

print(nums1)
