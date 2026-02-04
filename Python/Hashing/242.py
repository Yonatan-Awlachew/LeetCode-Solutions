class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): return False
        counter1,counter2 = {},{}
        for x in s:
            if x in counter1: counter1[x]+=1
            else: counter1[x]=1
        for y in t:
            if y in counter2: counter2[y]+=1
            else: counter2[y]=1
        return counter1==counter2
