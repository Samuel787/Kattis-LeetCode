# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        mSet = set()
        currA = headA
        while currA != None:
            mSet.add(currA)
            currA = currA.next
        
        currB = headB
        while currB != None:
            if currB in mSet:
                return currB
            currB = currB.next
        return None