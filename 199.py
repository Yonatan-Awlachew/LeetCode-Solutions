class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque()
        level = 0

        if root: queue.append(root)

        while len(queue)>0:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr.right: queue.append(curr.right)
                if curr.left: queue.append(curr.left)
                if len(result)==level: result.append(curr.val)
            level+=1
        return result
