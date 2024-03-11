class Solution:
    # possible solutions prefix sum + binary search
    # init -> prefix sum o(n) runtime
    # pickindex -> binary search log(n) runtime

    # alias method pack everything into dict like struct with max len 2
    # init -> n runtime at most iter over each elem once
    # pick -> 1 runtime takes at most 2 box check to pick 

    def __init__(self, w: List[int]): 
        ep =  10e-5 #variable due to rounding errors on floats
        self.n = len(w) # len of original list and actually also the len of the boxes so not technically needed
        weight_sum = sum(w) # the total sum of all elements (only needed to get the elements as percents)
        self.box_size = 1/self.n # the size of each index
        w = [x/weight_sum for x in w] #each elem is now what percent of the total it is

        self.boxes = [] # holds the probabilities
        big = {i:val for (i, val) in enumerate(w) if  val >= self.box_size} # probabilities greater than or equal to the right size
        small = {i:val for (i, val) in enumerate(w) if  val < self.box_size} # boxes smaller than the right size
        #algo works like this bigger elements will be used to perfectly fill smaller ones
        #this means that every elem will at most have 2 options in it
        # big ones might become small ones in this process and get added to the small stack
        while small and big:
            j, size = small.popitem() # 
            i, big_size = big.popitem() # can replace with some iter thing but i dont want to get into syntax hell
            
            self.boxes.append((j,i,size))

            big_size = big_size-(self.box_size-size) # new size of big box
            if big_size <  self.box_size-ep: #constant is due to rounding errors on floats
                small[i] = big_size #big box now small
            else:
                big[i] = big_size #big box still big 
        self.boxes.extend((key,key,self.box_size) for key in big) # add the perfect sized ones


    def pickIndex(self) -> int:
        r = random.random()*self.n # range 0->2 
        i, line = int(r), random.random()* self.box_size #one random var is for which box we are in, the second random var is for which elem of the box we are in... Could also be replaced by using the remainder of the first var and doing some fancy math lol
        print(self.boxes[i][0] if self.boxes[i][2]> line else self.boxes[i][1])
        return self.boxes[i][0] if self.boxes[i][2]> line else self.boxes[i][1]

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()