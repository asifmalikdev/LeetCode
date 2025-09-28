class Solution:
    def minimumTotal(self, triangle):
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])
        
        return triangle[0][0]
a = "hello"
b = "hello"
print(a is b)
c = int(4)
d = int(4)
print(c is d)