class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = defaultdict(int)
        max_char = ""
        max_count = 0
        for letter in s:
            counter[letter] +=1
            cur_count = counter[letter]
            if cur_count > max_count:
                max_count = cur_count
                max_char = letter
        if max_count > (len(s)-1)//2+1:
            return ""
        i = 0
        res = [None]*len(s)
        for _ in range(max_count):
            res[i] = max_char
            i+=2
        del counter[max_char]

        for letter in counter:
            count = counter[letter]
            for _ in range(count):
                if i > len(s)-1:
                    i = 1
                res[i] = letter
                i+=2
        return "".join(res)
            