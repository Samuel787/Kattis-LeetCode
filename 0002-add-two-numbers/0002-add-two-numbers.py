# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        firstPointer = l1
        secondPointer = l2
        carry = 0
        dummyHead = ListNode()
        prev = dummyHead
        
        while firstPointer != None or secondPointer != None:
            firstVal = 0
            secondVal = 0
            if firstPointer != None:
                firstVal = firstPointer.val
                firstPointer = firstPointer.next
            if secondPointer != None:
                secondVal = secondPointer.val
                secondPointer = secondPointer.next

            total = firstVal + secondVal + carry
            if total > 9:
                carry = 1
                total %= 10
            else:
                carry = 0
            prev.next = ListNode(total)
            prev = prev.next
            
        if carry != 0:
            prev.next = ListNode(carry)
        
        return dummyHead.next