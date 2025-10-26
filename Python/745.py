class WordFilter:

    def __init__(self, words: List[str]):
        self.lookup = {}
        for i, word in enumerate(words):
            n = len(word)
            for p in range(1, n+1):
                prefix = word[:p]
                for s in range(n):
                    suffix = word[s:]
                    self.lookup[prefix + "#" + suffix] = i

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get(pref + "#" + suff, -1)
