class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count,L,result,max_freq = {},0,0,0

        for R in range(len(s)):
            count[s[R]] = 1 + count.get(s[R],0)
            max_freq = max(max_freq,count[s[R]])

            while (R-L+1)-max_freq>k:
                count[s[L]]-=1
                L+=1
            result = max(result,R-L+1)
        return result
