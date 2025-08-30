class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
        




nums =  [1,1,1,3,3,4,3,2,4,2]
obj = Solution()
print(obj.containsDuplicate(nums))

nums = [1,1,1,3,3,4,3,2,4,2]

num = set(nums)
print(num)