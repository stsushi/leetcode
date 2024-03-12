"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(root):
            head = root
            tail = root
            if root.left:
                lh,lt = helper(root.left)
                lt.right = root
                root.left = lt
                head = lh
            if root.right:
                rh, rt = helper(root.right)
                rh.left = root
                root.right = rh
                tail = rt
            head.left = tail
            tail.right = head
            return head,tail
        if root:
            head,tail =helper(root)
            return head
        