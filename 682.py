class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result=[]
        for x in operations:
            if x=='C':
                result.pop()
            elif x=='D':
                result.append(2*result[-1])
            elif x=='+':
                result.append(result[-1]+result[-2])
            else:
                result.append(int(x))
        return sum(result)
