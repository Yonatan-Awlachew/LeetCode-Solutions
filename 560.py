class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        curr_sum,count = 0,0

        for x in nums:
            curr_sum+=x
            if curr_sum-k in prefix:
                count+=prefix[curr_sum-k]
            prefix[curr_sum] = prefix.get(curr_sum,0)+1
        return count
