class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def insertHead(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def removeTail(self):
        if self.size == 0:
            return None
        tail = self.tail.prev
        self.removeNode(tail)
        return tail

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 0
        self.nodeMap = {} 
        self.freqMap = {} 
    
    def updateFreq(self, node):
        freq = node.freq
        self.freqMap[freq].removeNode(node)
        
        if freq == self.minFreq and self.freqMap[freq].size == 0:
            self.minFreq += 1
        
        node.freq += 1
        if node.freq not in self.freqMap:
            self.freqMap[node.freq] = DLL()
        self.freqMap[node.freq].insertHead(node)

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.updateFreq(node)
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.updateFreq(node)
        else:
            if self.size == self.capacity:
                temp = self.freqMap[self.minFreq].removeTail()
                del self.nodeMap[temp.key]
                self.size -= 1
            newNode = Node(key, value)
            self.nodeMap[key] = newNode
            if 1 not in self.freqMap:
                self.freqMap[1] = DLL()
            self.freqMap[1].insertHead(newNode)
            self.minFreq = 1
            self.size += 1
