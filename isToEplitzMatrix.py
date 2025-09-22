class Solution(object):
    def isToeplitzMatrix(self, matrix):
        rows = len(matrix)
        col = len(matrix[0])
        for i in range(1, rows):
            for j in range(1, col):
                if matrix[i][j]  != matrix[i-1][j-1]:
                    return False

        return True

        