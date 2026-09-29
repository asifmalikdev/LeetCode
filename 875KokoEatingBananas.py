class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left,right = 1,max(piles)
        while left < right:
            mid = (left + right) // 2
            hours = 0
            for pile in piles:
                hours = hours + (pile + mid -1) // mid
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left





piles = [3,6,7,11]
h = 8
obj = Solution()
res = obj.minEatingSpeed(piles, h)
print(res)