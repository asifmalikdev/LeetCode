class Solution(object):
    def maxFrequencyElements(self, nums):
        ElementHashTable = {}
        for num in nums:
            ElementHashTable[num] = ElementHashTable.get(num, 0)+1
        res = 0
        max = 0
        for key, value in ElementHashTable.items():
            if value > max:
                max = value
                res = max
            elif value == max:
                res = res + value
        return res

        
nums = [5,1,2,2,3,1,4]
obj = Solution()
print(obj.maxFrequencyElements(nums))