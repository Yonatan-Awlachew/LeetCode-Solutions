class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==1:
            return stones[0]

        heap=[]
        for x in stones:
            heap.append(-x)
        heapq.heapify(heap)

        while len(heap)>1:
            x,y = heapq.heappop(heap),heapq.heappop(heap)
            if x==y:
                continue
            elif x>y:
                y=y-x
                heapq.heappush(heap,y)
            else:
                x=x-y
                heapq.heappush(heap,x)
        if len(heap)==0: return 0
        return -heap[0]
