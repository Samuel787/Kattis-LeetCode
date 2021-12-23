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
        
        new_lists = []
        i = 0
        while i < len(lists):
            l1 = lists[i]
            if i + 1 != len(lists):
                l2 = lists[i + 1]
                l1 = self.mergeLists(l1, l2)
            new_lists.append(l1)
            i += 2
        return self.mergeKLists(new_lists)
            
    def mergeLists(self, list1, list2):
        head = ListNode(0, None)
        pointer_to_head = head
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                head.next = list1
                head = head.next
                list1 = list1.next
            else:
                head.next = list2
                head = head.next
                list2 = list2.next
        
        if list1 != None:
            head.next = list1
        
        if list2 != None:
            head.next = list2
        
        return pointer_to_head.next