class Solution(object):
    def maximumSubarraySum(self, nums, k):
        n = len(nums)
        left = 0
        win_sum = 0
        max_sum = 0
        seen={}
        for right in range(n):
            print(max_sum)
            win_sum +=nums[right]
            seen[nums[right]] = seen.get(nums[right], 0)+1

            while right-left +1 > k:
                win_sum = win_sum - nums[left]
                seen[nums[left]]-=1
                if seen[nums[left]] == 0:
                    del seen[nums[left]]
                left+=1
             
            if right-left+1 == k and len(seen) == k:
                max_sum = max(max_sum , win_sum)                             
            
        return max_sum

nums = [9,9,9,8,8,8,1,5,4,2,4,9,9,9]
k = 3
obj = Solution()
print(obj.maximumSubarraySum(nums, k))