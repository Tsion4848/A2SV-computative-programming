class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        result = 0
        checked = defaultdict(int)
        deliciousness.sort()
        ans = 0
        for d in deliciousness:
            n = 1
            while n <= d + d:
                ans = (ans + checked[n-d]) % (10 ** 9 + 7)
                n = n << 1
            checked[d] += 1
        return ans