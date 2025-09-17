class Solution(object):
    def findDuplicates(self, nums):
        res = []
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else:
                res.append(num)
        return res


nums = [4, 3, 2, 7, 8, 2, 3, 1]
obj = Solution()
print(obj.findDuplicates(nums))
