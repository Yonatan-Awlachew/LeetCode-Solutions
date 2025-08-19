class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        queue = deque([(root,1)])

        while queue:
            n,d = queue.popleft()

            if not n.left and not n.right:
                return d
            if n.left: queue.append((n.left,d+1))
            if n.right: queue.append((n.right,d+1))
