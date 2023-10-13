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
        dummyHead = ListNode(-1, head)
        start = 0
        end = 0
        
        prev = dummyHead
        curr = dummyHead.next

        prevNodeRef = dummyHead
        currNodeRef = dummyHead.next

        while curr != None:
            elementsInWindow = end - start + 1
            if elementsInWindow == n + 1:
                # increment the start pointer also
                prevNodeRef = currNodeRef
                currNodeRef = currNodeRef.next
                start += 1
            end += 1
            print("Start value is " + str(start))
            print("ref pointer val: " + str(currNodeRef.val))
                
            curr = curr.next

        # remove the nth node from end
        prevNodeRef.next = currNodeRef.next
        return dummyHead.next

    # def removeNthFromEnd(self, head, n):
    #     length = self.getListLength(head)
    #     nodeIdx = length - n

    #     dummyHead = ListNode(-1, head)
    #     prev = dummyHead
    #     curr = head
    #     count = 0
    #     while count <= nodeIdx:
    #         if count == nodeIdx:
    #             prev.next = curr.next
    #         else:
    #             prev = curr
    #             curr = curr.next
    #         count += 1
    #     return dummyHead.next
                
    
    # def getListLength(self, head):
    #     length = 0
    #     curr = head
    #     while curr != None:
    #         length += 1
    #         curr = curr.next
    #     return length
        