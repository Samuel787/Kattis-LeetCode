# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        l1 = []
        l2 = []
        l1.append(root)
        height = 0
        isL1 = True
        isFound = False
        while (l1 or l2) and not isFound:
            height += 1
            if isL1:
                while l1:
                    curr_node = l1.pop(0)
                    if curr_node.left == None and curr_node.right == None:
                        isFound = True
                        break
                    if curr_node.left != None:
                        l2.append(curr_node.left)
                    if curr_node.right != None:
                        l2.append(curr_node.right)
                isL1 = False
            else:   
                while l2:
                    curr_node = l2.pop(0)
                    if curr_node.left == None and curr_node.right == None:
                        isFound = True
                        break
                    if curr_node.left != None:
                        l1.append(curr_node.left)
                    if curr_node.right != None:
                        l1.append(curr_node.right)
                isL1 = True
        return height
                