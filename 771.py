class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jews,count = set(jewels),0
        for x in stones:
            if x in jews: count+=1
        return count
