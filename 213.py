class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        def rob_1(nums):
            prev,curr = 0,0
            for x in nums:
                prev,curr=curr,max(curr,prev+x)
            return curr
        a = rob_1(nums[1:])
        b = rob_1(nums[:-1])
        return max(a,b)
