class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        queue = deque()

        for x in range(rows):
            for y in range(cols):
                if grid[x][y]==1: queue.append((x,y,0))
        if not queue or len(queue)==rows*cols: return -1
        max_dist = -1
        directions = [ (0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r,c,distance = queue.popleft()
            for i,j in directions:
                row,col = r+i,c+j
                if (0<=row<rows and 0<=col<cols and grid[row][col]==0):
                    grid[row][col]=1
                    queue.append((row,col,distance+1))
                    max_dist=max(max_dist,distance+1)
        return max_dist
