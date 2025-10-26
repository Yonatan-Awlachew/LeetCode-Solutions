class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        if head.next==None:
            return None
        slow = fast = head
        prev = None

        while fast and fast.next:
            prev=slow
            fast=fast.next.next
            slow=slow.next
        prev.next=prev.next.next
        return head
