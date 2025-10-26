class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def postorder(root):
            if not root:
                return 
            postorder(root.left)
            postorder(root.right)
            result.append(root.val)
        postorder(root)
        return result
