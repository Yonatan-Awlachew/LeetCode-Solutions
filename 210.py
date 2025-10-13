class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(numCourses)}
        for course,prereq in prerequisites:
            graph[prereq].append(course)
        
        state,result,cycle = [0]*numCourses,[],False
        def dfs(node):
            nonlocal cycle
            if cycle: return
            if state[node]==1: 
                cycle = True
                return 
            if state[node]==2: return 
            state[node]=1
            for nei in graph[node]: dfs(nei)
            state[node]=2
            result.append(node)
            
        for course in range(numCourses): 
            if state[course]==0: dfs(course)
        return result[::-1] if not cycle else[]
