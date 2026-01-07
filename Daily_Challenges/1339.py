class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        max_product = 0
        def dfs_total(node):
            if not node: return 0
            return node.val + dfs_total(node.left) + dfs_total(node.right)
        total = dfs_total(root)
        def dfs(node):
            if not node: return 0
            left,right = dfs(node.left),dfs(node.right)
            subtree_sum = node.val + left + right
            nonlocal max_product
            max_product = max(max_product,subtree_sum*(total-subtree_sum))
            return subtree_sum
        dfs(root)
        return max_product%(10**9+7)
