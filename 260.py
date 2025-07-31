class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result ={}
        for i in nums:
            if i not in result:
                result[i]=1
            else:
                result[i]+=1
        out=[]
        for i in nums:
            if result[i]==1:
                out.append(i)
        return out
