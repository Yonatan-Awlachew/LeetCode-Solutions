class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: return 0
        n = max(nums)
        dp = [0]*(n+1)
        for i in nums:
            dp[i]+=i
        
        x,y = 0,0
        for j in dp:
            x,y = y+j, max(x,y)
        return max(x,y)
