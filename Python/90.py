class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result,sub = [],[]
        nums.sort()
        def traverse(i):
            if i==len(nums):
                result.append(sub.copy())
                return
            sub.append(nums[i])
            traverse(i+1)
            sub.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            traverse(i+1)
        traverse(0)
        return result
