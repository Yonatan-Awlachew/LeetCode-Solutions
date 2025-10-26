class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap,result=[],[]
        for i in range(len(mat)):
            heap.append((sum(mat[i]),i))
        heapq.heapify(heap)
        for x in range(k):
            a,b = heapq.heappop(heap)
            result.append(b)
        return result
