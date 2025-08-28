import random
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map: return False
        self.map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map: return False
        index = self.map[val]
        last = self.arr[-1]

        self.arr[index],self.arr[-1] = self.arr[-1],self.arr[index]
        self.map[last] = index

        self.arr.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)
        
