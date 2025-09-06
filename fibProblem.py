class Solution:
    def fibSeries(self, num):
        a, b = 0, 1
        for _ in range(num):
            yield a   # yield one number at a time
            a, b = b, a + b

obj = Solution()
num = 10000
fib = obj.fibSeries(num)


temp = True
while True:
    print(next(fib))
    choice = input("do you want to continue? y/n").strip().lower()
    if choice!="y":
        break
