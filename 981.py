class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        l,r = 0,len(values)-1
        result = ""
        while l<=r:
            mid = (l+r)//2
            if values[mid][0]<=timestamp:
                result = values[mid][1]
                l = mid+1
            else:
                r=mid-1
        return result

