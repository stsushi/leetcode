class Solution:
    def calculate(self, s: str) -> int:
        num_set = set('1234567890')
        op_set = set('/*-+')
        def ans(index):
            stack, num, op = [], 0, "+"
            def calculate(num, op):
                if op == '+': return stack.append(num)
                if op == '-': return stack.append(-num)
                if op == "*": return stack.append(stack.pop()* num)
                if op == '/': return stack.append(int(stack.pop() / num))
            while(index < len(s)):
                elem = s[index]
                if elem in op_set:
                    calculate(num,op)
                    num, op = 0, elem
                if elem in num_set:
                    num= num*10+int(elem)
                if elem == ")":
                    calculate(num,op)
                    return  sum(stack), index
                if elem == "(":
                    num, j = calc(index+1)
                    index = j
                index+=1
            calculate(num,op)
            return sum(stack)
        return ans(0)