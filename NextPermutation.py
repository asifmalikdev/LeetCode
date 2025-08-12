class Solution(object):
    def nextPermutation(self, nums):
        temp = nums[:]  # copy original order
        sorted_nums = sorted(nums)  # sorted starting point
        
        temp1 = []
        found_original = False
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if i != j and j != k and k != i:
                        current_perm = [sorted_nums[i], sorted_nums[j], sorted_nums[k]]
                        if found_original:
                            nums[:] = current_perm
                            return
                        if current_perm == temp:
                            found_original = True
        
        nums[:] = sorted_nums
        return nums
        

obj = Solution()
nums = [1,2,3]
print(obj.nextPermutation(nums))