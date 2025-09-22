class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        stone_hash = {}
        for i in range(len(stones)):
            stone_hash[stones[i]] = stone_hash.get(stones[i], 0) + 1
        res = 0
        for ch in jewels:
            if ch in stone_hash:
                res += stone_hash[ch]

        return res

        