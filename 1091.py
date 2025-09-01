class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1: return -1
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
        queue = deque([(0,0,1)])
        visited = set((0,0))

        while queue:
            r,c,length = queue.popleft()
            if r==n-1 and c==n-1: return length
            for x,y in directions:
                row,col = r+x,c+y
                if (0<=row<n and 0<=col<n and
                    grid[row][col]==0 and (row,col) not in visited):
                    visited.add((row,col))
                    queue.append((row,col,length+1))
        return -1
