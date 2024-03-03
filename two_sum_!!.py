numbers = [2,7,11,15]
target = 9
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum > target:
                right -=1
            elif sum < target:
                left += 1
            elif sum == target:
                return [left+1,right+1]
        