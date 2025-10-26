class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        for x in grid:
            l,r = 0 ,len(x)
            while l<r:
                mid = (l+r)//2
                if x[mid]<0:
                    r=mid
                else:
                    l=mid+1
            neg += len(x)-l
        return neg
