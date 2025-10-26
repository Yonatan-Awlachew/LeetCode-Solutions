class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head:
        return head
      dummy, curr = ListNode(0),head

      while curr:
        prev = dummy
        while prev.next and prev.next.val<curr.val:
          prev = prev.next
        
        nextnode = curr.next
        curr.next,prev.next = prev.next, curr
        
        curr = nextnode
        
      return dummy.next
