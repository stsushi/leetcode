# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #check scope stuff
        p_route = []
        q_route = []
        cur = []
        def backtrack(root):
            nonlocal p_route
            nonlocal q_route
            if root == p:
                print(cur)
                p_route = cur[:]
            if root == q:
                print(cur)
                q_route = cur[:]

            if root.left:
                cur.append("l")
                backtrack(root.left)
                cur.pop()
            if root.right:
                cur.append("r")
                backtrack(root.right)
                cur.pop()
        backtrack(root)
        i, j = 0,0
        while(i < len(p_route) and j < len(q_route) and p_route[i] == q_route[j]):
            if p_route[i] == 'l':
                root = root.left
            if p_route[i] == 'r':
                root = root.right
            i+=1
            j+=1
        return root