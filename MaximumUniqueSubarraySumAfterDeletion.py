class Solution(object):
    def maxSum(self, nums):
        if max(nums) < 0:
            return max(nums)
        dict1 = {}
        res = 0
        for num in nums:
            if num > 0 and num not in dict1.keys():
                res = res + num
                dict1[num] = dict1.get(num, 0) + 1

        return res
    
nums = [1,2,3,4,5]
obj = Solution()
print(obj.maxSum(nums))