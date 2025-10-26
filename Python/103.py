class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        level = 0
        if root:
            queue.append(root)
        while queue:
            temp=[]
            for _ in range(len(queue)):
                curr = queue.popleft()
                temp.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            if level%2==1:
                temp.reverse()
            result.append(temp)
            level+=1
        return result
