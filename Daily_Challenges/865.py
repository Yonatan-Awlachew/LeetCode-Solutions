class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node==None: return(node,0)
            leftNode,leftDepth = dfs(node.left)
            rightNode,rightDepth = dfs(node.right)
            if leftDepth==rightDepth: return(node,leftDepth+1)
            if leftDepth>rightDepth: return(leftNode,leftDepth+1)
            else: return (rightNode,rightDepth+1)
        return dfs(root)[0]
