nums = [1,3,5,6]
target = 7
start = 0
end = len(nums) - 1
while start <= end:
    mid = (start + end) // 2
    if target == nums[mid]:
        print(mid)
        break
    elif target > nums[mid]:
        start = mid + 1
    else:
        start = mid + 1
        end = mid - 1

else:
    print(mid,start,end)