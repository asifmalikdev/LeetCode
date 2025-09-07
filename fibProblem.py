class Solution:
    def fibSeries(self, num):
        a, b = 0, 1
        for _ in range(num):
            yield a   
            a, b = b, a + b

obj = Solution()
num = 100000
fib = obj.fibSeries(num)


temp = True
while True:
    print(next(fib))
    choice = input("do you want to continue? y/n").strip().lower()
    if choice!="y":
        break
