class Solution(object):
    def titleToNumber(self, columnTitle):
        res =  0
        for i in range(len(columnTitle)):
            res += ((ord(columnTitle[i])-64) * (26**(len(columnTitle)-i-1)))
        return res




columnTitle = "AAA"
obj = Solution()
print(obj.titleToNumber(columnTitle))

temp = "hello"

if (temp == "malik") or "hey":
    print("asif malik")
else:
    print("error")