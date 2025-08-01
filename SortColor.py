class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)-1):
            temp = nums[i]
            for j in range(i+1,len(nums)):
                if temp > nums[j]:
                    temp,nums[j] = nums[j],temp

            nums[i]=temp
    


nums = [2,0,2,1,1,0]
obj = Solution()
obj.sortColors(nums)