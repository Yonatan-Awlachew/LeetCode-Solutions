class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        tot_time,i = 0,0
        while i<len(colors):
            j = i 
            group_sum,group_max = 0,0
            while j<len(colors) and colors[j]==colors[i]:
                group_sum += neededTime[j]
                group_max = max(group_max,neededTime[j])
                j+=1
            tot_time += group_sum-group_max
            i=j
        return tot_time
