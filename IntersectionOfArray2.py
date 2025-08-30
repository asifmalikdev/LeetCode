class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        seen = {}
        for num in nums1:
            seen[num] = seen.get(num, 0)+1
        res = []
        for num in nums2:
            if num in seen and seen[num]>0:
                seen[num]-=1
                res.append(num)
        return res
        


nums1 = [1,2,2,1]
nums2 = [2,2]
obj = Solution()
print(obj.intersect(nums1, nums2))