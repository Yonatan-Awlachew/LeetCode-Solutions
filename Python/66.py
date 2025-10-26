class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        y= int("".join(map(str, digits)))
        y+=1
        digits = [int(d) for d in str(y)]
        return digits
