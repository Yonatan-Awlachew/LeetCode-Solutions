class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left,right)
    
    def merge(self,l,r):
        dummy = ListNode(0)
        tail = dummy
        while l and r:
            if l.val<r.val:
                tail.next,l = l,l.next
            else:
                tail.next,r=r,r.next
            tail=tail.next
        tail.next = l if l else r
        return dummy.next
