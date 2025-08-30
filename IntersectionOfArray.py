class Solution(object):
    def intersection(self, nums1, nums2):
        return [num for num in nums1 if num in nums2]
        


nums1 = [1,2,2,1]
nums2 = [2,2]
obj = Solution()
print(obj.intersection(nums1, nums2))