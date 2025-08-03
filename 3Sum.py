class Solution():
    def threeSum(self, nums):
        nums.sort()
        res =[]
        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left<right:
                total = nums[i]+ nums[left]+ nums[right]
                if total ==0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left+=1
                    while right > left and nums[right]==nums[right-1]:
                        right+=1
                    
                

                    left+=1
                    right-=1
                elif total>0:
                    right-=1
                elif total<0:
                    left+=1

        return res


        
        # temp_list = []
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         for k in range(j+1,len(nums)):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 triplet = [nums[i],nums[j],nums[k]]
        #                 if sorted(triplet) not in [sorted(x) for x in temp_list]:
        #                     temp_list.append(triplet)
        # return temp_list
nums = [-1,0,1,2,-1,-4]
obj = Solution()
print(obj.threeSum(nums))

