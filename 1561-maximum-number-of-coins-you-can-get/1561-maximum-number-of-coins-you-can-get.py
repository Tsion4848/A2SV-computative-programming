class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sortedPiles = sorted(piles, reverse=True)
        res = 0
        count = len(piles) / 3

        for i in range(len(piles)) :
            if not count:
                return res
            if i % 2 == 1 : 
                res += sortedPiles[i]
                count -= 1