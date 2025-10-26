class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows,cols = len(grid),len(grid[0])
        visited = set()
        count = 0
        def dfs(row,col):
            if (min(row,col)<0 or row==rows or col==cols or 
               (row,col) in visited or grid[row][col]=="0"):
                return 
            visited.add((row,col))
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1" and (row,col) not in visited:
                    dfs(row,col)
                    count+=1
        return count
