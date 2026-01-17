class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        ans = 0

        for i in range(n):
            x1,y1 = bottomLeft[i]
            x2,y2 = topRight[i]

            for j in range(i+1,n):
                x3,y3 = bottomLeft[j]
                x4,y4 = topRight[j]

                left = max(x1,x3)
                right = min(x2,x4)
                bottom = max(y1,y3)
                up = min(y2,y4)

                if left<right and bottom<up:
                    side = min(right-left,up-bottom)
                    ans = max(ans,side*side)
        return ans
