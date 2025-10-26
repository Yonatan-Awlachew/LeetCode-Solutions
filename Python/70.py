class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        prev,result = 0,1
        for i in range(n):
            prev,result = result, prev+result
        return result
        
