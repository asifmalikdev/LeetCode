def yieldSimpleFunction():
    for j in range(3,11):
        yield j

ans = yieldSimpleFunction()

while True:
    print(next(ans))
    condition = input("Enter Y for next or anyother key to terminate").strip().lower()
    if condition != "y" :
        break

class Solution():
    def fibSeries(self, num):
        a = 0
        b = 1
        

