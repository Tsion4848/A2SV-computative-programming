class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if mat == [] or r * c != len(mat) * len(mat[0]):
            return mat

        ans = [[0 for j in range(c)] for i in range(r)]
        x = 0

        for row in mat:
            for num in row:
                ans[x // c][x % c] = num
                x += 1

        return ans