class Solution(object):
    def convertToTitle(self, columnNumber):
        res = ""
        while columnNumber>0:
            columnNumber-=1
            res = chr(columnNumber % 26 + ord('A')) +res
            columnNumber//=26
        return res


columnNumber = 701
obj = Solution()
print(obj.convertToTitle(columnNumber))