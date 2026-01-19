class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m,n = len(mat),len(mat[0])
        prefix = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                prefix[i+1][j+1] = mat[i][j] + prefix[i][j+1] + prefix[i+1][j] - prefix[i][j]
        
        def find_square(k):
            for i in range(m-k+1):
                for j in range(n-k+1):
                    total = prefix[i+k][j+k] - prefix[i+k][j] - prefix[i][j+k] + prefix[i][j]
                    if total<=threshold: return True
            return False
        lo,hi = 0,min(m,n)
        ans = 0
        while lo<=hi:
            mid = (lo+hi)//2
            if find_square(mid):
                ans=mid
                lo=mid+1
            else: hi = mid-1
        return ans
