class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        result = []
        
        def dfs(node,path):
            if node==n-1:
                result.append(path[:])
                return
            for x in graph[node]:
                path.append(x)
                dfs(x,path)
                path.pop()
        dfs(0,[0])
        return result
