class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for x in words:
            node = root
            for char in x:
                if char not in node.children: 
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = x
        
        self.result = set()
        rows,cols = len(board),len(board[0])

        def dfs(r,c,node):
            char = board[r][c]
            if char not in node.children: return
            next = node.children[char] 

            if next.word:
                self.result.add(next.word)
                next.word = None
            
            board[r][c]="#"
            for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
                row,col = x+r,y+c
                if 0<=row<rows and 0<=col<cols and board[row][col]!="#":
                    dfs(row,col,next)
            board[r][c] = char

            if not next.children: node.children.pop(char)

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root)
        return list(self.result)
