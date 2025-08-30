class Solution(object):
    def minimumOperations(self, nums):
        return len([n for n in set(nums) if n>0])
        

nums = [1,5,0,3,5]
obj = Solution()
print(obj.minimumOperations(nums))