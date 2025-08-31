class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return 
        rows,cols = len(board),len(board[0])
    
        def dfs(row,col):
            if (min(row,col)<0 or row==rows or col==cols or board[row][col]!="O"):
                return
            board[row][col]="#"
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        for row in range(rows):
            dfs(row,0)
            dfs(row,cols-1)
        for col in range(cols):
            dfs(0,col)
            dfs(rows-1,col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=="O": board[row][col]="X"
                elif board[row][col]=="#": board[row][col]="O"
