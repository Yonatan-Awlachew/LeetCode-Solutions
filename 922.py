class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        even,odd = 0,1
        while even<n and odd<n:
            if nums[even]%2 == 0: even+=2
            elif nums[odd]%2 == 1: odd+=2
            else:
                nums[even],nums[odd] = nums[odd],nums[even]
                even+=2
                odd+=2
        return nums
