class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead: return -1
        queue,visited = deque(["0000"]),set(["0000"])
        count = 0
        def neighbour(code):
            neighbours=[]
            for i in range(4):
                digit=int(code[i])
                for x in [-1,+1]:
                    newDigit = (digit+x+10)%10
                    newCode= code[:i] + str(newDigit)+code[i+1:]
                    neighbours.append(newCode)
            return neighbours
        while queue:
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                if curr==target: return count
                for x in neighbour(curr):
                    if x not in dead and x not in visited:
                        queue.append(x)
                        visited.add(x)
            count+=1
        return -1
