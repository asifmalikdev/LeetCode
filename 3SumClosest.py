class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res_total = nums[0]+nums[1] + nums[2]
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total = 



nums = [-1,2,1,-4]
target = 1
obj = Solution
obj.threeSumClosest(nums, target)