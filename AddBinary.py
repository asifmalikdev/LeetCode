class Solution():
    def addBinary(self, a, b):
        left = len(a) - 1
        right = len(b) - 1
        res = []
        rem = 0

        while left > -1 or right > -1:
            temp = rem
            if left > -1:
                temp += int(a[left])
            if right > -1:
                temp += int(b[right])

            res.append(str(temp % 2))  
            rem = temp // 2            

            left -= 1
            right -= 1

        if rem:
            res.append('1')
        return ''.join(reversed(res))

a = "1010"
b = "1011"
obj = Solution()
print(obj.addBinary(a,b))

