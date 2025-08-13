class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return True
            if nums[left] == target or nums[right] == target:
                return True

            while left < mid and nums[left] == nums[mid]:
                left += 1

            while right > mid and nums[right] == nums[mid]:
                right -= 1

            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid +1
                else:
                    right = mid-1
        return False




nums = [1,0,1,1,1]
target = 0
obj = Solution()
print(obj.search(nums, target))