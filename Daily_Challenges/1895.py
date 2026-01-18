class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        n = min(r, c)
        rowPrefix = [[0]*c for _ in range(r)]
        colPrefix = [[0]*c for _ in range(r)]
        
        for i in range(c):
            cumm = 0
            for j in range(r):
                cumm += grid[j][i]
                colPrefix[j][i] = cumm
        
        for i in range(r):
            cumm = 0
            for j in range(c):
                cumm += grid[i][j]
                rowPrefix[i][j] = cumm
        
        for k in range(n, 1, -1):
            for i in range(0, r - k + 1):
                for j in range(0, c - k + 1):
                    target = rowPrefix[i][j + k - 1] - (rowPrefix[i][j - 1] if j > 0 else 0)
                    
                    valid = True
                    for r_idx in range(i, i + k):
                        row_sum = rowPrefix[r_idx][j + k - 1] - (rowPrefix[r_idx][j - 1] if j > 0 else 0)
                        if row_sum != target:
                            valid = False
                            break
                    if not valid: continue
                    
                    for c_idx in range(j, j + k):
                        col_sum = colPrefix[i + k - 1][c_idx] - (colPrefix[i - 1][c_idx] if i > 0 else 0)
                        if col_sum != target:
                            valid = False
                            break
                    if not valid:continue
                    
                    diag_sum = 0
                    for d in range(k):
                        diag_sum += grid[i + d][j + d]
                    if diag_sum != target:continue
                    
                    anti_diag_sum = 0
                    for d in range(k):
                        anti_diag_sum += grid[i + d][j + k - 1 - d]
                    if anti_diag_sum != target:continue
                    
                    return k
        
        return 1
