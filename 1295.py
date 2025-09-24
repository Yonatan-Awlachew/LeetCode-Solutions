class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            temp = 0
            while x:
                x//=10
                temp+=1
            if temp%2==0: count+=1
        return count
