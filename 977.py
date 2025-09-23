class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0,n-1
        result = [0]*n
        i = n-1

        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                result[i] = nums[l]**2
                l+=1
            else:
                result[i] = nums[r]**2
                r-=1
            i-=1
        return result
