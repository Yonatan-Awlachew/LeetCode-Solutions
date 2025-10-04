class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def robTree(node):
            if node==None: return (0,0)
            
            left = robTree(node.left)
            right = robTree(node.right)

            first = node.val + left[1] + right[1]
            second = max(left) + max(right)

            return (first,second)
        return max(robTree(root))
