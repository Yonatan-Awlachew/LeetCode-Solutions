class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        frequency = Counter(nums1)
        result = []
        for x in nums2:
            if x in frequency and frequency[x]>0: 
                result.append(x)
                frequency[x]-=1
        return result
