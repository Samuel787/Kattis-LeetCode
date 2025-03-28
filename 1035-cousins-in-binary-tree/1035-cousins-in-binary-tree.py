# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.x = x
        self.y = y
        self.xParent = None
        self.yParent = None
        self.xLevel = -1
        self.yLevel = -1

        self.dfs(root, None, 0)

        return self.xParent != self.yParent and self.xLevel == self.yLevel

    def dfs(self, root, parent, height):
        if root == None:
            return
        if root.val == self.x:
            self.xLevel = height
            self.xParent = parent
        
        if root.val == self.y:
            self.yLevel = height
            self.yParent = parent
        
        if self.xLevel != -1 and self.yLevel != -1:
            return
        
        self.dfs(root.left, root, height + 1)
        self.dfs(root.right, root, height + 1)
