# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        count = 0
        stack = []
        if root != None:
            stack.append(root)
        while stack:
            count += 1
            curr = stack.pop()
            if curr.left != None:
                stack.append(curr.left)
            if curr.right != None:
                stack.append(curr.right)
        return count
            

        