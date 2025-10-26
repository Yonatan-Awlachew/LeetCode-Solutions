class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1: return stones[0]
        
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            a,b = heapq.heappop(heap),heapq.heappop(heap)
            if b>a: heapq.heappush(heap,a-b)
        if len(heap)==0: return 0
        return -heap[0]
