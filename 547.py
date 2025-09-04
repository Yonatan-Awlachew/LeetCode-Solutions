class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited = set()
        provinces = 0

        def dfs(city):
            for i in range(n):
                if isConnected[city][i]==1 and i not in visited:
                    visited.add(i)
                    dfs(i)
        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces+=1
        return provinces
