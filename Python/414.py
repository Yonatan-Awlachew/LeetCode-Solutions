class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct_nums = sorted(set(nums), reverse=True)
        return distinct_nums[2] if len(distinct_nums) >= 3 else distinct_nums[0]
