class Solution(object):
    def pivotIndex(self, nums):
        t_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if t_sum-left_sum-num == left_sum:
                return i
            left_sum +=num
        return -1
            

        





nums = [1,7,3,6,5,6]
obj = Solution()
print(obj.pivotIndex(nums))

nums = [1,2,3]
obj = Solution()
print(obj.pivotIndex(nums))

nums = [2,1,-1]
obj = Solution()
print(obj.pivotIndex(nums))
