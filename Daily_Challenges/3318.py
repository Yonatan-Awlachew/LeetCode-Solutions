class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n,result = len(nums),[]        
        for i in range(n-k+1)i
            top,xsum = set(),0
            window = nums[i:i+k]
            freq = Counter(window)
            sorted_freq = sorted(freq.items(),key=lambda a: (-a[1],-a[0]))
            for num,_ in sorted_freq[:x]:
                top.add(num)
            for num in window:
                if num in top:
                    xsum += num
            result.append(xsum)
        return result
