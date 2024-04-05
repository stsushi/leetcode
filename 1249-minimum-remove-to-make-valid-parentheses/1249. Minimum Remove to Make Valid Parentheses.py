class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []

        for index, elem in enumerate(s):
            if elem == "(":
                stack.append(index)
                s[index] = ""
            if elem == ")":
                if stack:
                    s[stack.pop()] = "("
                else:
                    s[index] = ""
        return "".join(s)