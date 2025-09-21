class UnionFind:
    def __init__(self,n):
        self.parent = {}
        self.rank = {}

        for i in range(1,n+1):
            self.parent[i] = i
            self.rank[i] = 0
    
    def find(self,n):
        p = self.parent[n]
        while p!=self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self,a,b):
        p1,p2 = self.find(a), self.find(b)
        if p1==p2: return False

        if self.rank[p1]>self.rank[p2]: self.parent[p2]=p1
        elif self.rank[p1]<self.rank[p2]: self.parent[p1] = p2
        else:
            self.parent[p2]=p1
            self.rank[p1]+=1
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        UF = UnionFind(n)

        for x,y in edges:
            if not UF.union(x,y):
                return [x,y]
