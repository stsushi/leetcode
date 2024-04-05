class SparseVector:
    def __init__(self, nums: List[int]):
        #intuition we can def do this in n time, dont even want overhead of hashing algo
        # in some extreme case we can consider doing binary search on matching so lets form into sparse arr
        self.vec = []
        for i,elem in enumerate(nums):
            if elem != 0:
                self.vec.append((i,elem))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        small_vec, big_vec = (self.vec, vec.vec) if len(self.vec) < len(vec.vec) else (vec.vec, self.vec)
        ans = 0
        ptr, j, y  = 0, big_vec[0][0], big_vec[0][1]
        for i, x in small_vec:
            while j < i:
                if ptr > len(big_vec)-2:
                    return ans
                ptr, j, y = ptr+1, big_vec[ptr+1][0], big_vec[ptr+1][1]
            if j == i:
                ans = ans + y*x
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)