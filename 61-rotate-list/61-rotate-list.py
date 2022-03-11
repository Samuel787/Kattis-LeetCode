# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        
        length = 0;
        curr = head
        prev = None
        while curr != None:
            prev = curr;
            curr = curr.next;
            length += 1
        endRef = prev;
        
        rotate = length - k % length;
        if rotate == 0:
            return head
        originalHead = head;
        endRef.next = originalHead;
        length = 1;
        curr = head;
        while length < rotate:
            curr = curr.next;
            length += 1;
        newHead = curr.next;
        curr.next = None;
        return newHead;
        
        
        
        
        