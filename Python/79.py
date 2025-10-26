class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])

        def dfs(r,c,i):
            if len(word)==i: return True
            if(min(r,c)<0 or r==rows or c==cols or board[r][c]!=word[i]): return False
            
            temp = board[r][c]
            board[r][c]="#"
            result = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or
                        dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            board[r][c] = temp
            return result
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
        return False
