class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word:str)->None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True
    
    def canForm(self,word:str)->bool:
        n = len(word)
        def dfs(start,count):
            if start == n:
                return count>=2
            node = self.root
            for i in range(start,n):
                c = word[i]
                if c not in node.children: return False
                node = node.children[c]
                if node.word:
                    if dfs(i+1,count+1): return True
            return False
        return dfs(0,0)
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        result = []
        for word in words:
            if not word: continue
            if self.canForm(word): result.append(word)
            else: self.insert(word)
        return result
