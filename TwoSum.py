class Solution:
        # def twoSum(self,numbers,target):
        #     new_num={}
        #     for index,num in enumerate(numbers):

        #         comp=target-num
        #         if comp in new_num:
        #             return(new_num[comp],index)
        #         new_num[num]=index

        def twoSum(self, nums, target):
            print(nums)
            i=0
            j=len(nums)-1
            while j>i:
                if nums[i] + nums[j] == target:
                    print("hello")
                    return i,j
                elif nums[i] + nums[j] > target:
                    j-=1
                else:
                    i+=1

#5,2,11,7,15,2,2,45,45,23,4,2,345,6
solution=Solution()
print(solution.twoSum([5,2,11,7,15],9))
