class Solution():
    def evenGen(self, num):
        for n in range(1,num//2 +1):
            yield n*2


obj = Solution()

res = obj.evenGen(10000)

while True:
    print(next(res))
    ans = input("Y for Next number").strip().lower()
    if ans != "y":
        break