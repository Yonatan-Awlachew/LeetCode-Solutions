class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        i,n = 0,len(arr)
        while i<n:
            if arr[i]==0 and i+1<n:
                for j in range(n-1,i,-1):
                    arr[j] = arr[j-1]
                if i+1<n:
                    arr[i+1]=0
                i+=2
            else:
                i+=1
