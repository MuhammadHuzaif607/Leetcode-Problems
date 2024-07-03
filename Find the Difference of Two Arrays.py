nums1 = [1,2,3]
nums2 = [2,4,6]
num1 = []
num2 = []
for el in nums1:
    if el not in nums2:
        num1.append(el)

for el in nums2:
    if el not in nums1:
        num2.append(el)

print(num1,num2)