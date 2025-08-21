class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        current_sum = 0
        sums_freq = {0:1}
        for num in nums:
            current_sum += num
            if current_sum - k in sums_freq:
                count +=sums_freq[current_sum-k]
            sums_freq[current_sum] = sums_freq.get(current_sum, 0 ) +1
            


nums = [1,2,3]
k = 3
obj = Solution()
obj.subarraySum(nums, k)