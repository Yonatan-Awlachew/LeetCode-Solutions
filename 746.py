class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        x,y = 0,0
        for i in range(2,len(cost)+1):
            x,y = y,min(y+cost[i-1],x+cost[i-2])
        return y
