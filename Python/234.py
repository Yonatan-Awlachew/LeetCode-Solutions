class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        elem = []
        while head:
            elem.append(head.val)
            head=head.next
        i,j= 0,len(elem)-1
        while i<=j:
            if elem[i]!=elem[j]:
                return False
            i,j = i+1,j-1
        return True
