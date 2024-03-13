class Solution:

    def __init__(self, w: List[int]):
        ep =  10e-5 #variable due to rounding errors on floats
        sum_w = sum(w)
        n = len(w)
        self.n = len(w) # too lazy to refactor... realized i need this in pickindex
        box_size = 1/n
        self.box_size = 1/n # too lazy to refactor... realized i need this in pickindex
        w = [x/sum_w for x in w] #converts them into percent of whole

        small = { i:x for i,x in enumerate(w) if x < box_size}
        big = { i:x for i,x in enumerate(w) if x >= box_size}
        
        self.boxes = []

        while small and big:
            small_index, small_size = small.popitem()
            big_index, big_size = big.popitem()

            self.boxes.append((small_index,big_index,small_size))

            new_big_size = big_size +small_size - box_size
            if new_big_size >= box_size:
                big[big_index] = new_big_size
            else:
                small[big_index] = new_big_size
        self.boxes.extend((key,key, box_size) for key in big)
        self.boxes.extend((key, key, box_size) for key in small) #rounding error




    def pickIndex(self) -> int:
        i = int(random.random()*self.n)
        j = random.random()*self.box_size
        pick = self.boxes[i]
        return pick[0] if j < pick[2] else pick[1]



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()