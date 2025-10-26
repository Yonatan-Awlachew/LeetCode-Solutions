class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        perim = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1: 
                    perim+=4
                    if r+1<rows and grid[r+1][c]==1:
                        perim-=2
                    if c+1<cols and grid[r][c+1]==1:
                        perim-=2
        return perim
