class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        max_sum = 0
        stack,i = [],-1

        slow,fast = head,head
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        while slow:
            max_sum = max(stack[i]+slow.val,max_sum)
            slow = slow.next
            i-=1
        return max_sum
