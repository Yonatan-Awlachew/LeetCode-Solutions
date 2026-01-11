class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        max_area,n = 0,len(matrix[0])
        heights = [0]*n
        for row in matrix:
            for i in range(n):
                if row[i]=='1': heights[i]+=1
                else: heights[i]=0
            stack = [-1]
            for i in range(n+1):
                curr = heights[i] if i<n else 0
                while stack[-1]!=-1 and heights[stack[-1]]>curr:
                    h = heights[stack.pop()]
                    w = i-stack[-1]-1
                    max_area = max(max_area,h*w)
                stack.append(i)
        return max_area
