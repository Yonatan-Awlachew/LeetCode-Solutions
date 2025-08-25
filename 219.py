class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = set()
        for i,x in enumerate(nums):
            if x in map: return True
            map.add(x)
            if len(map)>k: map.remove(nums[i-k])
        return False
