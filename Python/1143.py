class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)
        dynamic = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if text1[i]==text2[j]:
                    dynamic[i][j] = 1 + dynamic[i+1][j+1]
                else:
                    dynamic[i][j] = max(dynamic[i+1][j],dynamic[i][j+1])
        return dynamic[0][0]
