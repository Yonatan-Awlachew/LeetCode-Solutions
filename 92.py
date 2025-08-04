class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)

        LP,curr = dummy, head
        for i in range(left-1):
            LP,curr = curr,curr.next
        
        prev = None
        for i in range(right-left+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        LP.next.next = curr
        LP.next = prev

        return dummy.next
