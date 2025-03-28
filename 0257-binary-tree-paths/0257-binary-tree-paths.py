# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        self.result = []
        if root == None:
            return self.result
        self.traverse(root, "")
        return self.result
    
    def traverse(self, root, path):
        if root == None:
            return
        path += str(root.val)
        if root.left == None and root.right == None:
            self.result.append(path)

        if root.left != None:
            self.traverse(root.left, path + "->")
        if root.right != None:
            self.traverse(root.right, path + "->")
