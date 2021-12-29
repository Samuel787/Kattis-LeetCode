"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        leftNode = root
        while leftNode != None:
            head = leftNode
            while head != None and head.left != None:
                head.left.next = head.right
                if head.next != None:
                    head.right.next = head.next.left
                else:
                    head.right.next = None
                head = head.next
            leftNode = leftNode.left
        return root
        