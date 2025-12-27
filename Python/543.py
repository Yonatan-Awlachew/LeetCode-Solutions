class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(node):
            nonlocal diameter
            if not node: return 0
            left,right = dfs(node.left),dfs(node.right)
            diameter = max(diameter,left+right)
            return 1+max(left,right)
        dfs(root)
        return diameter
