class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result,prev = 0,0
        for x in bank:
            curr = str(x).count("1")
            if curr>0:
                result+=curr*prev
                prev = curr
        return result
