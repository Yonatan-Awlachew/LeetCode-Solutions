class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root: queue.append(root)
        bottom = root.val
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                if i==0: bottom = curr.val
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
        return bottom
