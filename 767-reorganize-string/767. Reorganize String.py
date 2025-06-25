class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = [0] * 26
        max_count_index = 0
        for c in s:
            i = ord(c) - ord('a')
            counter[i] += 1
            if counter[i] > counter[max_count_index]:
                max_count_index = i
        
        if counter[max_count_index] > math.ceil(len(s) / 2):
            return ''

        res = [None] * len(s)
        pos = 0
        for i in range(26):
            count = counter[(max_count_index + i) % 26]
            char = chr(ord('a') + (max_count_index + i) % 26)
            for _ in range(count):
                print(res)
                res[pos] = char
                pos += 2
                if pos >= len(s):
                    pos = 1
        return ''.join(res)