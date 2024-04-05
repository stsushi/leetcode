"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        #concept traverse from top to bottom...
        # if they converge naturually thats good
        # but this concept is most important for when they do not converge naturally
        # it will cause them to both meet at their convergent path...
        #p1 -> p2 -> p3 -> c1 -> c2 -> c3
        #.........q1 -> c1 -> c2 -> c3

        #If you force them to switch paths after they reach c3:
        #P Travels: (3 steps to c1), (3 common steps to q1), (1 step to c1)
        #Q Travels: (1 step to c1), (3 common steps to p1), (3 steps to c1)
        pt = p
        qt = q
        while(pt!=qt):
            if not pt.parent:
                pt = q
            else:
                pt = pt.parent
            if not qt.parent:
                qt = p
            else:
                qt = qt.parent
        return pt
