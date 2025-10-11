class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix),len(matrix[0])
        row_flag,col_flag = [False]*rows, [False]*cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0: col_flag[j],row_flag[i] = True,True
        
        for i in range(rows):
            for j in range(cols):
                if row_flag[i] or col_flag[j]: matrix[i][j]=0
