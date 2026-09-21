from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums


nums = [1,1,1,1,1]
obj = Solution()
print(obj.runningSum(nums))

for i in range(2):
    print(i)