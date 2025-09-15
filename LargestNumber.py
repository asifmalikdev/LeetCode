class Solution(object):
    def largestNumber(self, nums):
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x*10, reverse=True)
        result = ''.join(nums)
        return '0' if result[0] == '0' else result
        
        
        



nums = ["3","30","34","5","9"]
obj = Solution()
print(obj.largestNumber(nums))