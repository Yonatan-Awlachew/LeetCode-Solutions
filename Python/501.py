class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None
        self.count = 0
        self.max_count = 0
        self.mode = []

        def inorder(root):
            if not root:
                return None

            inorder(root.left)

            if self.prev==root.val:
                self.count+=1
            else:
                self.count=1
            self.prev=root.val

            if self.count>self.max_count:
                self.max_count = self.count
                self.mode = [root.val]
            elif self.count==self.max_count:
                self.mode.append(root.val)
            
            inorder(root.right)
        
        inorder(root)
        return self.mode
