# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        self.result = []
        self.traverse(root)
        return self.result


    def traverse(self, root):
        if root == None:
            return
        if root.left != None:
            self.traverse(root.left)
        if root.right != None:
            self.traverse(root.right)
        self.result.append(root.val)
