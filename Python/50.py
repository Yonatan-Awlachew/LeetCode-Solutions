class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate(x,n):
            if n==0: return 1
            if n==1: return  x
            temp = calculate(x,n//2)
            if n%2==0: return temp*temp
            return x*temp*temp
        if n<0: return 1/(calculate(x,abs(n)))
        return calculate(x,n)
