class Node:
    def __init__(self,key:int,value:int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node:Node):
        prev,next = node.prev,node.next
        prev.next , next.prev = next, prev

    def add(self,node:Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.add(node)
        else:
            if len(self.cache)>=self.capacity:
                recent = self.tail.prev
                self.remove(recent)
                del self.cache[recent.key]
            new = Node(key,value)
            self.add(new)
            self.cache[key] = new
