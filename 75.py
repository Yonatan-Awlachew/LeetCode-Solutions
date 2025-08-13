class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def quick(nums,s,e):
            if e-s<=0:
                return nums
            pivot,left = nums[e],s
            for i in range(s,e):
                if nums[i]<pivot:
                    nums[i],nums[left] = nums[left],nums[i]
                    left+=1
            nums[left],nums[e]=pivot,nums[left]

            quick(nums,s,left-1)
            quick(nums,left+1,e)
            return nums
        nums=quick(nums,0,len(nums)-1)
