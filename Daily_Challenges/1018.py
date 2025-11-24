class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        x,result = 0,[]
        for num in nums:
            x = x*2 + num
            result.append(x%5==0)
        return result
