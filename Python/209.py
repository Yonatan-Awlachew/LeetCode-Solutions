class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length,total = len(nums)+1,0
        L=0
        for R in range(len(nums)):
            total+=nums[R]
            while target<=total:
                length = min(length,R-L+1)
                total-=nums[L]
                L+=1
        return 0 if length==len(nums)+1 else length
