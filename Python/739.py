class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        result = [0]*n
        for i,temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                prev_temp,prev_index = stack.pop()
                result[prev_index] = i-prev_index
            stack.append((temp,i))
        return result
