class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        D = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in D:
                if stack and stack[-1] == D[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack
