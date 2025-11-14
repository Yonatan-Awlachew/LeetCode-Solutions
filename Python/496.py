class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {}
        for i in range(len(nums2)):
            next_gret = -1
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    next_gret = nums2[j]
                    break
            result[nums2[i]] = next_gret
        res = []
        for x in nums1:
            res.append(result[x])
        return res
