class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1,int(sqrt(n))+1)]
        queue,visited = deque([n]),set([n])
        level = 0
        while queue:
            level+=1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for x in squares:
                    next = curr-x
                    if next<0: break
                    if next ==0: return level
                    if next not in visited:
                        visited.add(next)
                        queue.append(next)
        return level
