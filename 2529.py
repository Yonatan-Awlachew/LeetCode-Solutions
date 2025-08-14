class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n =len(nums)

        l,r = 0,n
        while l<r:
            mid = (l+r)//2
            if nums[mid]>=0:
                r=mid
            else:
                l=mid+1
        neg = l

        l,r = 0,n
        while l<r:
            mid = (l+r)//2
            if nums[mid]>0:
                r=mid
            else:
                l=mid+1
        pos = n-l
        return max(neg,pos)
        
