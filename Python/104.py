class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            return 1+max(left,right)
        return dfs(root)
