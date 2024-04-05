class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        num = 0
        num_set = set("1234567890")
        ptr = 0
        for letter in abbr:
            if letter in num_set:
                if num == 0 and letter == "0":
                    return False
                num = num*10+int(letter)
            else:
                ptr+= num
                num= 0
                if ptr > len(word)-1 or word[ptr] != letter:
                    return False
                ptr+=1
        ptr+= num
        return False if ptr!=len(word) else True
