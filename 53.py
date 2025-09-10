class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr = 0
        for n in nums:
            curr = max(curr,0) + n
            max_sum = max(curr,max_sum)
        return max_sum
