class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i:[] for i in range(numCourses) }
        for course,prereq in prerequisites:
            pre[course].append(prereq)
        visited = set()
        def dfs(course):
            if course in visited: return False
            if pre[course]==[]: return True
            visited.add(course)
            for x in pre[course]:
                if not dfs(x): return False
            visited.remove(course)
            pre[course]=[]
            return True
        for course in range(numCourses):
            if not dfs(course): return False
        return True
