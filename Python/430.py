
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head

        def dfs(node):
            curr,last = node,None
            while curr:
                next = curr.next
                if curr.child:
                    child_head=curr.child
                    child_tail = dfs(child_head)

                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None

                    if next:
                        child_tail.next = next
                        next.prev = child_tail
                    last=child_tail
                else:
                    last = curr
                curr = next
            return last
        dfs(head)
        return head
