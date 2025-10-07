class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: return []
        rows,cols = len(heights),len(heights[0])

        rows, cols = len(heights),len(heights[0])
        pacific = set()
        atalantic = set()

        def dfs(row,col,visited,prev_height):
            if (min(row,col)<0 or row==rows or col==cols or
                (row,col) in visited or heights[row][col]<prev_height):
                return
            visited.add((row,col))
            dfs(row+1,col,visited,heights[row][col])
            dfs(row-1,col,visited,heights[row][col])
            dfs(row,col+1,visited,heights[row][col])
            dfs(row,col-1,visited,heights[row][col])
        for c in range(cols):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows-1,c,atalantic,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,cols-1,atalantic,heights[r][cols-1])
        return list(pacific & atalantic)
