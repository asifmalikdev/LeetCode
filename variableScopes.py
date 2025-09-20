class Solution():
    def new_fun(self, num, nums):
        num = num + 5
        print(num, id(num))
        # nums = nums*5
        # print(nums, id(nums))
        nums = [x*5 for x in nums]
        print(nums, id(nums))



num = 5
nums = [1, 2, 3]
print(num, id(num))
print(nums, id(nums))
obj = Solution()
obj.new_fun(num, nums)
print(num)
print(nums, id(nums))