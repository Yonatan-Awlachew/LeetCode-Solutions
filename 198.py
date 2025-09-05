class Solution:
    def rob(self, nums: List[int]) -> int:
        prev,curr = 0,0
        for i in nums:
            prev,curr = curr,max(curr,prev+i)
        return curr
