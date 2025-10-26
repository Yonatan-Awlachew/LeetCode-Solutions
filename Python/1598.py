class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0

        for x in logs:
            if x=='./':
                continue
            elif x=='../':
                result = max(0,result-1)
            else:
                result+=1
        return result
