class Solution(object):
    def search(self,nums, target):
        low,high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                low = mid+1
            else:
                high = mid-1
        return -1






obj = Solution()
print(obj.search([-1,0,3,5,9,12],0))
