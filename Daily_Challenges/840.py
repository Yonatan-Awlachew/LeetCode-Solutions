class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        count = 0

        for r in range(rows-2):
            for c in range(cols-2):
                if grid[r+1][c+1]!=5: continue
                visited,valid = set(),True

                for i in range(r,r+3):
                    for j in range(c,c+3):
                        val = grid[i][j]
                        if val<1 or val>9 or val in visited:
                            valid = False
                            break
                        visited.add(val)
                    if not valid: break
                if not valid: continue
                
                target = grid[r][c] + grid[r][c+1] + grid[r][c+2]
                for i in range(3):
                    if grid[r+i][c] + grid[r+i][c+1] + grid[r+i][c+2]!=target:
                        valid = False
                        break
                if not valid: continue
                for j in range(3):
                    if grid[r][c+j] + grid[r+1][c+j] + grid[r+2][c+j]!=target: 
                        valid = False
                        break

                if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]!=target or
                    grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2]!=target ): continue

                if not valid: continue
                count+=1
        return count
