class MyHashMap:
    def __init__(self):
        self.size = 2003
        self.buckets = [[] for k in range(self.size)]

    def index(self,key:int)-> int:
        return key%self.size
    
    def put(self, key: int, value: int) -> None:
        temp = self.buckets[self.index(key)]
        for i,(x,y) in enumerate(temp):
            if x==key:
                temp[i] = (key,value)
                return 
        temp.append((key,value))

    def get(self, key: int) -> int:
        temp = self.buckets[self.index(key)]
        for x,y in temp:
            if x==key:
                return y
        return -1

    def remove(self, key: int) -> None:
        temp = self.buckets[self.index(key)]
        for i,(x,y) in enumerate(temp):
            if x==key:
                temp.pop(i)
                return
