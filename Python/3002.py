class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        s1,s2 = set(nums1),set(nums2)
        unique1=len(s1-s2)
        unique2=len(s2-s1)
        n=len(nums1)
        
        common=len(s1&s2)
        new1=min(unique1,n//2)
        new2=min(unique2,n//2)
        return min(new1+new2+common,n)
