# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
   
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.count = {}
        self.helper(root)
        maximum = 0
        for i in self.count:
            if self.count[i] > maximum:
                maximum = self.count[i]
                # print(str(i) + ":" + str(self.count[i]))
        
        res = []
        for i in self.count:
            if self.count[i] == maximum:
                res.append(i)
        
        return res;
        
        
    def helper(self, root):
        if root == None:
            return
        if root.val in self.count:
            self.count[root.val] += 1
        else:
            self.count[root.val] = 1
        self.helper(root.left)
        self.helper(root.right)
        return
        