class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyStack:

    def __init__(self):
        self.left = self.right = None
        self.count = 0

    def push(self, x: int) -> None:
        node = ListNode(x)
        if self.count==0:
            self.left=self.right=node
        else: 
            self.right.next = node
            self.right = self.right.next
        self.count+=1

    def pop(self) -> int:
        if self.count==0:
            return 
        elif self.left==self.right:
            x=self.left.val
            self.left=self.right
            self.count-=1
            return x
        self.count-=1
        curr = self.left
        while curr:
            if curr.next==self.right:
                x=self.right.val
                self.right=curr
                self.right.next = None
                return x
            curr = curr.next
    def top(self) -> int:
        if self.count!=0:
            return self.right.val
        return None

    def empty(self) -> bool:
        return self.count==0
