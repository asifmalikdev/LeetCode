class Solution():
    def addBinary(self, a, b):
        left = len(a)
        right = len(b)
        i,j = 0,0
        res = ""
        rem = 0
        while i<left and j<right:
            temp =rem + int(a[i]) + int(b[j])
            rem = 0
            if temp<2:
                res = res + str(temp)
            else:
                rem = 1
                res = res + "0"
            i=i+1
            j=j+1

        return res
a = "11"
b = "1"
obj = Solution()
print(obj.addBinary(a,b))
print("just test",1/2)