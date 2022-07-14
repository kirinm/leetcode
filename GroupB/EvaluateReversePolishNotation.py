class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for el in tokens:
            if el not in '+-/*':
                stack.append(el)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if el == '+': val = a+b
                if el == '*': val = a*b
                if el == '/': val = a/b
                stack.append(val)
        return int(stack.pop())                    