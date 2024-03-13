class Solution:
    def isNumber(self, s: str) -> bool:
        e = False
        dot = False
        digit = False
        digits = {'0','1','2','3','4','5','6','7','8','9'}
        size = set(range(len(s)))
        for index, elem in enumerate(s):
            if elem == '+' or elem == '-':
                if index ==0 or (s[index-1] == 'e' or  s[index-1]== 'E'):
                    pass
                else:
                    return False
            elif elem == '.':
                if dot == True or e == True:
                    return False
                dot = True
            elif elem == 'e' or elem == 'E':
                if e == True or digit == False:
                    return False
                e = True
                digit = False
                dot = True
            elif elem not in digits:
                return False
            else:
                digit = True
        if digit == False:
            return False
        else:
            return True
            