class Solution:
    from collections import Counter
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        res = [[0] * n for _ in range(m)]
        onerow = [row.count(1) for row in grid]
        onecol = [col.count(1) for col in zip(*grid)]
        
        
        for i in range(m):
            for j in range(n):
                res[i][j] = onerow[i] + onecol[j] - \
                    (n - onerow[i]) - (m - onecol[j])
        return res