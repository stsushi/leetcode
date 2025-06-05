class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mappings = dict()
        mappings[" "] = " "
        pointer = 0
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for letter in key:
            if letter != " " and letter not in mappings:
                mappings[letter] = alphabet[pointer]
                pointer += 1
        return "".join([mappings[letter] for letter in message])