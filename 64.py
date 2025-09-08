class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        dp = [0]*cols
        for r in range(rows):
            curr = [0]*cols
            for c in range(cols):
                if r==0 and c==0: curr[c] = grid[r][c]
                elif r==0: curr[c] = curr[c-1] + grid[r][c]
                elif c==0: curr[c] = dp[c] + grid[r][c]
                else : curr[c] = grid[r][c] + min(curr[c-1],dp[c])
            dp = curr
        return dp[-1]
