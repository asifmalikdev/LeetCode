class Solution:
        def twoSum(self,numbers,target):
            new_num={}
            for index,num in enumerate(numbers):

                comp=target-num
                if comp in new_num:
                    return(new_num[comp],index)
                new_num[num]=index

solution=Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
