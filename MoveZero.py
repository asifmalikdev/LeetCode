class Solution(object):
    def moveZeroes(self, nums):
        pos =  0    
        for num in nums:
            if num != 0:
                nums[pos] = num
                pos+=1
        for i in range(pos, len*nums):
            nums[i]=0
                
        return nums


nums = [0,1,0,3,12]
obj = Solution()
print(obj.moveZeroes(nums))