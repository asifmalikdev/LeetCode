import math

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0

        gcd_val = math.gcd(a, b)

        for i in range(1, math.isqrt(gcd_val) + 1):
            if gcd_val % i == 0:
                if gcd_val // i == i:
                    ans += 1
                else:
                    ans += 2
        return ans
                    
        return ans


obj = Solution()
a = 1
b = 2
print(obj.commonFactors(a,b))