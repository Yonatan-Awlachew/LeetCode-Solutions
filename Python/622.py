class ListNode:
    def __init__(self,val,prev,next):
        self.val=val
        self.prev=prev
        self.next=next
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.left = ListNode(0,None,None)
        self.right = ListNode(0,self.left,None)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        node = ListNode(value,self.right.prev,self.right)
        self.right.prev.next = node
        self.right.prev = node
        self.size-=1
        return True


    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.size+=1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next==self.right
    
    def isFull(self) -> bool:
        return self.size==0


