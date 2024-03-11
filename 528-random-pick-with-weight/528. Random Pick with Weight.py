class Solution:
    # possible solutions prefix sum + binary search
    # init -> prefix sum o(n) runtime
    # pickindex -> binary search log(n) runtime

    # alias method pack everything into dict like struct with max len 2
    # init -> n runtime at most iter over each elem once
    # pick -> 1 runtime takes at most 2 box check to pick 

    def __init__(self, w: List[int]): 
        ep =  10e-5
        self.n = len(w)
        weight_sum = sum(w)
        self.box_size = 1/self.n
        w = [x/weight_sum for x in w] #each elem is now what percent of the total it is

        self.boxes = []
        big = {i:val for (i, val) in enumerate(w) if  val >= self.box_size}
        small = {i:val for (i, val) in enumerate(w) if  val < self.box_size}
        while small and big:
            j, size = small.popitem()
            i, big_size = big.popitem()
            
            self.boxes.append((j,i,size))

            big_size = big_size-(self.box_size-size)
            if big_size <  self.box_size-ep: #constant is due to rounding errors on floats
                small[i] = big_size
            else:
                big[i] = big_size
        self.boxes.extend((key,key,self.box_size) for key in big)


    def pickIndex(self) -> int:
        r = random.random()*self.n # range 0->2 
        i, line = int(r), random.random()* self.box_size
        print(self.boxes[i][0] if self.boxes[i][2]> line else self.boxes[i][1])
        return self.boxes[i][0] if self.boxes[i][2]> line else self.boxes[i][1]

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()