class Solution(object):
    def majorityElement(self, nums):
        count = 0
        cand = nums[0]
        for num in nums:
            if count==0:
                cand = num
            if cand == num:
                count+=1
            else:
                count-=1
        return cand



obj = Solution()
print(obj.majorityElement([3,2,3,2,3,2,3]))
