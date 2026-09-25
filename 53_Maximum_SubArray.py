from typing import List
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            
            if current_sum < 0:
                current_sum = 0
        return max_sum       



nums = [-2,1,-3,4,-1,2,1,-5,-3,4,9]
obj = Solution()
res = obj.maxSubArray(nums)
print(res)