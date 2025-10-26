class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid=head
        trav=head
        while trav and trav.next:
            trav=trav.next.next
            mid=mid.next
        return mid
