class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for index,num in nums:
            if num in nums and index - seen[nums] <= k:
                return True
            seen[nums]=index
        return False

        




nums = [1,2,3,1]n
k = 3
obj = Solution()
obj.containsNearbyDuplicate(nums, k)