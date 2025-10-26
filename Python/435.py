class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        prev_end = intervals[0][1]
        for i in range(1,len(intervals)):
            start,end = intervals[i]
            if prev_end>start: 
                count+=1
                prev_end = min(end,prev_end)
            else: prev_end = end
        return count
