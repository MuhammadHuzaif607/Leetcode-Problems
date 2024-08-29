nums = [1,2,3,4]
prefix = []
suffix = [0] * len(nums)
prefix_num = 1
suffix_num = 1

for num in nums:
    prefix_num *= num
    prefix.append(prefix_num)

for index in reversed(range(len(nums))):
    pass
    