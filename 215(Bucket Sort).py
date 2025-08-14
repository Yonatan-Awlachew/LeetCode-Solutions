class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_val = min(nums)
        size = max(nums)-min_val+1
        counts = [0]*size
        
        for n in nums:
            counts[n-min_val]+=1
        
        i=0
        for n in range(len(counts)-1,-1,-1):
            for j in range(counts[n]):
                nums[i]=n+min_val
                i+=1
        
        return nums[k-1]
    
