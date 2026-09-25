from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = 0
        count = 0
        seen = {0:1}
        for num in nums:
            current_sum += num
            compliment = current_sum - k
            if compliment in seen:
                count += seen[compliment]
            seen[current_sum] = seen.get(current_sum,0) + 1
        return count
        



nums = [1, 2, 2,1, 2]
k = 3
obj = Solution()
res = obj.subarraySum(nums,k)
print(res)