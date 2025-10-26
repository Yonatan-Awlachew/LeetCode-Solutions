
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        if not fast or not fast.next: return None

        slow2 = head
        while slow!=slow2:
            slow = slow.next
            slow2 = slow2.next
        return slow
