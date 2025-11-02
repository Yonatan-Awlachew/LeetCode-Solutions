class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0]*n for i in range(m)]

        for r,c in guards:  grid[r][c]=1
        for r,c in walls:   grid[r][c]=2

        directions  = [(0,1),(0,-1),(1,0),(-1,0)]

        for row,col in guards:
            for x,y in directions:
                r,c = row+x, col+y
                while 0<=r<m and 0<=c<n and grid[r][c]!=1 and grid[r][c]!=2:
                    if grid[r][c]==0:
                        grid[r][c]=3
                    r+=x
                    c+=y
        result = sum(i.count(0) for i in grid)
        return result
