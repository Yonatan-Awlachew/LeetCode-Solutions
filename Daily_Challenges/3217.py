class Solution:
    def modifiedList(self, nums: List[int],head: Optional[ListNode])->Optional[ListNode]:
        remove_numbers = set(nums)

        while head and head.val in remove_numbers:
            head = head.next
        
        curr = head
        while curr and curr.next:
            if curr.next.val in remove_numbers:
                curr.next = curr.next.next
            else: curr= curr.next
        return head
