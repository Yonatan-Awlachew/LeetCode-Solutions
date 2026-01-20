class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        answer = []
        for x in nums:
            if x & (x-1) == 0:
                answer.append(-1)
                continue
            
            msb = 1
            while msb << 1 <= x:
                msb <<= 1
            
            ans = x - (msb >> 1) - 1 if msb > 1 else 1
            i = 0
            while i | (i+1) != x:
                i += 1
            answer.append(i)
        return answer
