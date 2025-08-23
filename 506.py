class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        result = [""]*n
        heap = []
        for i in range(len(score)):
            heap.append((-score[i],i))
        heapq.heapify(heap)

        rank = 1
        while heap:
            x,y = heapq.heappop(heap)
            if rank==1:
                result[y] = "Gold Medal"
            elif rank==2:
                result[y] = "Silver Medal"
            elif rank==3:
                result[y] = "Bronze Medal"
            else:
                result[y] = str(rank)
            rank+=1
        return result
