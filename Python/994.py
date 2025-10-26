class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        fresh=0
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1: fresh+=1
                elif grid[i][j]==2: queue.append((i,j))
        if fresh==0: return 0
        mint=0
        while queue:
            for x in range(len(queue)):
                r,c = queue.popleft()
                negh = [(0,1),(0,-1),(1,0),(-1,0)]
                for i,j in negh:
                    if (0<=r+i<rows and 0<=c+j<cols 
                        and grid[r+i][c+j]==1):
                            grid[r+i][c+j]=2
                            fresh-=1
                            queue.append((r+i,c+j))
            mint+=1 
        if fresh==0: return mint-1
        else: return -1
