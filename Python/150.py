class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if  x.lstrip("-").isdigit(): stack.append(int(x))
            else:
                b = stack.pop()
                a = stack.pop()
                if x=='+': stack.append(a+b)
                elif x=='-': stack.append(a-b)
                elif x=='*': stack.append(a*b)
                elif x=='/': stack.append(int(a/b))         
        return stack[-1]
