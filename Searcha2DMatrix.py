class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1

        while left <= right:
            mid = (left + right)//2
            col = mid % n
            row = mid // n
            mid_value = matrix[row][col]
            if mid_value == target:
                return True
            elif mid_value > target:
                right = mid-1
            elif mid_value < target:
                left = mid+1


obj = Solution()
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
print(obj.searchMatrix(matrix, 23))