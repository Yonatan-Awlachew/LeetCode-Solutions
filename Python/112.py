class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
      def check(root,sum):
        if not root:
          return False
        sum+=root.val
        if not root.left and not root.right:
          return targetSum==sum
        return check(root.left,sum) or check(root.right,sum)
      return check(root,0)
