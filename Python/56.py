class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        result = []
        start,end = intervals[0]

        for i in range(1,len(intervals)):
            x,y = intervals[i]
            if x<=end: end = max(end,y)
            else: 
                result.append([start,end])
                start,end = x,y
        result.append([start,end])
        return result
