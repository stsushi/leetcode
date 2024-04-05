class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        num = 0
        num_set = set("1234567890")
        ptr = 0
        for elem in abbr:
            if elem in num_set:
                if elem == '0' and num == 0:
                    return False
                num = num *10 + int(elem)
            else:
                ptr +=num
                num = 0
                if ptr > len(word)-1 or word[ptr] != elem:
                    return False
                ptr+=1

        ptr +=num
        return True if ptr == len(word) else False
