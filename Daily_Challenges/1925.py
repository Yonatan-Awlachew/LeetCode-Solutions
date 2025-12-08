class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for a in range(1,n+1):
            for b in range(1,n+1):
                res = a**2 + b**2
                c = int(sqrt(res))
                if c*c==res and c<=n: count+=1
        return count
