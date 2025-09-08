class Solution(object):
    def getNoZeroIntegers(self, n):
        for i in range(1, n):
            a, b = i, n - i
            if "0" not in str(a) and "0" not in str(b):
                return [a, b]
