class Solution(object):
    def findDisappearedNumbers(self, nums):   
        nums_range = set(range(1,len(nums)+1))
        nums = set(nums)
        missing = list(nums_range-nums)
        return missing
    

nums = [7,4,3,2,7,8,2,3,1]
obj = Solution()
print(obj.findDisappearedNumbers(nums))