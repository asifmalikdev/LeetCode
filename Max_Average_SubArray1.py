class Solution(object):
    def findMaxAverage(self, nums, k):
        win_sum = 0
        max_sum = 0
        start = 0
        for end in range(len(nums)):
            win_sum += nums[end]
            
            if end - start + 1 == k:
                if win_sum > max_sum:
                    max_sum = win_sum
                win_sum -= nums[start]
                start+=1
        return max_sum/k
    

nums = [1,12,-5,-6,50,3]
k = 4
obj = Solution()
print(obj.findMaxAverage(nums, k))


nums = [5]
k = 1
obj = Solution()
print(obj.findMaxAverage(nums, k))