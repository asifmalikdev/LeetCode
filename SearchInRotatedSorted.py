class Solution(object):
    def search(self, nums):
        left, right = 0, len(nums)-1
        while left<right:
            mid = (left + right)//2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return nums[mid]
            elif nums[mid-1] < nums[mid] < nums[mid+1]  :
                right = mid-1

            elif nums[mid+1]>nums[mid] > nums[mid-1]:
                left = left+1
        return 0
            


    




obj = Solution()
nums = [0,2,1,0]
target = 2
print(obj.search(nums))

