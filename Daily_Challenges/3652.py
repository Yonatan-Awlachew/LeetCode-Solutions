class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n,m=len(prices),k//2
        base =0
        for i in range(n): base+=prices[i]*strategy[i]

        A,B = [0]*n,[0]*n
        for i in range(n):
            A[i] = -strategy[i]*prices[i]
            B[i] = (1-strategy[i])*prices[i]
        
        sumA,sumB = sum(A[0:m]),sum(B[m:k])
        maxGain = sumA+sumB

        for l in range(1,n-k+1):
            sumA -=A[l-1]
            sumA +=A[l+m-1]

            sumB -= B[l+m-1] 
            sumB += B[l+k-1]
            maxGain = max(maxGain,sumA+sumB)
        return base+max(0,maxGain)
