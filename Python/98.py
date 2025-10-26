class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvalid(root,left,right):
            if not root:
                return True
            if not(root.val>left and root.val<right):
                return False
            return isvalid(root.left,left,root.val) and isvalid(root.right,root.val,right)
        return isvalid(root,float("-inf"),float("inf"))
