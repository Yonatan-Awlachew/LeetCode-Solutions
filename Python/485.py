class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        counts =[]
        for x in nums:
            if not x:
                l=0
                continue
            l+=1
            counts.append(l)
        if counts:
            return max(counts)
        else:
            return 0
