# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = self.getListLength(head)
        nodeIdx = length - n

        dummyHead = ListNode(-1, head)
        prev = dummyHead
        curr = head
        count = 0
        while count <= nodeIdx:
            if count == nodeIdx:
                prev.next = curr.next
            else:
                prev = curr
                curr = curr.next
            count += 1
        return dummyHead.next
                
    
    def getListLength(self, head):
        length = 0
        curr = head
        while curr != None:
            length += 1
            curr = curr.next
        return length
        