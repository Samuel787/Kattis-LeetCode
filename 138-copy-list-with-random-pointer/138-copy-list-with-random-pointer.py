"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head == None:
            return head;
        
        curr = head
        nodeDict = {None:None}
        sentinelHead = Node(0)
        temp = Node(curr.val)
        nodeDict[curr] = temp
        sentinelHead.next = temp
        curr2 = sentinelHead.next
        curr = curr.next
        while curr:
            temp = Node(curr.val)
            nodeDict[curr] = temp
            curr = curr.next
            curr2.next = temp
            curr2 = curr2.next
        
        curr2 = sentinelHead.next
        curr = head
        while curr2:
            curr2.random = nodeDict[curr.random]
            curr = curr.next
            curr2 = curr2.next
        
        return sentinelHead.next
        
        
            
        