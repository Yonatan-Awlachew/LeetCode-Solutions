class Solution:
    def totalMoney(self, n: int) -> int:
        monday,result = 1,0
        for x in range(n):
            result += monday+(x%7)
            if (x+1)%7==0:
                monday +=1
        return result
