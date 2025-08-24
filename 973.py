class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap,i=[],0
        result=[]
        for x in points:
            heap.append((x[0]**2 + x[1]**2,i))
            i+=1
        heapq.heapify(heap)
        for j in range(k):
            a,b = heapq.heappop(heap)
            result.append(points[b])
        return result
