class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k=len(nums)-k
        def quickSelect(s, e):
            pivot,left = nums[e],s
            for i in range(s,e):
                if pivot>=nums[i]:
                    nums[left],nums[i] = nums[i],nums[left]
                    left+=1
            nums[left],nums[e]=nums[e],nums[left]
            
            if left>k: return quickSelect(s,left-1)
            elif left<k: return quickSelect(left+1,e)
            else: return nums[left]

        return quickSelect(0,len(nums)-1)
