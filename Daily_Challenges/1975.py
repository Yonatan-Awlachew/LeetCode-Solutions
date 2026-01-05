class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total,neg_count,min_abs = 0,0,float('inf')
        for row in matrix:
            for x in row:
                total+=abs(x)
                if x<0: neg_count+=1
                min_abs = min(min_abs,abs(x))
        if neg_count%2==1: total-=2*min_abs
        return total
