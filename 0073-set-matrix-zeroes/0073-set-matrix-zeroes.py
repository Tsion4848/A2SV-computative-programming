class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
#         rowind = 0
#         colind = 0
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == 0:
#                     rowind = i
#                     colind = j
        
#         for j in range(len(matrix)):
#             matrix[rowind][j] = 0
#             matrix[j][colind] = 0
            
#         print(matrix)

        if len(matrix) == 0 or len(matrix[0]) == 0: return

        row = [False] * len(matrix)
        column = [False] * len(matrix[0])

        # Record the rows and columns with element(s) being zero.
        for rowIndex in range(len(matrix)):
            for colIndex in range(len(matrix[0])):
                if matrix[rowIndex][colIndex] == 0:
                    row[rowIndex] = True
                    column[colIndex] = True

        # Set the qualified entire row(s) and column(s) to zero.
        for rowIndex in range(len(matrix)):
            for colIndex in range(len(matrix[0])):
                if row[rowIndex] == True or column[colIndex] == True:
                    matrix[rowIndex][colIndex] = 0

        return matrix
