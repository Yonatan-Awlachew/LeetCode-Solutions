class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for x in range(len(nums)):
            if nums[x]!=val:
                nums[left]=nums[x]
                left+=1
        return left
