class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()
        return (nums[-1] * nums[-2] - nums[1] * nums[0])



nums = [4,2,5,9,7,4,8]
obj = Solution()
print(obj.maxProductDifference(nums))