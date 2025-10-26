class RandomizedCollection:

    def __init__(self):
        self.arr = []
        self.map = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.map[val].add(len(self.arr))
        self.arr.append(val)
        return len(self.map[val])==1

    def remove(self, val: int) -> bool:
        if not self.map[val]: return False
        index = self.map[val].pop()
        last = self.arr[-1]
        self.arr[index] = last
        self.map[last].add(index)
        self.map[last].discard(len(self.arr)-1)

        self.arr.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        
