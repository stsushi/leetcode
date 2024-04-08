from heapq import heapify, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # another method quick select...
        points = [((x*x+y*y),(x,y)) for (x,y) in points]
        heapify(points)
        ans = []

        while(k):
            ans.append(heappop(points)[1])
            k-=1
        return ans