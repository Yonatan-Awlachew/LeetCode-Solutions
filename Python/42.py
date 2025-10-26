class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        L,R = 0, len(height)-1
        left_max,right_max = height[L],height[R]
        water = 0

        while L<R:
            if left_max<right_max:
                L+=1
                left_max = max(left_max,height[L])
                water+=left_max-height[L]
            else: 
                R-=1
                right_max = max(right_max,height[R])
                water+=right_max-height[R]  
        return water
