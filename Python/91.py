class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=="0": return 0
        n=len(s)
        dynamic = [0]*(n+1)
        dynamic[0],dynamic[1] = 1,1

        for i in range(2,n+1):
            one_digit = int(s[i-1:i])
            two_digit = int(s[i-2:i])

            if 1<=one_digit<=9: dynamic[i]+=dynamic[i-1]
            if 10<=two_digit<=26: dynamic[i]+=dynamic[i-2]
        return dynamic[n]
