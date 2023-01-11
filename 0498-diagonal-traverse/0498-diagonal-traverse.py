class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        defdict = collections.defaultdict()
        if not mat:
            return res
        
        m = len(mat)
        n = len(mat[0])
        res = []
        row, col = 0, 0
         
        while row < m and col < n:
             
            temp = []
             
            # To collect all elements of a diagonal, keep going one row down and column 
            # to the left until we hit matrix boundaries
            i, j = row, col
            while i < m and j >= 0:
                temp.append(mat[i][j])
                i += 1
                j -= 1
                 
            # Reverse the order for alternate diagonals
            if (row + col) % 2 == 0:
                res.extend(temp[::-1])
            else:
                res.extend(temp)
                 
            # Set row, col to traverse the next diagonal
            if col < n - 1:
                col += 1
            else:
                row += 1
                 
        return res