# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None or head.next == None):
            return head
        curr = head
        prev = None
        while curr.next != None:
            temp = curr.next #assert temp is not None
            curr.next = prev 
            prev = curr
            curr = temp
        curr.next = prev
        return curr

