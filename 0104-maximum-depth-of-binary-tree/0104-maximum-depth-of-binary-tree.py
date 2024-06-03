# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # self.max = 0
        # dfs(root)
        # return self.max
        return self.dfs(root)

    def dfs(self, root):
        if root == None:
            return 0
        leftDepth = 1 + self.dfs(root.left)
        rightDepth = 1 + self.dfs(root.right)
        return max(leftDepth, rightDepth)