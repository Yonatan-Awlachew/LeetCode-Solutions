class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[:k])
        max_sum = total
        for i in range(k,len(nums)):
            total+=nums[i]
            total-=nums[i-k]
            max_sum = max(max_sum,total)
        return max_sum/k
