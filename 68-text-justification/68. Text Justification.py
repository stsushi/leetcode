class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        #crazy hard to do in an interview because the time complexity and space complexity is hard to optimize and many corner cases
        lines = []
        line = []
        total_len = 0
        for i, word in enumerate(words):
            if len(word) + total_len < maxWidth+1:
                line.append(word) # can append a number or filler instead because time complexity of building string is n
                total_len+=len(word)+1
            else:
                total_len-=len(line)
                if len(line) > 1:
                    while total_len < maxWidth: #round robin
                        for index in range(len(line)-1):
                            if total_len == maxWidth:
                                break
                            total_len+=1
                            line[index]+=" "
                else: line[0]+= (maxWidth-len(line[0]))*" "
                lines.append("".join(line))
                line = [word]
                total_len = len(word)+1
        final_line = " ".join(line)
        final_line+= (maxWidth-len(final_line))*" "
        lines.append(final_line)
        return lines