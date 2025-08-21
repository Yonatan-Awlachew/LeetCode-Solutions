class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        sub=[]

        def traverse(i):
            if i>=len(nums):
                result.append(sub.copy())
                return
            sub.append(nums[i])
            traverse(i+1)
            sub.pop()
            traverse(i+1)
        traverse(0)
        return result
