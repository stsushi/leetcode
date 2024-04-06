class Solution:
    def calculate(self, s: str) -> int:
        num_set = set('1234567890')
        op_set = set('/*-+')
        stack = []
        def evaluate(num, op):
            if op == "*": return stack.append(stack.pop() * num)
            if op == "/": return stack.append(int(stack.pop()/num))
        num, op = 0, "+"
        for elem in s:
            if elem in num_set:
                num = num*10 + int(elem)
            if elem in op_set:
                if op == "*" or op == "/":
                    evaluate(num,op)
                elif op == "+":
                    stack.append(num)
                else:
                    stack.append(-num)
                num, op = 0, elem
        if op == "*" or op == "/":
            evaluate(num, op)
        elif op == "+":
            stack.append(num)
        else:
            stack.append(-num)
        return sum(stack)