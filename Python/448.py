class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = [i for i in range(1,len(nums)+1)]
        set1 = set(result)
        set2 = set(nums)
        return list(set1-set2)
