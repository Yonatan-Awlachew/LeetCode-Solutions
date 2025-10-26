class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        n = len(nums)
        
        for i in range(n):
            if i>far: return False
            far = max(far,i + nums[i])
            if far>=n-1: return True
        return True
