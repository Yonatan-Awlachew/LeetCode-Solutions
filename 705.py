class ListNode:
    def __init__(self,key):
        self.key = key
        self.next = None
class MyHashSet:
    def __init__(self):
        self.set = [ListNode(0) for _ in range(10**4)]

    def add(self, key):
        curr = self.set[key%len(self.set)]

        while curr.next:
            if curr.next.key == key:
                return 
            curr = curr.next
        curr.next = ListNode(key)

    def contains(self, key):
        curr = self.set[key%len(self.set)]
        
        while curr.next:
            if curr.next.key == key:
                return True
            curr = curr.next
        return False

    def remove(self, key):
        curr = self.set[key%len(self.set)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
