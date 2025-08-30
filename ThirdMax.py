class Solution(object):
    def thirdMax(self, nums):
        nums = set(nums)
        if len(nums)>2:
            return nums[3]
        
        else:
            nums = list(nums)
            return nums[-1]
        
nums = [1,2]
[1,1,1,1,1,,2,2,2,2,2,2,3]
obj = Solution()
print(obj.thirdMax(nums))