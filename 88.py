class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j,k = 0,0,0
        while k<=m+n-1:
            if i<m:
                nums1[k]=nums1[j]
                i+=1
            elif j<n:
                nums1[k]=nums2[j]
                j+=1
            elif nums1[i]<nums2[j]:
                nums1[k]=nums1[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            k+=1
