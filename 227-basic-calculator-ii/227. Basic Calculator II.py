class Solution:
    def calculate(self, s: str) -> int:
        stack, num, i, op = [], 0, 0, "+"
        def calculate(num, op):
            if op == '+': return stack.append(num)
            if op == '-': return stack.append(-num)
            if op == "*": return stack.append(stack.pop()* num)
            if op == '/': return stack.append(int(stack.pop() / num))
        num_set = set('1234567890')
        op_set = set('/*-+')
        for elem in s:
            if elem in op_set:
                calculate(num,op)
                num, op = 0, elem
            if elem in num_set:
                num= num*10+int(elem)
        calculate(num,op)
        return sum(stack)