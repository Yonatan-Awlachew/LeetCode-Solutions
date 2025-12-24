class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        def dfs(root):
            root.left,root.right = root.right,root.left
            if root.left: dfs(root.left)
            if root.right: dfs(root.right)
            return root
        return dfs(root)
