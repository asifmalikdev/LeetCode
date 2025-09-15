class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers)-1
        while l<r:
            num = numbers[l] + numbers[r]
            if num == target:
                return [l+1, r+1]
            if num < target:
                l+=1
            if num > target:
                r-=1
        



nums = [1,2,3]
obj = Solution()        
print(obj.permute(nums))