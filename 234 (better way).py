
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        
        # assign slow to the middle value
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        # reverse half of the elements starting from the middle 
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow= temp

        # check for the palindrome
        l ,r = head, prev
        while r:
            if l.val!=r.val:
                return False
            l,r = l.next, r.next
        return True
