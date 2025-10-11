class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols, positions = len(matrix),len(matrix[0]),[]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0: positions.append((i,j))
        
        for x,y in positions:
            for col in range(cols): matrix[x][col]=0
            for row in range(rows): matrix[row][y]=0
