class Solution(object):
    def addStrings(self, num1, num2):
        i = len(num1)-1
        j = len(num2)-1
        carry = 0
        res = ""
        temp = ""
        while i > -1 or j > -1 or carry:
            d1 = ord(num1[i]) - ord("0") if i >= 0  else 0
            d2 = ord(num2[j]) - ord("0") if j >= 0 else 0

            total = d1 + d2 + carry

            carry = total // 10
            digit = total % 10

            res = chr(ord("0") + digit ) + res

            i-=1
            j-=1
        return res



num1 = "11"
num2 = "123"
obj = Solution()
print(obj.addStrings(num1, num2))