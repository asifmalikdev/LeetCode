class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                print(nums[i:j])
                if sum(nums[i:j]) == goal:
                    counter +=1
        return counter
    
nums = [0,0,0,0,0]
goal = 0
obj = Solution()
print(obj.numSubarraysWithSum(nums, goal))