class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        left = 0
        freq = {}
        total_subarraay = 0
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right],0) + 1

            while max(freq) - min(freq) > 2:
                freq[nums[left]]-=1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1
            total_subarraay +=(right-left+1)
        return total_subarraay

nums = [2,3,5,4,2,4]
obj = Solution()
res = obj.continuousSubarrays(nums)
print(res)