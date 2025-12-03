class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        if " " not in s: return len(s)
        else:        
            for i in range(len(s)-1,-1,-1):
                if s[i]==" ": continue
                else: count+=1
                if s[i-1]==" ": return count
