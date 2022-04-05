# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.curr = root

    def next(self):
        """
        :rtype: int
        """
        if self.curr == None:
            self.curr = self.stack.pop()
        else:
            while self.curr.left != None:
                self.stack.append(self.curr)
                self.curr = self.curr.left
        
        temp = self.curr.val
        
        if self.curr.right != None:
            self.curr = self.curr.right
        else:
            self.curr = None
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curr or self.stack
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()