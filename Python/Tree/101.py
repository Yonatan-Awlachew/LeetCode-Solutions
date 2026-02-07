class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left,right):
            if not left and not right: return True
            if not left or not right: return False
            return (left.val==right.val and check(left.right,right.left) and 
                    check(left.left,right.right))
        return check(root.left,root.right)
