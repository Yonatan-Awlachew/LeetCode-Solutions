from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
      result=[]
      queue=deque()
      
      if root:
        queue.append(root)
      
      while len(queue)>0:
        temp=[]
        for _ in range(len(queue)):
          curr = queue.popleft()
          temp.append(curr.val)
          if curr.left:
            queue.append(curr.left)
          if curr.right:
            queue.append(curr.right)
        result.append(temp)
      return result
