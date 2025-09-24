class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"

        ans = []
        if (numerator < 0) ^ (denominator < 0):
            ans.append("-")

        numerator, denominator = abs(numerator), abs(denominator)
        q, r = divmod(numerator, denominator)
        ans.append(str(q))
        if r == 0:
            return "".join(ans)
        ans.append(".")
        remainder_map = {}  
        while r != 0:
            if r in remainder_map:
                idx = remainder_map[r]
                ans.insert(idx, "(")
                ans.append(")")
                break
            remainder_map[r] = len(ans)

            r *= 10
            q, r = divmod(r, denominator)
            ans.append(str(q))

        return "".join(ans)





n = 428
d = 125
obj = Solution()
print(obj.fractionToDecimal(n,d))