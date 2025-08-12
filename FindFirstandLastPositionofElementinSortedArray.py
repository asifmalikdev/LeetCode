class Solution(object):
    def searchRange(self, nums, target):
        left, right = 0, len(nums)-1
        if len(nums) == 1 and target == 1:
            return 0,0
        if len(nums) == 1 and target != 0:
            return -1,-1
        while left<right:
            mid = (left+right)//2
            if nums[mid] == target:
                if nums[mid+1] == nums[mid]:
                    return mid, mid+1
                else:
                    return mid-1, mid
            elif target > nums[mid]:
                left = mid+1
            
            else:
                right = mid-1
        return -1,-1

nums= [5,7,7,8,8,10]
target = 8
obj = Solution()
print(obj.searchRange(nums, target))