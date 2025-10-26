class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        Sums = sum(arr[:k])
        if (Sums/k)>= threshold: result = 1
        else: result = 0

        for i in range(k,len(arr)):
            Sums += arr[i] - arr[i-k]
            if (Sums/k)>=threshold: result+=1
        return result
