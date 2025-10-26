class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for x in operations:
            if x=="++X" or x=="X++": result+=1
            else: result-=1
        return result
