class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        counter = 0
        for num1 in arr1:
            condition = True
            for num2 in arr2:
                if abs(num1-num2)  <= d:
                    condition = False
                    break

            if condition:
                counter += 1
        return counter 


arr1 = [4,5,8]
arr2 = [10,9,1,8]
d = 2
obj = Solution()
print(obj.findTheDistanceValue(arr1, arr2, d))