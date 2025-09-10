class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr = 0
        for n in nums:
            curr = max(0,curr)
            curr+=n
            maxSum = max(curr,maxSum)
        return maxSum
