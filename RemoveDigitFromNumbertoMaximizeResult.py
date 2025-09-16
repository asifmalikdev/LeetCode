class Solution(object):
    def removeDigit(self, number, digit):
        res = ""
        for i,ch in enumerate(number):
            if ch == digit:
                temp = number[:i] + number[i+1:]
                if temp > res:
                    res = temp

        return res
        


number = "1231"
digit = "1"
obj = Solution()
print(obj.removeDigit(number, digit))