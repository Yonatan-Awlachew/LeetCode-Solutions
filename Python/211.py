class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for x in word:
            if x not in curr.children:
                curr.children[x] = TrieNode()
            curr = curr.children[x]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(index,node):
            curr = node
            for i in range(index,len(word)):
                char = word[i]
                if char==".":
                    for child in curr.children.values():
                        if dfs(i+1,child): return True
                    return False
                else:
                    if char not in curr.children: return False
                    curr = curr.children[char]
            return curr.word
        return dfs(0,self.root)
