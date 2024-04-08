class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = 0
        ans = 0
        for elem in s:
            if elem == "(":
                stack +=1
            elif elem == ")" and stack !=0:
                stack -=1
            else:
                ans+=1

        return ans+stack

