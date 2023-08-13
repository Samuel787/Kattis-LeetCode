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
        if lists == None or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                j = i + 1
                if j < len(lists):
                    mergedLists.append(self.merge2Lists(lists[i], lists[j]))
                else:
                    mergedLists.append(lists[i])
            lists = mergedLists
        return lists[0]
        
    # This method gives u head
    def merge2Lists(self, one, two):
        if one == None and two == None:
            return None
        head = None
        curr = None
        while one != None and two != None:
            if one.val <= two.val:
                if curr == None:
                    curr = one
                    head = curr
                else:
                    curr.next = one
                    curr = curr.next
                one = one.next
            else:
                if curr == None:
                    curr = two
                    head = curr
                else:
                    curr.next = two
                    curr = curr.next
                two = two.next
        
        if one != None:
            if head == None:
                head = one
            else:
                curr.next = one
            
        if two != None:
            if head == None:
                head = two
            else:
                curr.next = two
        
        return head