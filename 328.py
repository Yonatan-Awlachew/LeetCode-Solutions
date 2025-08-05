class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head:
        return None

      odd = head
      even = even_first = head.next

      while even and even.next:
        odd.next = odd.next.next
        odd = odd.next

        even.next = even.next.next
        even = even.next

      odd.next = even_first
      return head
