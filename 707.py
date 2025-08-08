class ListNode:
    def __init__(self, val=0,next=None, prev=None):
        self.val = val
        self.next= next
        self.prev=prev
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)  # Dummy head
        self.tail = ListNode(0)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        curr=self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size+=1
        
    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if self.size<index or index<0:
            return
        if index == self.size:
            self.addAtTail(val)
            return
        if index ==0:
            self.addAtHead(val)
            return
        node = ListNode(val)
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        node.prev = curr.prev
        node.next = curr
        curr.prev.next = node
        curr.prev = node
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return
        curr= self.head.next
        for _ in range(index):
            curr = curr.next
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.size -= 1
