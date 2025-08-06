class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        count = 1
        last = head

        while last.next:
            last = last.next
            count+=1
        
        k=k%count
        if k==0:
            return head
        curr = head
        for _ in range(count-k-1):
            curr = curr.next
        Head = curr.next
        curr.next = None
        last.next = head
        
        return Head
