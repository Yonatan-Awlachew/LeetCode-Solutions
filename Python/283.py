class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        for i in range(len(nums)):
            if nums[i]:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
