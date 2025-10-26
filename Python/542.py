class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols = len(mat),len(mat[0])
        queue=deque()
        for x in range(rows):
            for y in range(cols):
                if mat[x][y]==0: queue.append((x,y))
                else: mat[x][y]=float("inf")
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            r,c = queue.popleft()
            for x,y in directions:
                row,col = r+x,c+y
                if (0<=row<rows and 0<=col<cols):
                    if mat[row][col]>mat[r][c]+1:
                        mat[row][col]=mat[r][c]+1
                        queue.append((row,col))
        return mat
