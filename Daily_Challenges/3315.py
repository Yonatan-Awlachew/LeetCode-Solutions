class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        answer = []
        for x in nums:
            if x!=2: answer.append(x - ((x+1) &(-x-1))//2)
            else: answer.append(-1)
        return answer
