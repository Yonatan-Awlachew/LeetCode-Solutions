class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        def check(nums):
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]: return False
            return True
        while not check(nums):
            min_sum,index = float("inf"),0
            for i in range(len(nums)-1):
                curr_sum = nums[i]+nums[i+1]
                if curr_sum<min_sum: min_sum,index = curr_sum,i
            merged = nums[index] + nums[index+1]
            nums[index] = merged
            nums.pop(index+1)
            count+=1
        return count
