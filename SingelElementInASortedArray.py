class Solution(object):
    def singleNonDuplicate(self, nums):
        for i in range(0,len(nums),2):
            if nums[i] != nums[i+1]:
                return nums[i]
                    





nums = [1,1,2,3,3,4,4,8,8]
obj = Solution()
print(obj.singleNonDuplicate(nums))