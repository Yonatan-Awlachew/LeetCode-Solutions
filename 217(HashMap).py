class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for x in nums:
            if x in map: return True
            else: map[x]=1
        return False
        
