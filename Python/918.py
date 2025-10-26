class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)

        curr_max = max_sum = nums[0]
        curr_min = min_sum = nums[0]

        for n in nums[1:]:
            curr_max = max(n,curr_max + n)
            max_sum = max(max_sum,curr_max)

            curr_min = min(n,curr_min + n)
            min_sum = min(curr_min,min_sum)
        
        if max_sum<0: return max_sum
        return max(max_sum,total-min_sum)
