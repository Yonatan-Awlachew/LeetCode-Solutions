class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols = len(obstacleGrid),len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[rows-1][cols-1]==1:
            return 0

        prev = [0]*cols
        for i in range(rows-1,-1,-1):
            curr = [0]*cols
            curr[cols-1]=1
            for j in range(cols-1,-1,-1):
                if obstacleGrid[i][j]==1: curr[j] = 0
                elif i==rows-1 and j==cols-1: curr[j]=1
                else: 
                    right = curr[j+1] if j+1<cols else 0
                    down = prev[j] if i+1<rows else 0
                    curr[j] = right + down
            prev=curr
        return prev[0]
