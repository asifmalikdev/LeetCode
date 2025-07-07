class Solution:
        # def twoSum(self,numbers,target):
        #     new_num={}
        #     for index,num in enumerate(numbers):

        #         comp=target-num
        #         if comp in new_num:
        #             return(new_num[comp],index)
        #         new_num[num]=index

        def twoSum(self, nums, target):
            i=0
            j=len(nums)-1
            while j>i:
                print("asif",i,j)
                if nums[i] + nums[j] == target:
                    return i,j
                elif nums[i] + nums[j] > target:
                    j-=1
                else:
                    i+=1
                    print("hello")






solution=Solution()
print(solution.twoSum([3,2,4],6))
