class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0]*n
        for i in range(m-1,-1,-1):
            curr = [0]*n
            curr[n-1]=1
            for j in range(n-2,-1,-1):
                curr[j] = curr[j+1] + prev[j]
            prev = curr
        return prev[0]
