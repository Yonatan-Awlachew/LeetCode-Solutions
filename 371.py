class Solution:
    def getSum(self, a: int, b: int) -> int:
        x = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b!=0:
            temp = (a&b)<<1
            a = (a^b) & x
            b = temp & x
        return a if a<=max_int else ~(a^x)
