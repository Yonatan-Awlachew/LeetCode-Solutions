class Solution:
    def numOfWays(self, n: int) -> int:
        Mod = 10**9 + 7
        A,B = 6,6
        for _ in range(2,n+1):
            ABA = (3*A+2*B)%Mod
            ABC = (2*A+2*B)%Mod
            A,B = ABA,ABC
        return (A+B)%Mod
