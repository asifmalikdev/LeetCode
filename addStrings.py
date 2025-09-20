class Solution(object):
    def addStrings(self, num1, num2):
        res1 = 0
        res2 = 0
        i = len(num1)-1
        for ch in num1:
            res1 += (ord(ch)-ord("0")) * 10**i
            i-=1
        i = len(num2)-1
        for ch in num2:
            res2 += (ord(ch)- ord("0")) * 10**i
            i-=1
        return res1 + res2
        
        

num1 = "11"
num2 = "123"

obj = Solution()
print(obj.addStrings(num1, num2))

count = 0

def increment():
    print(count)
    global count
    count += 1

increment()
print(count)
