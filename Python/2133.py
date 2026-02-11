class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        target = set(range(1,n+1))
        for i in range(n):
            if set(matrix[i])!=target: return False
            if set(matrix[j][i] for j in range(n))!=target: return False
        return True
