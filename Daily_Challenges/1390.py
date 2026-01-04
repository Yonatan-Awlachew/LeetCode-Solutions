class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            divisors = set()
            for i in range(1,int(sqrt(n))+1):
                if n%i==0:
                    divisors.add(i)
                    divisors.add(n//i)
                
                if len(divisors)>4: break
            if len(divisors)==4: total+=sum(divisors)
        return total
