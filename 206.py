class Solution:
      def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current,previous = head, None
        while current:
          next = current.next
          current.next = previous
          previous = current
          current = next
        return previous
