class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([root])
        level,max_level = 1,1
        max_sum = float("-inf")
        while queue:
            curr_sum = 0
            n = len(queue)
            for _ in range(n):
                curr = queue.popleft()
                curr_sum+=curr.val
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            if curr_sum>max_sum: max_sum,max_level = curr_sum,level
            level+=1
        return max_level
