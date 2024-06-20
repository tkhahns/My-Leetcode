# No stack (extra memory) solution:

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 2
        while i < len(tokens):
            if tokens[i] in ["+", "-", "*", "/"]:
                temp = self.operator(tokens[i],int(tokens[i-2]),int(tokens[i-1]))
                tokens[i-2] = temp
                tokens.pop(i-1)
                tokens.pop(i-1)
                i-=2
            else:
                i += 1
        return int(tokens[0])


    def operator(self, op, num1, num2):
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            return int(num1 / num2)

# Stack solution:
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+" or token == "-" or token == "*" or token == "/":
                a, b = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(b + a)
                elif token == "-":
                    stack.append(b - a)
                elif token == "*":
                    stack.append(b * a)
                elif token == "/":
                    stack.append(int(b / a))
            else:
                stack.append(int(token))
        return stack[0]