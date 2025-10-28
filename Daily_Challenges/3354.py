class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total,left,ans = sum(nums),0,0

        for i in nums:
            if i==0:
                if 2*left==total: ans+=2
                elif abs(2*left-total)==1: ans+=1
            left+=i
        return ans
