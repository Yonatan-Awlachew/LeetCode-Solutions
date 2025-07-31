class Solution:
    def toLowerCase(self, s: str) -> str:
        x=""
        for i in range(len(s)):
            if s[i].isupper():
                x+=s[i].lower()
                continue
            x+=s[i]
        return x
