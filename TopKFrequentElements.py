class Solution(object):
    def topKFrequent(self, nums, k):
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]] = dict1.get(nums[i], 0) + 1

        sorted_items = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
        res = [item[0] for item in sorted_items[:k]]
        return res

nums = [3,2,1,1,1,2,2,3,2,2]
k = 2
obj = Solution()
print(obj.topKFrequent(nums, k))