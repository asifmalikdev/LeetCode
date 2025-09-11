class Solution(object):
    def summaryRanges(self, nums):   
        num = [nums[0]]
        res = ""
        fin_res =[]
        j = 0

        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                num.append(nums[i])
                print(nums[i])
            else:
                if len(num) == 1:
                    fin_res.append(f"{num[0]}")
                else:
                    fin_res.append(f"{num[0]}->{num[-1]}")
                num = [nums[i]]
                
        if len(num) == 1:
            res =  f"{num[0]}"
            fin_res.append(res)
        else:
            res =  f"{num[0]}->{num[-1]}"
            fin_res.append(res)

        return fin_res

obj = Solution()
nums = [0,1,2,4,5,7]
print(obj.summaryRanges(nums))