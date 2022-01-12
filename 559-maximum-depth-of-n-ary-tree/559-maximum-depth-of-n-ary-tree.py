"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if root == None:
            return 0
        children = root.children
        max_depth = 0
        for child in children:
            temp = self.maxDepth(child)
            max_depth = max(temp, max_depth)
        return max_depth + 1