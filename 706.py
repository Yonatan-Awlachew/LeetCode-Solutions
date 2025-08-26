class MyHashMap:
    def __init__(self):
        self.M = 2003
        self.buckets = [[] for _ in range(self.M)]

    def _idx(self, key: int) -> int:
        return key % self.M

    def put(self, key: int, value: int) -> None:
        b = self.buckets[self._idx(key)]
        for i, (k, v) in enumerate(b):
            if k == key:
                b[i] = (key, value)   
                return
        b.append((key, value))         

    def get(self, key: int) -> int:
        b = self.buckets[self._idx(key)]
        for k, v in b:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        b = self.buckets[self._idx(key)]
        for i, (k, _) in enumerate(b):
            if k == key:
                b.pop(i)
                return
