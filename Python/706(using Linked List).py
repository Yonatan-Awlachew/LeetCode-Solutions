class ListNode:
    def __init__(self,key=-1,val=-1,next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def hash(self,key):
        return key%len(self.map)
    
    def put(self, key: int, value: int) -> None:
        curr = self.map[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key,value)

    def get(self, key: int) -> int:
        curr = self.map[self.hash(key)]
        while curr.next:
            if curr.next.key==key:
                return curr.next.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.map[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next=curr.next.next
                return
            curr = curr.next
        
