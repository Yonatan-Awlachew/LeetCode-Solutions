class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr=0
        for x in nums:
            if curr<2 or x>nums[curr-2]:
                nums[curr]=x
                curr+=1
        return curr
