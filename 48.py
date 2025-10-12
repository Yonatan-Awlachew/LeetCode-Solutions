class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows,cols = len(matrix),len(matrix[0])
        for i in range(rows):
            for j in range(i+1,cols):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for k in range(cols//2):
            for l in range(rows):
                matrix[l][k],matrix[l][cols-k-1] = matrix[l][cols-k-1],matrix[l][k]
   
