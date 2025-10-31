class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        numbers,result = {},[]
        for x in nums:
            if x not in numbers: numbers[x]=1
            else: result.append(x)
        return result
