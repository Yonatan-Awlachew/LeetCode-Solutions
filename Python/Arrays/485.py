class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,temp = 0,0
        for num in nums:
            if num==1: temp+=1
            else: temp=0
            count=max(temp,count)
        return count
