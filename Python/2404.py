class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count={}
        for n in nums:
            if n%2==0:
                count[n] = 1+count.get(n,0)
        if not count: return -1
        else:
            results = [k for k,v in count.items() if v==max(count.values())]
        return min(results)
