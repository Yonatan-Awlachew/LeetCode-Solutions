class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        h = sorted(hFences + [1, m])
        v = sorted(vFences + [1, n])
        
        h_diffs = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                h_diffs.add(h[j] - h[i])
        
        max_side = -1
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                diff = v[j] - v[i]
                if diff in h_diffs:
                    max_side = max(max_side, diff)
        
        return (max_side * max_side) % (10**9 + 7) if max_side != -1 else -1
