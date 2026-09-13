class Solution(object):
    def tallestBillboard(self, rods):
        dp = {0:0}
        for rod in rods:
            current_dp = dp.copy()
            for diff,shorter in current_dp.items():
                breakpoint()
                dp[diff + rod] = max(dp.get(diff + rod, 0),shorter)

                new_diff = abs(diff-rod)
                new_shorter = shorter + min(diff, rod)

                dp[new_diff] = max(
                    dp.get(new_diff, 0),
                    new_shorter
                )
                print(dp)
        return dp[0]


obj = Solution()
print(obj.tallestBillboard([6,2,3,1]))