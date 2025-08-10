class RecentCounter:

    def __init__(self):
        self.requests = deque()
        self.count = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.count+=1
        while self.requests and self.requests[0]<t-3000:
            self.requests.popleft()
            self.count-=1
        return self.count
