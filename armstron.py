class Solution():
    def armstrong(self, num):
        n = len(str(num))
        temp = num
        print(n)
        total = 0
        while num > 0:
            total = total + (num%10)**n
            num = num // 10
        return total == temp


num = 123
num1 = 153
num2 = 371
obj = Solution()
print(obj.armstrong(num))
print(obj.armstrong(num1))
print(obj.armstrong(num2))