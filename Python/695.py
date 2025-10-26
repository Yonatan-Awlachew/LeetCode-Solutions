class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        visited = set()
        def dfs(r,c):
            if (min(r,c)<0 or r==rows or c==cols or
                grid[r][c]==0 or (r,c) in visited):
                return 0
            visited.add((r,c))
            area=1
            area+=dfs(r+1,c)
            area+=dfs(r-1,c)
            area+=dfs(r,c+1)
            area+=dfs(r,c-1)
            return area
        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    max_area=max(dfs(r,c),max_area)
        return max_area
            
