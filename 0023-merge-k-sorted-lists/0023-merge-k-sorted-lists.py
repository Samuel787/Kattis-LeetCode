# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        if len(lists) == 2:
            return self.merge2Lists(lists[0], lists[1])
        
        mid = len(lists) // 2
        leftPartition = self.mergeKLists(lists[0: mid]) 
        rightPartition = self.mergeKLists(lists[mid:])
        return self.merge2Lists(leftPartition, rightPartition)

    def merge2Lists(self, listOne, listTwo):
        head = ListNode(-1, None)
        curr = head
        while listOne != None and listTwo != None:
            if listOne.val < listTwo.val:
                curr.next = listOne
                listOne = listOne.next
            else:
                curr.next = listTwo
                listTwo = listTwo.next
            curr = curr.next
        
        if listOne != None:
            curr.next = listOne
        
        if listTwo != None:
            curr.next = listTwo
        
        return head.next
            
        

