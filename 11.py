class Solution:
    def maxArea(self, height: List[int]) -> int:
        L,R,max_area = 0,len(height)-1,0

        while L<R:
            curr_max = min(height[L],height[R])*(R-L)
            max_area = max(curr_max,max_area)
            if height[L]>height[R]: R-=1
            else: L+=1
        return max_area
