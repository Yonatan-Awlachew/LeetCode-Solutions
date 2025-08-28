class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        for x in words:
            curr = Counter(x)
            for c in count:
                count[c]=min(count[c],curr[c])
        result = []
        for y in count:
            for i in range(count[y]):
                result.append(y)
        return result
