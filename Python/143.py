class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head,head
        while fast and fast.next: slow,fast = slow.next, fast.next.next
        curr,prev,slow.next = slow.next,None,None
        while curr:
            next = curr.next
            curr.next = prev
            prev,curr = curr, next

        first,second = head,prev
        while second:
            temp1,temp2 = first.next,second.next
            first.next = second
            second.next = temp1
            first,second = temp1,temp2
        
